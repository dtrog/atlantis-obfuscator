
from pydantic import BaseModel, ValidationError
from typing import List, Dict, Optional

class LexAtlantisVolume(BaseModel):
    title: str
    sections: Dict[str, str]

class FictionEntry(BaseModel):
    title: str
    author: Optional[str]
    body: str

class UserGuidance(BaseModel):
    persona: str
    tone: str
    style: str
    constraints: Optional[Dict[str, str]]

class MemorySchema(BaseModel):
    lex_atlantis: Optional[Dict[str, LexAtlantisVolume]]
    fiction_pool: Optional[List[FictionEntry]]
    guidance: Optional[UserGuidance]

def validate_memory(payload: dict):
    try:
        validated = MemorySchema(**payload)
        return validated.dict()
    except ValidationError as e:
        return {"error": e.errors()}
