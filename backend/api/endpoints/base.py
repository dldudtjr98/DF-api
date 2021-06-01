from typing import List

from httpx import AsyncClient
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from api.models.base.schemas import JobModel, ServerModel
from modules import if_none_insert, make_api_url, request_to_api_server


router = APIRouter()
client = AsyncClient()
db_client = AsyncIOMotorClient(settings.DB_CONNECT_PATH)

db = db_client['base_info']
job = db['job']
server = db['server']


@router.post("/server", status_code=status.HTTP_201_CREATED)
async def create_server():
    url = make_api_url('servers')
    data = await request_to_api_server(url)
    print(data)
    data = jsonable_encoder(data["rows"])
    await if_none_insert(server, data, 'serverName')
    return {"data": 'ok'}


@router.get("/server", status_code=status.HTTP_200_OK, response_model=List[ServerModel])
async def get_server():
    servers = await server.find().to_list(100)
    return servers


@router.post("/job", status_code=status.HTTP_201_CREATED)
async def create_job():
    url = make_api_url('jobs')
    data = await request_to_api_server(url)
    print(data)
    for base_job in data["rows"]:  # 귀검사(남), 귀검사(여), ...
        for index, adv_job in enumerate(base_job["rows"]):  # 웨펀마스터, 소울브링어, ...
            while "next" in adv_job:
                final = adv_job["next"]
                adv_job = adv_job["next"]
            base_job["rows"][index] = final
        base_job["advance"] = base_job.pop("rows")
    data = jsonable_encoder(data["rows"])
    await if_none_insert(job, data, 'jobName')
    return {"data": 'ok'}


@router.get("/job", status_code=status.HTTP_200_OK, response_model=List[JobModel])
async def get_job():
    jobs = await job.find().to_list(100)
    return jobs
