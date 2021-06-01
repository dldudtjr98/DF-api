from typing import List
from bson import ObjectId
from pydantic.fields import Field
from pydantic.main import BaseModel
from modules import PyObjectId


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
