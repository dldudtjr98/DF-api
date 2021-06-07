from typing import List
from bson import ObjectId
from pydantic.fields import Field
from pydantic.main import BaseModel
from modules import PyObjectId


class JobModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    baseId: str = Field(...)
    baseName: str = Field(...)
    advancedId: str = Field(...)
    advancedName: str = Field(...)
    criticalCategory: List[str] = []

    class Config:
        json_encoders = {ObjectId: str}


class ServerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    serverId: str = Field(...)
    serverName: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class SkillSearch(BaseModel):
    jobId: str
    jobGrowId: str


class SkillSearchDetail(BaseModel):
    jobId: str
    skillId: str
