import os
import json
import cohere
from dotenv import load_dotenv
from rag_engine import retrieve_context
from schemas import EnvironmentalContext, SoilHealth, Climate

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_recommendation(user_message: str, current_context: EnvironmentalContext) -> dict:
    """Uses Cohere LLM to reason over environmental context and retrieved facts."""
    
    # 1. Retrieve Scientific Facts via RAG
    retrieved_facts = retrieve_context(user_message, top_k=2)
    
    evidence_text = ""
    for r in retrieved_facts:
        evidence_text += f"- {r['fact']} (Source: {r['source']})\n"
        
    # 2. Format Environmental Variables
    env_state = current_context.model_dump_json(indent=2)
    
    # 3. Define the AI Persona and Strict JSON Output Schema
    system_prompt = """You are a Senior AI Environmental Scientist.
Your job is to provide actionable, evidence-backed environmental recommendations based on the user's context and retrieved scientific facts.
You MUST connect multiple environmental variables (e.g., soil health, climate, land use) in your reasoning.

Output MUST be strictly in the following JSON structure:
{
  "recommendation": "Specific action to take",
  "why_it_works": "Scientific reasoning combining multiple variables",
  "impacted_metrics": ["Metric 1", "Metric 2"],
  "time_horizon": "Short/Medium/Long term",
  "evidence": "Reference the provided scientific source"
}"""

    user_prompt = f"""
User Query: {user_message}

Current Environmental State:
{env_state}

Retrieved Scientific Evidence:
{evidence_text}
"""

    # 4. Generate Response using Cohere
    print("🧠 AI Scientist is reasoning across variables... Please wait.")
    response = co.chat(
        message=user_prompt,
        preamble=system_prompt,
        model="command-xlarge-nightly",
        response_format={"type": "json_object"}
    )
    
    # Parse and return the JSON response
    return json.loads(response.text)

if __name__ == "__main__":
    # Test the reasoning engine
    print("--- Testing Reasoning Engine ---")
    
    # Mocking a structured input from the user
    test_context = EnvironmentalContext(
        soil_health=SoilHealth(organic_carbon_percent=0.3, moisture_level="low"),
        climate=Climate(rainfall_pattern="low"),
        land_use="monoculture wheat",
        region="semi-arid"
    )
    
    test_query = "Biodiversity is declining on my land, what should I do?"
    
    final_output = generate_recommendation(test_query, test_context)
    
    print("\n✅ Final Structured Recommendation:")
    print(json.dumps(final_output, indent=2))