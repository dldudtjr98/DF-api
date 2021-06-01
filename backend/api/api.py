from fastapi import APIRouter

from api.endpoints import base, character

api_router = APIRouter()
api_router.include_router(character.router, prefix="/character", tags=["character"])
api_router.include_router(base.router, prefix="/base", tags=["base"])
