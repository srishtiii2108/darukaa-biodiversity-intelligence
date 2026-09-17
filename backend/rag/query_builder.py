from schemas import EnvironmentalContext

def build_context_aware_query(user_message: str, context: EnvironmentalContext) -> str:
    """
    Combines the user's raw message with structured environmental context 
    to build a powerful multi-variable semantic query for the vector database.
    """
    query_parts = [user_message]

    # Extract soil variables safely
    soil = context.soil_health
    if soil.organic_carbon_percent is not None:
        query_parts.append(f"soil organic carbon {soil.organic_carbon_percent}%")
    if soil.moisture_level:
        query_parts.append(f"soil moisture {soil.moisture_level}")
    if soil.ph is not None:
        query_parts.append(f"soil pH {soil.ph}")

    # Extract climate variables safely
    climate = context.climate
    if climate.rainfall_pattern:
        query_parts.append(f"rainfall pattern {climate.rainfall_pattern}")
    if climate.temperature_celsius is not None:
        query_parts.append(f"temperature {climate.temperature_celsius} celsius")

    # Extract land use & region safely
    if context.land_use:
        query_parts.append(f"land use practice {context.land_use}")
    if context.region:
        query_parts.append(f"region {context.region}")

    # Combine everything into a rich scientific search string
    enhanced_query = " ".join(query_parts)
    print(f"🔍 Context-Aware Query Built: '{enhanced_query}'")
    return enhanced_query