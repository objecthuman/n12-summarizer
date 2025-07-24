from src.llm import summarize_with_query

# Sample chat messages
messages = [
    "user1: This is a test.",
    "user2: Yes, testing summarization.",
    "user1: Let's check how it works.",
]

summary = summarize_with_query(messages, "")
print("General Summary:\n", summary)

summary_with_query = summarize_with_query(messages, "what are they discussing?")
print("Query Summary:\n", summary_with_query)
