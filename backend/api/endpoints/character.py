import datetime
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import APIRouter, status

from core.config import settings
from ..models.character.schemas import CharacterModel, CharacterResponseModel, Search, SearchDetail
from .modules.character import (
    calc_all_skill_critical, get_character_critical_skill, get_crit, search_basic_info,
    search_skill_enforce_info, search_skill_info
)
from modules import make_api_url, make_img_url, request_to_api_server


router = APIRouter()
client = AsyncClient()
db_client = AsyncIOMotorClient(settings.DB_CONNECT_PATH)

db = db_client['character']
base_db = db_client['base_info']

job = base_db['job']
char_base = db['base']


@router.get("/search", status_code=status.HTTP_200_OK, response_model=CharacterResponseModel)
async def serch_user(request: Search):
    params = {
        "characterName": request.name,
        "jobId": request.jobId,
        "jobGrowId": request.jobGrowId,
        "wordType": "full",
        "limit": 100
    }
    url = make_api_url(f'servers/{request.server}/characters')
    data = await request_to_api_server(url, params)
    for char in data["rows"][:]:
        char["critical"] = None
        if char["level"] != settings.MAX_LEV:
            data["rows"].remove(char)
            continue
        character = (
            await char_base
            .find({"characterBasic.characterId": char["characterId"]})
            .sort("regTime", -1)
            .to_list(100)
        )
        if character:
            char["critical"] = character[0]["critical"]
        detail_char_url = f'servers/{char["serverId"]}/characters/{char["characterId"]}'
        char["charImg"] = make_img_url(f'{detail_char_url}?zoom=3')
    return {"data": data["rows"]}


@router.get("/search/detail", status_code=status.HTTP_200_OK, response_model=CharacterModel)
async def search_detail_user(request: SearchDetail):
    basic_data = await search_basic_info(request.serverId, request.characterId)
    skill_data = await search_skill_info(request.serverId, request.characterId)
    skill_enforce_equip_data = await search_skill_enforce_info(request.serverId, request.characterId, 'equipment')
    critical = await get_crit(job, request)

    buff_skill = skill_enforce_equip_data["skill"]["buff"]["skillInfo"]
    crit_skill = get_character_critical_skill(basic_data["jobId"], basic_data["jobGrowId"])
    add_skill_critical = calc_all_skill_critical(crit_skill, buff_skill, skill_data)

    critical += add_skill_critical
    data = {
        "characterBasic": basic_data,
        "critical": critical,
        "regTime": datetime.datetime.now()
    }
    insert_data = jsonable_encoder(data)
    await char_base.insert_one(insert_data)

    return data
