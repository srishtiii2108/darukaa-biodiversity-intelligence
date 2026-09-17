from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatRequest
from conversation_manager import conversation_manager

app = FastAPI(
    title="Darukaa AI Environmental Scientist API",
    description="Conversational Backend for AI Biodiversity Intelligence System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "active", "system": "Darukaa AI Backend is running properly."}

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    try:
        result = conversation_manager.process_turn(
            session_id=request.session_id,
            user_message=request.user_message
        )
        return result
    except Exception as e:
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during conversation processing.")

@app.post("/api/upload")
async def upload_document(session_id: str = Form(...), file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")
        
        if not text.strip():
            raise HTTPException(status_code=400, detail="Uploaded file is empty or unreadable.")
        
        from rag.rag_engine import co, collection
        
        chunk_size = 1000
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        
        response = co.embed(
            texts=chunks,
            model="embed-english-v3.0",
            input_type="search_document"
        )
        
        ids = [f"{session_id}_{file.filename}_chunk_{i}" for i in range(len(chunks))]
        metadatas = [{
            "source_id": f"upload_{file.filename}",
            "title": file.filename,
            "organization": "Custom Session Upload",
            "url": "User Provided Document",
            "session_id": session_id
        } for _ in range(len(chunks))]
        
        collection.add(
            documents=chunks,
            embeddings=response.embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        return {"message": "Document ingested successfully", "filename": file.filename, "chunks": len(chunks)}
    except Exception as e:
        print(f"Upload Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))