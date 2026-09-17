def validate_context(context_dict: dict) -> dict:
    """
    Evaluates if the extracted context has enough variables (at least 3)
    to make a scientifically grounded recommendation.
    """
    soil_vars = ["ph", "organic_carbon_percent", "moisture_level"]
    climate_vars = ["temperature_celsius", "rainfall_pattern"]
    land_vars = ["land_use", "region"]

    known_vars = []
    missing_high_value = []

    # 1. Check Soil Context
    soil_health = context_dict.get("soil_health", {})
    if hasattr(soil_health, "__dict__"): # If it's a pydantic object
        soil_health = soil_health.model_dump()
        
    for v in soil_vars:
        if soil_health.get(v) is not None:
            known_vars.append(f"soil {v}")
        elif len(missing_high_value) < 2 and v in ["organic_carbon_percent", "moisture_level"]:
            missing_high_value.append(f"soil {v.replace('_', ' ')}")

    # 2. Check Climate Context
    climate = context_dict.get("climate", {})
    if hasattr(climate, "__dict__"):
        climate = climate.model_dump()
        
    for v in climate_vars:
        if climate.get(v) is not None:
            known_vars.append(f"climate {v}")
        elif len(missing_high_value) < 2 and v == "rainfall_pattern":
            missing_high_value.append("rainfall pattern")

    # 3. Check Land Context
    for v in land_vars:
        if context_dict.get(v) is not None:
            known_vars.append(v)
        elif len(missing_high_value) < 2 and v == "land_use":
            missing_high_value.append("land use type")

    # The Core Rule: We need at least 3 variables for multi-metric reasoning
    is_sufficient = len(known_vars) >= 3

    # Generate a smart, concise question based on what's missing
    clarification_question = None
    if not is_sufficient:
        if missing_high_value:
            clarification_question = (
                "To give you a scientifically accurate recommendation, I need a bit more context. "
                f"Could you share your {', '.join(missing_high_value)}?"
            )
        else:
            clarification_question = "Could you provide some details about your soil health, rainfall, or land use?"

    return {
        "is_sufficient": is_sufficient,
        "known_count": len(known_vars),
        "clarification_question": clarification_question
    }

if __name__ == "__main__":
    print("--- Testing Context Validator ---")
    
    # Test 1: Only 1 variable (Should ask for more)
    test_context_1 = {
        "soil_health": {"organic_carbon_percent": 0.3},
        "climate": {},
        "land_use": None,
        "region": None
    }
    print("\nTest 1 (1 variable known):")
    result_1 = validate_context(test_context_1)
    print(f"Is Sufficient? {result_1['is_sufficient']}")
    print(f"Question: {result_1['clarification_question']}")

    # Test 2: 3 variables (Should be sufficient)
    test_context_2 = {
        "soil_health": {"organic_carbon_percent": 0.3},
        "climate": {"rainfall_pattern": "low"},
        "land_use": "monoculture wheat",
        "region": None
    }
    print("\nTest 2 (3 variables known):")
    result_2 = validate_context(test_context_2)
    print(f"Is Sufficient? {result_2['is_sufficient']}")