import json

from core.config import settings
from bson.objectid import ObjectId
from httpx import AsyncClient

client = AsyncClient()


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


async def if_none_insert(table, data, key):
    for frag in data:
        doc_key = await table.find_one({key: frag[key]})
        if doc_key is None:
            await table.insert_one(frag)
