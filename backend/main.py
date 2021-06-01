from typing import List

from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from pydantic.fields import Field
from pydantic.main import BaseModel
from httpx import AsyncClient
from fastapi import FastAPI, status
from api.api import api_router
from core.config import settings
from modules import PyObjectId, if_none_insert, make_api_url, request_to_api_server


app = FastAPI()
client = AsyncClient()
db_client = AsyncIOMotorClient(settings.DB_CONNECT_PATH)

db = db_client['base_info']
job = db['job']
server = db['server']


class JobModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    jobId: str = Field(...)
    jobName: str = Field(...)
    advance: List[dict] = []

    class Config:
        json_encoders = {ObjectId: str}


class ServerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    serverId: str = Field(...)
    serverName: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def index():
    return {"message": "I'm health"}


@app.post("/server", status_code=status.HTTP_201_CREATED)
async def create_server():
    url = make_api_url('servers')
    data = await request_to_api_server(url)
    print(data)
    data = jsonable_encoder(data["rows"])
    await if_none_insert(server, data, 'serverName')
    return {"data": 'ok'}


@app.get("/server", status_code=status.HTTP_200_OK, response_model=List[ServerModel])
async def get_server():
    servers = await server.find().to_list(100)
    return servers


@app.post("/job", status_code=status.HTTP_201_CREATED)
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


@app.get("/job", status_code=status.HTTP_200_OK, response_model=List[JobModel])
async def get_job():
    jobs = await job.find().to_list(100)
    return jobs


app.include_router(api_router, prefix='')
