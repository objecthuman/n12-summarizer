from qdrant_client import QdrantClient
from src.config import settings


qdrant_client = QdrantClient(
    url="https://32b17cf0-eb4a-4dfc-a750-9fb0677cdb4a.eu-central-1-0.aws.cloud.qdrant.io:6333", 
    api_key= settings.QDRANT_API_KEY
)


