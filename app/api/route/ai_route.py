from fastapi import APIRouter, Depends
from app.schemas.ai import AISchema

ai_route = APIRouter(prefix='/ai', tags=['AI'])

@ai_route.get('/data-model/{model}')
async def data_model(ai : AISchema = Depends()):
    return ai
        