# code realted to llm. 
# for ex: llm prompts, function that asks llm for summary.

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document

from src.qdrant import qdrant_client 
from src.config import settings

def summarize_with_query(messages: list[str], query: str) -> str:
    if not messages:
        return "No messages to summarize."

    # Set up embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

    collection_name = "chat_messages"

    # Optionally recreate the collection ( fresh vectors each time)
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config={
            "size": 1536,
            "distance": "Cosine"
        }
    )

    # Wrap messages in LangChain Document objects
    docs = [Document(page_content=msg) for msg in messages]

    # Store in Qdrant
    vector_store = Qdrant.from_documents(
        documents=docs,
        embedding=embeddings,
        url="https://32b17cf0-eb4a-4dfc-a750-9fb0677cdb4a.eu-central-1-0.aws.cloud.qdrant.io:6333",
        api_key=settings.QDRANT_API_KEY,
        collection_name=collection_name,
        batch_size=10
    )

    # LLM
    llm = ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY)

    #  If user provided a query , do RetrievalQA
    if query.strip():
        retriever = vector_store.as_retriever(search_type="similarity", k=5)
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        return qa.invoke(query)["result"]

    #  If no query , do general summarization
    else:
        summarize_chain = load_summarize_chain(llm, chain_type="stuff")
        result = summarize_chain.invoke(docs)
        return result["output_text"] 