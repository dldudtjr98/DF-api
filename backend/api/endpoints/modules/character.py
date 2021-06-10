from core.config import settings
from modules import make_api_url, request_to_api_server


async def search_basic_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}')
    data = await request_to_api_server(url)
    return data


async def search_equip_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/equip/equipment')
    data = await request_to_api_server(url)
    return data


async def search_skill_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/skill/style')
    data = await request_to_api_server(url)
    return data


async def search_skill_detail_info(job_id, skill_id):
    url = make_api_url(f'skills/{job_id}/{skill_id}')
    data = await request_to_api_server(url)
    return data


async def job_info():
    url = make_api_url('jobs')
    data = await request_to_api_server(url)
    return data


async def search_status_info(server, char_id):
    url = make_api_url(f'servers/{server}/characters/{char_id}/status')
    data = await request_to_api_server(url)
    return data


async def search_skill_enforce_info(server, char_id, category):
    url = make_api_url(f'servers/{server}/characters/{char_id}/skill/buff/equip/{category}')
    data = await request_to_api_server(url)
    return data


def get_character_critical_skill(baseId, advancedId):
    for skill in settings.CRIT_SKILL_ACTIVE:
        if skill["jobId"]["baseId"] == baseId and skill["jobId"]["advancedId"] == advancedId:
            return skill["skillId"]
    return None


def calc_skill_critical(crit_skill, skill_id, buff_skill_lv):
    initial_lv_crit = crit_skill[skill_id][0]
    increase_per_lv_crit = crit_skill[skill_id][1]
    add_critical = initial_lv_crit + increase_per_lv_crit * (buff_skill_lv - 1)
    return add_critical


def calc_all_skill_critical(crit_skill, buff_skill, skill_data):
    buff_skill_critical = 0
    normal_skill_active_critical = 0
    normal_skill_passive_critical = 0
    if crit_skill:
        for skill_id in crit_skill.keys():
            if buff_skill["skillId"] == skill_id:
                buff_skill_critical = calc_skill_critical(crit_skill, skill_id, buff_skill["option"]["level"])
            else:
                for active in skill_data["skill"]["style"]["active"]:
                    if active["skillId"] == skill_id:
                        normal_skill_active_critical = calc_skill_critical(crit_skill, skill_id, active["level"])
                for passive in skill_data["skill"]["style"]["passive"]:
                    if passive["skillId"] == skill_id:
                        normal_skill_passive_critical = calc_skill_critical(crit_skill, skill_id, active["level"])
    add_critical = buff_skill_critical + normal_skill_active_critical + normal_skill_passive_critical
    return add_critical


async def get_crit(job, request):
    status_data = await search_status_info(request.serverId, request.characterId)
    try:
        myjob = await job.find_one(
            {"baseId": status_data["jobId"], "advancedId": status_data["jobGrowId"]},
            {"criticalCategory": 1}
        )
    except TypeError as e:
        print(e)
    physic = [status for status in status_data["status"] if status["name"] == "물리 크리티컬"][0]["value"]
    magic = [status for status in status_data["status"] if status["name"] == "마법 크리티컬"][0]["value"]

    if len(myjob["criticalCategory"]) == 1:
        if myjob["criticalCategory"][0] == "physic":
            return physic
        else:
            return magic
    else:
        return max(physic, magic)
