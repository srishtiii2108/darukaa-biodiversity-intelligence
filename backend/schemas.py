from pydantic import BaseModel, Field
from typing import Optional

class SoilHealth(BaseModel):
    ph: Optional[float] = Field(None, description="Soil pH level")
    organic_carbon_percent: Optional[float] = Field(None, description="Soil organic carbon percentage")
    moisture_level: Optional[str] = Field(None, description="e.g., low, medium, high")

class Climate(BaseModel):
    temperature_celsius: Optional[float] = Field(None, description="Average temperature")
    rainfall_pattern: Optional[str] = Field(None, description="e.g., low, heavy, seasonal")

class EnvironmentalContext(BaseModel):
    soil_health: Optional[SoilHealth] = Field(default_factory=SoilHealth)
    climate: Optional[Climate] = Field(default_factory=Climate)
    land_use: Optional[str] = Field(None, description="e.g., monoculture wheat, agroforestry")
    region: Optional[str] = Field(None, description="e.g., semi-arid, tropical")
    biodiversity_status: Optional[str] = Field(None, description="e.g., declining, stable")

class ChatRequest(BaseModel):
    user_message: str
    context: Optional[EnvironmentalContext] = Field(default_factory=EnvironmentalContext)
    
class ChatResponse(BaseModel):
    reply: str
    updated_context: EnvironmentalContext