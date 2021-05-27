import json
from httpx import AsyncClient
from fastapi import FastAPI, status, Request
from api.api import api_router
from core.config import settings


app = FastAPI()
client = AsyncClient()


async def request_to_api_server(url):
    resp = await client.get(url)
    return json.loads(resp.text)


def make_url(chunk_url):
    url = f'{settings.DF_API_SERVER}{chunk_url}?apikey={settings.DF_API_KEY}'
    return url


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def index():
    return {"message": "I'm health"}


@app.get("/server", status_code=status.HTTP_200_OK)
async def serch_user():
    url = make_url('servers')
    data = await request_to_api_server(url)
    return {"data": data["rows"]}


@app.get("/job", status_code=status.HTTP_200_OK)
async def search_job():
    url = make_url('jobs')
    data = await request_to_api_server(url)
    for base_job in data["rows"]:  # 귀검사(남), 귀검사(여), ...
        for index, adv_job in enumerate(base_job["rows"]):  # 웨펀마스터, 소울브링어, ...
            while "next" in adv_job:
                final = adv_job["next"]
                adv_job = adv_job["next"]
            base_job["rows"][index] = final
        base_job["advance"] = base_job.pop("rows")
    return {"data": data["rows"]}


app.include_router(api_router, prefix='')
