import json
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


app = FastAPI()
client = AsyncClient()

MONGO_DETAILS = f"mongodb://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}"
db_client = AsyncIOMotorClient(MONGO_DETAILS)

db = db_client['base_info']
job = db['job']
server = db['server']


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


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


async def request_to_api_server(url):
    resp = await client.get(url)
    return json.loads(resp.text)


def make_url(chunk_url):
    url = f'{settings.DF_API_SERVER}{chunk_url}?apikey={settings.DF_API_KEY}'
    return url


async def if_none_insert(table, data, key):
    for frag in data:
        doc_key = await table.find_one({key: frag[key]})
        if doc_key is None:
            await table.insert_one(frag)


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def index():
    return {"message": "I'm health"}


@app.post("/server", status_code=status.HTTP_201_CREATED)
async def create_server():
    url = make_url('servers')
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
    url = make_url('jobs')
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
