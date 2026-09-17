import os
import json
import cohere
from dotenv import load_dotenv

# Load API Key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def extract_environmental_data(user_message: str) -> dict:
    """
    Uses Cohere LLM to extract environmental variables from natural language.
    Returns a dictionary matching the ExtractedContext schema.
    """
    
    system_prompt = """You are an expert environmental data extractor.
Your job is to read the user's message and extract any environmental metrics mentioned.
If a parameter is NOT mentioned, you MUST set its value to null. Do not guess or hallucinate values.

Output MUST be strictly in the following JSON format:
{
    "soil_ph": float or null,
    "soil_organic_carbon_percent": float or null,
    "soil_moisture_level": string or null (e.g., "low", "medium", "high"),
    "climate_temperature_celsius": float or null,
    "climate_rainfall_pattern": string or null (e.g., "low", "medium", "high"),
    "land_use": string or null (e.g., "monoculture wheat", "agroforestry"),
    "region": string or null (e.g., "semi-arid", "tropical")
}"""

    try:
        response = co.chat(
            message=user_message,
            preamble=system_prompt,
            model="command-xlarge-nightly",
            response_format={"type": "json_object"}
        )
        # Parse the JSON string returned by the LLM into a Python dictionary
        return json.loads(response.text)
    except Exception as e:
        print(f"⚠️ Extraction Error: {e}")
        return {}  # Return empty dict if extraction fails so the app doesn't crash

if __name__ == "__main__":
    # Let's test the extractor independently
    test_msg = "My land has very low rainfall and we grow wheat continuously. The soil carbon is about 0.3%."
    
    print("🧠 Extracting data from message...")
    print(f"User: '{test_msg}'\n")
    
    extracted = extract_environmental_data(test_msg)
    
    print("✅ Extracted JSON:")
    print(json.dumps(extracted, indent=2))