from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class SoilHealth(BaseModel):
    ph: Optional[float] = Field(None, description="Soil pH level")
    organic_carbon_percent: Optional[float] = Field(None, description="Soil organic carbon percentage")
    moisture_level: Optional[str] = Field(None, description="e.g., low, medium, high")

class Climate(BaseModel):
    temperature_celsius: Optional[float] = Field(None, description="Average temperature")
    rainfall_pattern: Optional[str] = Field(None, description="e.g., low, heavy, seasonal")

class EnvironmentalContext(BaseModel):
    soil_health: SoilHealth = Field(default_factory=SoilHealth)
    climate: Climate = Field(default_factory=Climate)
    land_use: Optional[str] = Field(None, description="e.g., monoculture wheat, agroforestry")
    region: Optional[str] = Field(None, description="e.g., semi-arid, tropical")

# Schema for the LLM to strictly output extracted facts
class ExtractedContext(BaseModel):
    soil_ph: Optional[float] = None
    soil_organic_carbon_percent: Optional[float] = None
    soil_moisture_level: Optional[str] = None
    climate_temperature_celsius: Optional[float] = None
    climate_rainfall_pattern: Optional[str] = None
    land_use: Optional[str] = None
    region: Optional[str] = None

class ChatRequest(BaseModel):
    session_id: str = Field(..., description="Unique ID for the conversation session")
    user_message: str

class ChatResponse(BaseModel):
    reply: str
    updated_context: dict
    is_recommendation: bool