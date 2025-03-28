from fastapi import FastAPI
from app.api.route import ai_route

app = FastAPI(debug=True)
app.include_router(ai_route.ai_route)