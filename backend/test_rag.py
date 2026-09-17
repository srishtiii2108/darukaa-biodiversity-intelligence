from rag.rag_engine import retrieve_scientific_evidence
from schemas import EnvironmentalContext, SoilHealth, Climate

if __name__ == "__main__":
    print("--- Testing Upgraded Context-Aware RAG ---")
    
    # Mock environment state with multiple variables
    mock_context = EnvironmentalContext(
        soil_health=SoilHealth(organic_carbon_percent=0.3, moisture_level="low"),
        climate=Climate(rainfall_pattern="low"),
        land_use="monoculture wheat",
        region="semi-arid"
    )
    
    user_query = "Biodiversity is declining, how do I fix soil health?"
    
    evidence_list = retrieve_scientific_evidence(user_query, mock_context, top_k=2)
    
    print("\n✅ Retrieved Evidence Results:")
    for ev in evidence_list:
        print(f"\n- Chunk ID: {ev['chunk_id']}")
        print(f"  Source: {ev['organization']} ({ev['title']})")
        print(f"  Fact: {ev['fact'][:120]}...")