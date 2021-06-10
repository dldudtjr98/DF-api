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
    criticalCategory: List[str] = ["physic", "magic"]

    class Config:
        json_encoders = {ObjectId: str}


class JobResponseModel(BaseModel):
    data: List[JobModel] = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class JobSkillDetailModel(BaseModel):
    skillId: str = Field(...)
    name: str = Field(...)
    requiredLevel: int = Field(...)
    type: str = Field(...)
    costType: str = Field(...)


class JobSkillResponseModel(BaseModel):
    data: List[JobSkillDetailModel] = Field(...)


class ServerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    serverId: str = Field(...)
    serverName: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class ServerResponseModel(BaseModel):
    data: List[ServerModel] = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class SkillSearch(BaseModel):
    jobId: str
    jobGrowId: str


class SkillSearchDetail(BaseModel):
    jobId: str
    skillId: str
