import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from app.settings import (
    VECTOR_DB_PERSIST_PATH,
    VECTOR_DB_COLLECTION,
    VECTOR_DB_N_RESULTS,
)


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


class VectorDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=VECTOR_DB_PERSIST_PATH, settings=Settings(anonymized_telemetry=False)
        )
        self.collection = self.client.get_or_create_collection(
            name=VECTOR_DB_COLLECTION,
            metadata={"hnsw:space": "cosine"},
        )

    def add(self, id: str, content: str, metadata: dict[str, str]) -> bool:
        embedding = embedding_model.encode(content).tolist()

        try:
            self.collection.add(
                ids=[id],
                documents=[content],
                embeddings=[embedding],
                metadatas=[metadata],
            )
        except ValueError:
            return False

        return True

    def get(self, query: str, n_results: int = VECTOR_DB_N_RESULTS) -> dict:
        query_embedding = embedding_model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )

        return results  # type: ignore

    def query(self, question, n_results):
        result = self.collection.query(query_texts=[question], n_results=n_results)

        return result


db = VectorDB()
