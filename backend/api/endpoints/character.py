import json
from typing import Optional

from pydantic.main import BaseModel
from httpx import AsyncClient

from fastapi import (
    APIRouter, status
)
from core.config import settings


router = APIRouter()
client = AsyncClient()


async def request_to_api_server(url, params={}):
    params['apikey'] = settings.DF_API_KEY
    resp = await client.get(url, params=params)
    return json.loads(resp.text)


def make_api_url(chunk_url):
    url = f'{settings.DF_API_SERVER}{chunk_url}'
    return url


def make_img_url(chunk_url):
    url = f'{settings.DF_IMG_SERVER}{chunk_url}'
    return url


class Search(BaseModel):
    name: str
    server: Optional[str] = 'all'
    jobId: Optional[str] = ''
    jobGrowId: Optional[str] = ''


@router.get("/search", status_code=status.HTTP_200_OK)
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
        if char["level"] != settings.MAX_LEV:
            data["rows"].remove(char)
            continue
        detail_char_url = f'servers/{char["serverId"]}/characters/{char["characterId"]}'
        char["charImg"] = make_img_url(f'{detail_char_url}?zoom=3')
    return {"data": data["rows"]}


class SearchDetail(BaseModel):
    serverId: str
    characterId: str


async def search_basic_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}')
    data = await request_to_api_server(url)
    return data


async def search_equip_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/equip/equipment')
    data = await request_to_api_server(url)
    return data


async def search_skill_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/skill/style')
    data = await request_to_api_server(url)
    return data


async def search_skill_detail_info(job_id, skill_id):
    url = make_api_url(f'skills/{job_id}/{skill_id}')
    data = await request_to_api_server(url)
    return data


async def job_info():
    url = make_api_url(f'jobs')
    data = await request_to_api_server(url)
    return data


async def search_status_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/status')
    data = await request_to_api_server(url)
    return data


@router.get("/search/detail", status_code=status.HTTP_200_OK)
async def search_detail_user(request: SearchDetail):
    basic_data = await search_basic_info(request.serverId, request.characterId)
    equip_data = await search_equip_info(request.serverId, request.characterId)
    skill_data = await search_skill_info(request.serverId, request.characterId)
    skill_data = await search_skill_info(request.serverId, request.characterId)
    status_data = await search_status_info(request.serverId, request.characterId)
    critical = [status for status in status_data["status"] if status["name"] == "물리 크리티컬"][0]["value"]
    detail_skill_data = {}
    for active in skill_data["skill"]["style"]["active"]:
        if active["skillId"] in settings.CRIT_ACTIVE:
            detail_skill_data = await search_skill_detail_info(basic_data["jobId"], active["skillId"])

    return {
        "basic_data": basic_data,
        "equip_data": equip_data,
        "skill_data": skill_data,
        "detail_skill_data": detail_skill_data,
        "status_data": critical
    }
