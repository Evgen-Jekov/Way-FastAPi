from pydantic import BaseModel
from app.enums.ai import AIEnum

class AISchema(BaseModel):
    model : AIEnum
    version : float | None = None