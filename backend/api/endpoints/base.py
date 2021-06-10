from httpx import AsyncClient
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from api.models.base.schemas import (
    JobResponseModel, JobSkillResponseModel, ServerResponseModel, SkillSearch, SkillSearchDetail
)
from api.endpoints.modules.base import insert_data
from modules import make_api_url, request_to_api_server


router = APIRouter()
client = AsyncClient()
db_client = AsyncIOMotorClient(settings.DB_CONNECT_PATH)

db = db_client['base_info']
job = db['job']
server = db['server']


@router.post("/server", status_code=status.HTTP_201_CREATED, response_model=ServerResponseModel)
async def create_server():
    url = make_api_url('servers')
    data = await request_to_api_server(url)
    data = jsonable_encoder(data["rows"])
    return {"data": "OK"}


@router.get("/server", status_code=status.HTTP_200_OK, response_model=ServerResponseModel)
async def get_server():
    servers = await server.find().to_list(100)
    return {"data": servers}


@router.post("/job", status_code=status.HTTP_201_CREATED, response_model=JobResponseModel)
async def create_job():
    url = make_api_url('jobs')
    data = await request_to_api_server(url)
    for base_job in data["rows"]:  # 귀검사(남), 귀검사(여), ...
        for adv_job in base_job["rows"]:  # 웨펀마스터, 소울브링어, ...
            while "next" in adv_job:
                final = adv_job["next"]
                adv_job = adv_job["next"]
            await insert_data(job, base_job, final)
    return {"data": "OK"}


@router.get("/job", status_code=status.HTTP_200_OK, response_model=JobResponseModel)
async def get_job():
    jobs = await job.find().to_list(100)
    return {"data": jobs}


@router.get("/skill", status_code=status.HTTP_200_OK, response_model=JobSkillResponseModel)
async def get_skill(request: SkillSearch):
    params = {
        "jobGrowId": request.jobGrowId,
    }
    url = make_api_url(f'skills/{request.jobId}')
    data = await request_to_api_server(url, params)
    return {"data": data["skills"]}


@router.get("/skill/detail", status_code=status.HTTP_200_OK)
async def get_skill_detail(request: SkillSearchDetail):
    url = make_api_url(f'skills/{request.jobId}/{request.skillId}')
    data = await request_to_api_server(url)
    return {"data": data}
