from fastapi.encoders import jsonable_encoder
from core.config import settings


async def insert_data(table, base_job, final):
    insert_data = {}
    insert_data["criticalCategory"] = []
    insert_data["baseId"] = base_job["jobId"]
    insert_data["baseName"] = base_job["jobName"]
    insert_data["advancedId"] = final["jobGrowId"]
    insert_data["advancedName"] = final["jobGrowName"]

    for job in settings.CRIT_CATEGORY_PHYSIC:
        if job["baseId"] == base_job["jobId"] and insert_data["advancedId"] in job["advancedId"]:
            insert_data["criticalCategory"].append("physic")
    for job in settings.CRIT_CATEGORY_MAGIC:
        if job["baseId"] == base_job["jobId"] and insert_data["advancedId"] in job["advancedId"]:
            insert_data["criticalCategory"].append("magic")
    print(insert_data)

    data = jsonable_encoder(insert_data)
    doc_key = await table.find_one({"baseId": data["baseId"], "advancedId": data["advancedId"]})
    if doc_key is None:
        await table.insert_one(data)
