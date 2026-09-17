import os
import json
import cohere
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("Missing COHERE_API_KEY in .env")

co = cohere.Client(COHERE_API_KEY)

# Initialize Vector DB
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')
chroma_client = chromadb.PersistentClient(path=DB_PATH)

# We will create a new production collection
collection = chroma_client.get_or_create_collection(name="darukaa_scientific_kb")

def run_pipeline():
    print("🚀 Starting Scientific Document Ingestion Pipeline...")
    
    # 1. Load Source Registry
    registry_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'source_registry.json')
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry = json.load(f)

    # 2. Configure Semantic Chunker (800 tokens, 150 overlap)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " "]
    )

    documents_to_embed = []
    metadatas = []
    ids = []

    # 3. Read raw text, Chunk, and Attach Metadata
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    
    for source_id, meta in registry.items():
        filepath = os.path.join(raw_dir, f"{source_id}.txt")
        if not os.path.exists(filepath):
            print(f"⚠️ Warning: Raw text for {source_id} not found. Skipping.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        # Split into smart chunks
        chunks = text_splitter.split_text(text)
        
        for i, chunk in enumerate(chunks):
            documents_to_embed.append(chunk)
            # Critical: Store ID for traceability
            chunk_id = f"{source_id}_chunk_{i}"
            ids.append(chunk_id)
            
            # Enrich Metadata
            metadatas.append({
                "source_id": source_id,
                "title": meta["title"],
                "organization": meta["organization"],
                "topics": ", ".join(meta["topics"]) if "topics" in meta else "",
                "url": meta["url"]
            })
            print(f"📦 Prepared chunk: {chunk_id}")

    # 4. Generate Embeddings using Cohere V3 (Document Mode)
    if documents_to_embed:
        print(f"🧠 Embedding {len(documents_to_embed)} chunks via Cohere...")
        response = co.embed(
            texts=documents_to_embed,
            model="embed-english-v3.0",
            input_type="search_document" # Strict requirement for RAG documents
        )
        embeddings = response.embeddings

        # 5. Upsert to ChromaDB
        print("💾 Saving to Vector Database...")
        collection.upsert(
            documents=documents_to_embed,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        print(f"✅ Ingestion Complete! Total documents in DB: {collection.count()}")
    else:
        print("No documents found to ingest.")

if __name__ == "__main__":
    run_pipeline()