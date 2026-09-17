import os
import json
import cohere
from dotenv import load_dotenv
from rag.rag_engine import retrieve_scientific_evidence
from schemas import EnvironmentalContext

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_recommendation(user_message: str, current_context: EnvironmentalContext) -> dict:
    """
    Uses Cohere LLM to reason over environmental context and retrieved authoritative RAG evidence.
    Enforces strict citation traceability back to source registry metadata.
    """
    
    # 1. Retrieve authoritative scientific evidence using our upgraded RAG engine
    retrieved_evidence = retrieve_scientific_evidence(user_message, current_context, top_k=3)
    
    evidence_text = ""
    evidence_mapping = {}
    
    for i, ev in enumerate(retrieved_evidence):
        tag = f"[EVIDENCE_{i+1}]"
        evidence_text += f"{tag} (Source: {ev['organization']} - {ev['title']} | ID: {ev['chunk_id']})\nFact: {ev['fact']}\n\n"
        evidence_mapping[f"EVIDENCE_{i+1}"] = {
            "source_id": ev['source_id'],
            "title": ev['title'],
            "organization": ev['organization'],
            "url": ev['url']
        }
        
    # 2. Format Environmental Variables
    env_state = current_context.model_dump_json(indent=2)
    
    # 3. Define the AI Persona and Strict JSON Output Schema
    system_prompt = """You are a Senior AI Environmental Scientist.
Your job is to provide actionable, evidence-backed environmental recommendations based on the user's context and retrieved scientific evidence.
You MUST connect multiple environmental variables (e.g., soil health, climate, land use) in your reasoning.
You MUST cite the specific evidence tags provided (e.g., [EVIDENCE_1]) when using facts from the text. Do NOT invent citations or URLs.

Output MUST be strictly in the following JSON structure:
{
  "recommendation": "Specific action to take",
  "why_it_works": "Scientific reasoning combining multiple variables with evidence tags",
  "impacted_metrics": ["Metric 1", "Metric 2"],
  "time_horizon": "Short/Medium/Long term",
  "evidence_tags_used": ["EVIDENCE_1"]
}"""

    user_prompt = f"""
User Query: {user_message}

Current Environmental State:
{env_state}

Retrieved Authoritative Scientific Evidence:
{evidence_text if evidence_text else "No direct scientific evidence found."}
"""

    try:
        print("🧠 AI Scientist is reasoning across variables using authoritative RAG...")
        response = co.chat(
            message=user_prompt,
            preamble=system_prompt,
            model="command-xlarge-nightly",
            response_format={"type": "json_object"}
        )
        
        result_json = json.loads(response.text)
        
        # Resolve evidence tags to real source metadata (Zero LLM Hallucination for citations)
        resolved_sources = []
        used_tags = result_json.get("evidence_tags_used", [])
        for tag in used_tags:
            clean_tag = tag.replace("[", "").replace("]", "")
            if clean_tag in evidence_mapping:
                resolved_sources.append(evidence_mapping[clean_tag])
                
        result_json["resolved_sources"] = resolved_sources
        return result_json

    except Exception as e:
        print(f"⚠️ Reasoning Engine Error: {e}")
        return {
            "recommendation": "Unable to process recommendation at this moment due to a reasoning error.",
            "why_it_works": str(e),
            "impacted_metrics": [],
            "time_horizon": "N/A",
            "resolved_sources": []
        }