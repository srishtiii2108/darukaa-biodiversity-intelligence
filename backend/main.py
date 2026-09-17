from fastapi import FastAPI, HTTPException
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
        # Route the request through our new conversational orchestrator
        result = conversation_manager.process_turn(
            session_id=request.session_id,
            user_message=request.user_message
        )
        return result
    except Exception as e:
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during conversation processing.")