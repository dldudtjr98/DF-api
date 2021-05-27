from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

if settings.LOCAL:
    SQLALCHEMY_DATABASE_URL = "postgresql://pondun:pondun@psqldb:55432/pondun"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://bizcowork:bizcowork@5432/uploaddev"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
