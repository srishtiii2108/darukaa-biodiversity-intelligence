from conversation_manager import conversation_manager

if __name__ == "__main__":
    print("--- Testing Complete Upgraded Backend Flow ---")
    session_id = "test_session_pro_01"
    
    # Turn 1: Partial input (should trigger clarification)
    print("\n[Turn 1] User: 'My biodiversity is declining.'")
    res1 = conversation_manager.process_turn(session_id, "My biodiversity is declining.")
    print(f"AI: {res1['reply']}")
    
    # Turn 2: Providing remaining context (should trigger RAG + Reasoning)
    print("\n[Turn 2] User: 'My rainfall is low, I grow monoculture wheat, and soil carbon is 0.3%'")
    res2 = conversation_manager.process_turn(session_id, "My rainfall is low, I grow monoculture wheat, and soil carbon is 0.3%")
    print(f"AI:\n{res2['reply']}")