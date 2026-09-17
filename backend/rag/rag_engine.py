import os
import cohere
import chromadb
from dotenv import load_dotenv
from schemas import EnvironmentalContext
from rag.query_builder import build_context_aware_query

# Load Environment Variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("Missing COHERE_API_KEY in .env")

co = cohere.Client(COHERE_API_KEY)

# Connect to the production ChromaDB collection
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')
chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="darukaa_scientific_kb")

def get_query_embedding(query_text: str) -> list[float]:
    """Generates embedding for a search query using Cohere V3 query mode."""
    response = co.embed(
        texts=[query_text],
        model="embed-english-v3.0",
        input_type="search_query" # Strict requirement for retrieval queries
    )
    return response.embeddings[0]

def retrieve_scientific_evidence(user_message: str, context: EnvironmentalContext, top_k: int = 3) -> list[dict]:
    """
    Performs context-aware vector retrieval from ChromaDB with full metadata traceability.
    """
    # 1. Build the advanced search query
    smart_query = build_context_aware_query(user_message, context)
    
    # 2. Get embedding
    query_embedding = get_query_embedding(smart_query)
    
    # 3. Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    retrieved_evidence = []
    
    if results['documents'] and len(results['documents'][0]) > 0:
        docs = results['documents'][0]
        metadatas = results['metadatas'][0]
        ids = results['ids'][0]
        
        for i in range(len(docs)):
            meta = metadatas[i]
            retrieved_evidence.append({
                "chunk_id": ids[i],
                "fact": docs[i],
                "source_id": meta.get("source_id"),
                "title": meta.get("title"),
                "organization": meta.get("organization"),
                "url": meta.get("url")
            })
            
    print(f"📚 Retrieved {len(retrieved_evidence)} authoritative evidence chunks.")
    return retrieved_evidence