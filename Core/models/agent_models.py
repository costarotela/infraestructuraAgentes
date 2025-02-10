from pydantic import BaseModel, validator, Field
from typing import List, Dict, Optional

class AgentConfig(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)
    version: str = Field(regex=r'^\d+\.\d+\.\d+$')
    capabilities: List[str]
    metadata: Dict[str, str] = {}
    
    @validator('capabilities')
    def validate_capabilities(cls, v):
        if not v:
            raise ValueError('Debe tener al menos una capacidad')
        return v

class SalesAgentConfig(AgentConfig):
    industry: str
    customer_segments: List[str]
    sales_kpis: Dict[str, float]

class AgentIO(BaseModel):
    input: Dict[str, str]
    output: Dict[str, str]
    context: Optional[Dict[str, str]]
