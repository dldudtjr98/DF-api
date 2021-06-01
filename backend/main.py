from fastapi import FastAPI, status
from api.api import api_router


app = FastAPI()


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def index():
    return {"message": "I'm health"}


app.include_router(api_router, prefix='')
