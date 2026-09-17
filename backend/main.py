from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatRequest
from reasoning_engine import generate_recommendation

app = FastAPI(
    title="Darukaa AI Environmental Scientist API",
    description="Backend for AI Biodiversity Intelligence System",
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
        # Get the structured JSON recommendation from our reasoning engine
        result_dict = generate_recommendation(
            user_message=request.user_message,
            current_context=request.context
        )
        
        # Format the output into a clean string for the frontend UI
        formatted_reply = f"🌱 **Recommendation:** {result_dict.get('recommendation')}\n\n"
        formatted_reply += f"🔬 **Why it works:** {result_dict.get('why_it_works')}\n\n"
        formatted_reply += f"📊 **Impacted Metrics:** {', '.join(result_dict.get('impacted_metrics', []))}\n\n"
        formatted_reply += f"⏱ **Time Horizon:** {result_dict.get('time_horizon')}\n\n"
        formatted_reply += f"📚 **Evidence:** {result_dict.get('evidence')}"
        
        return {
            "reply": formatted_reply,
            "updated_context": request.context.model_dump()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))