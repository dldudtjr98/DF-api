from fastapi import APIRouter

from api.endpoints import character

api_router = APIRouter()
api_router.include_router(character.router, prefix="/character", tags=["character"])
