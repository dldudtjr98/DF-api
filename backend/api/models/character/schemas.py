import datetime
from typing import Optional

from pydantic import BaseModel


class CharacterBase(BaseModel):
    last_update: datetime.datetime
