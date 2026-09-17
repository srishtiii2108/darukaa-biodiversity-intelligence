from schemas import EnvironmentalContext
from typing import Dict, List

class ConversationSession:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.context = EnvironmentalContext()
        self.history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        """Adds a message to the chat history."""
        self.history.append({"role": role, "content": content})

    def update_context(self, extracted_data: dict):
        """Merges newly extracted data into the existing environmental context."""
        
        if extracted_data.get("soil_ph") is not None:
            self.context.soil_health.ph = extracted_data["soil_ph"]
        if extracted_data.get("soil_organic_carbon_percent") is not None:
            self.context.soil_health.organic_carbon_percent = extracted_data["soil_organic_carbon_percent"]
        if extracted_data.get("soil_moisture_level") is not None:
            self.context.soil_health.moisture_level = extracted_data["soil_moisture_level"]

        if extracted_data.get("climate_temperature_celsius") is not None:
            self.context.climate.temperature_celsius = extracted_data["climate_temperature_celsius"]
        if extracted_data.get("climate_rainfall_pattern") is not None:
            self.context.climate.rainfall_pattern = extracted_data["climate_rainfall_pattern"]

        if extracted_data.get("land_use") is not None:
            self.context.land_use = extracted_data["land_use"]
        if extracted_data.get("region") is not None:
            self.context.region = extracted_data["region"]

class MemoryManager:
    def __init__(self):
        # Stores sessions in memory for the MVP
        self.sessions: Dict[str, ConversationSession] = {}

    def get_session(self, session_id: str) -> ConversationSession:
        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationSession(session_id)
        return self.sessions[session_id]

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

# Singleton instance to be imported across the backend
memory_manager = MemoryManager()