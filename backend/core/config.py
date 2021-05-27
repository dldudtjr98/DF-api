import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    LOCAL: bool = os.getenv("LOCAL", True)
    DB_USERNAME: str = os.getenv("DB_USERNAME", "pondun")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "pondun")
    DB_HOST: str = os.getenv("DB_HOST", "psqldb:55432")
    DB_NAME: str = os.getenv("DB_NAME", "pondun")
    DF_API_KEY: str = os.getenv("DF_API_KEY", "DIId8NJ7XqzbmQ1v40BVZA2rNxQmiJr5")
    DF_API_SERVER: str = os.getenv("DF_API_SERVER", "https://api.neople.co.kr/df/")
    DF_IMG_SERVER: str = os.getenv("DF_IMG_SERVER", "https://img-api.neople.co.kr/df/")
    MAX_LEV: int = 100
    CRIT_ACTIVE: list = ["92360eab6e1f378902018eca681ac629"]


settings = Settings()
