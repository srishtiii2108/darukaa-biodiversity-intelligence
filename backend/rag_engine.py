import os
import json
import chromadb
import cohere
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY is missing! Please check your .env file.")

# 2. Configure Cohere API
co = cohere.Client(COHERE_API_KEY)

# 3. Initialize Vector Database (ChromaDB)
DB_PATH = "./chroma_db"
chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="environmental_knowledge")

# 4. Define the Embedding Function using Cohere
def get_embedding(text: str, is_query: bool = False) -> list[float]:
    """Converts text into mathematical vectors using Cohere"""
    # Cohere V3 models require input_type to be specified
    input_type = "search_query" if is_query else "search_document"
    
    response = co.embed(
        texts=[text],
        model="embed-english-v3.0",
        input_type=input_type
    )
    return response.embeddings[0]

# 5. Ingest Knowledge from JSON
def ingest_knowledge():
    """Reads scientific facts from JSON, creates embeddings, and saves to Vector DB"""
    if collection.count() > 0:
        print(f"Database already contains {collection.count()} documents. Skipping ingestion.")
        return

    print("Reading scientific knowledge base...")
    json_path = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_seed.json")
    
    with open(json_path, "r", encoding="utf-8") as f:
        knowledge_data = json.load(f)

    documents = []
    metadatas = []
    ids = []

    print("Generating mathematical vectors (embeddings) via Cohere API... Please wait.")
    for i, item in enumerate(knowledge_data):
        documents.append(item["fact"])
        metadatas.append({"source": item["source"], "topic": item["topic"]})
        ids.append(f"doc_{i}")

    # Add to ChromaDB
    embeddings = [get_embedding(doc, is_query=False) for doc in documents]
    
    collection.add(
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"✅ Successfully ingested {len(documents)} scientific facts into the Vector DB!")

# 6. Retrieve Knowledge
def retrieve_context(query: str, top_k: int = 2) -> list[dict]:
    """Searches the Vector DB for the most relevant scientific facts based on a query."""
    # Step A: Convert the user's query into an embedding
    query_embedding = get_embedding(query, is_query=True)
    
    # Step B: Search the DB for the closest matches
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    retrieved_facts = []
    if results['documents'] and len(results['documents']) > 0:
        for i in range(len(results['documents'][0])):
            retrieved_facts.append({
                "fact": results['documents'][0][i],
                "source": results['metadatas'][0][i]['source']
            })
    return retrieved_facts

if __name__ == "__main__":
    print("Vector DB Collection Name:", collection.name)
    
    # Run ingestion
    ingest_knowledge()
    
    print("Total documents currently in DB:", collection.count())
    
    # Test the retrieval pipeline
    print("\n--- Testing Retrieval Pipeline ---")
    test_query = "What should I do for low soil carbon and monoculture?"
    print(f"Query: {test_query}")
    
    results = retrieve_context(test_query)
    for r in results:
        print(f"\nSource: {r['source']}\nFact: {r['fact']}")