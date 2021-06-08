import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    LOCAL: bool = os.getenv("LOCAL", True)
    DB_USERNAME: str = os.getenv("DB_USERNAME", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "mongo_root")
    DB_HOST: str = os.getenv("DB_HOST", "mongodb:27017")
    DB_CONNECT_PATH: str = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}"
    DF_API_KEY: str = os.getenv("DF_API_KEY", "DIId8NJ7XqzbmQ1v40BVZA2rNxQmiJr5")
    DF_API_SERVER: str = os.getenv("DF_API_SERVER", "https://api.neople.co.kr/df/")
    DF_IMG_SERVER: str = os.getenv("DF_IMG_SERVER", "https://img-api.neople.co.kr/df/")
    MAX_LEV: int = 100
    CRIT_ACTIVE: list = ["92360eab6e1f378902018eca681ac629"]
    CRIT_CATEGORY_PHYSIC: list = [
        {
            "baseId": "41f1cdc2ff58bb5fdc287be0db2a8df3",  # 귀검사(남)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "92da05ec93fb43406e193ffb9a2a629b",
            ]
        },
        {
            "baseId": "1645c45aabb008c98406b3a16447040d",  # 귀검사(여)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "ca0f0e0e9e1d55b5f9955b03d9dd213c",  # 격투가(남)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "a7a059ebe9e6054c0644b40ef316d6e9",  # 격투가(여)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "afdf3b989339de478e85b614d274d1ef",  # 거너(남)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "944b9aab492c15a8474f96947ceeb9e4",  # 거너(여)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "a5ccbaf5538981c6ef99b236c0a60b73",  # 마법사(남)
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "3909d0b188e9c95311399f776e331da5",  # 마법사(여)
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
            ]
        },
        {
            "baseId": "f6a4ad30555b99b499c07835f87ce522",  # 프리스트(남)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
            ]
        },
        {
            "baseId": "0c1b401bb09241570d364420b3ba3fd7",  # 프리스트(여)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
            ]
        },
        {
            "baseId": "ddc49e9ad1ff72a00b53c6cff5b1e920",  # 도적
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "0ee8fa5dc525c1a1f23fc6911e921e4a",  # 나이트
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "3deb7be5f01953ac8b1ecaa1e25e0420",  # 마창사
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
            ]
        },
        {
            "baseId": "986c2b3d72ee0e4a0b7fcfbe786d4e02",  # 총검사
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
            ]
        },
        {
            "baseId": "17e417b31686389eebff6d754c3401ea",  # 다크나이트
            "advancedId": [
                "0a49d9c8b5e1358efff324e5cb11d41e",
            ]
        }
    ]
    CRIT_CATEGORY_MAGIC: list = [
        {
            "baseId": "41f1cdc2ff58bb5fdc287be0db2a8df3",  # 귀검사(남)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "1645c45aabb008c98406b3a16447040d",  # 귀검사(여)
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
            ]
        },
        {
            "baseId": "ca0f0e0e9e1d55b5f9955b03d9dd213c",  # 격투가(남)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
            ]
        },
        {
            "baseId": "a7a059ebe9e6054c0644b40ef316d6e9",  # 격투가(여)
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
                "37495b941da3b1661bc900e68ef3b2c6",
            ]
        },
        {
            "baseId": "afdf3b989339de478e85b614d274d1ef",  # 거너(남)
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "944b9aab492c15a8474f96947ceeb9e4",  # 거너(여)
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "a5ccbaf5538981c6ef99b236c0a60b73",  # 마법사(남)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
                "92da05ec93fb43406e193ffb9a2a629b",
            ]
        },
        {
            "baseId": "3909d0b188e9c95311399f776e331da5",  # 마법사(여)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
                "92da05ec93fb43406e193ffb9a2a629b",
            ]
        },
        {
            "baseId": "f6a4ad30555b99b499c07835f87ce522",  # 프리스트(남)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "0c1b401bb09241570d364420b3ba3fd7",  # 프리스트(여)
            "advancedId": [
                "37495b941da3b1661bc900e68ef3b2c6",
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3",
            ]
        },
        {
            "baseId": "ddc49e9ad1ff72a00b53c6cff5b1e920",  # 도적
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
                "6d459bc74ba73ee4fe5cdc4655400193",
            ]
        },
        {
            "baseId": "0ee8fa5dc525c1a1f23fc6911e921e4a",  # 나이트
            "advancedId": [
                "618326026de1a1f1cfba5dbd0b8396e7",
            ]
        },
        {
            "baseId": "3deb7be5f01953ac8b1ecaa1e25e0420",  # 마창사
            "advancedId": [
                "6d459bc74ba73ee4fe5cdc4655400193",
                "c9b492038ee3ca8d27d7004cf58d59f3"
            ]
        },
        {
            "baseId": "986c2b3d72ee0e4a0b7fcfbe786d4e02",  # 총검사
            "advancedId": [
                "c9b492038ee3ca8d27d7004cf58d59f3"
            ]
        },
        {
            "baseId": "b522a95d819a5559b775deb9a490e49a",  # 크리에이터
            "advancedId": [
                "0a49d9c8b5e1358efff324e5cb11d41e",
            ]
        }
    ]
    # skill 첫번째 = 1레벨 초기값, 두번째 = *n 크리티컬
    CRIT_SKILL_ACTIVE: list = [
        {
            "jobId": {  # 웨펀마스터
                "baseId": "41f1cdc2ff58bb5fdc287be0db2a8df3",
                "advancedId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "762c4e6d030eaf0abbfe1fec2b298574": [6, 1],  # 오버드라이브
                "5806440d21e7546d50007a5ba11f8024": [5, 1]   # 류심 강
            }
        },
        {
            "jobId": {  # 버서커
                "baseId": "41f1cdc2ff58bb5fdc287be0db2a8df3",
                "advancedId": "6d459bc74ba73ee4fe5cdc4655400193"
            },
            "skillId": {
                "dbf8b30c7057032af0d68fcfa289fdae": [3, 0.6],  # 선혈의 추억
            }
        },
        {
            "jobId": {  # 아수라
                "baseId": "41f1cdc2ff58bb5fdc287be0db2a8df3",
                "advancedId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "d0cdaca82892e54097f22a1f60817048": [10.5, 0.5],  # 살의의 파동
            }
        },
        {
            "jobId": {  # 소드마스터
                "baseId": "1645c45aabb008c98406b3a16447040d",
                "advancedId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "8c2379737c5acc935c1731f67f607655": [2, 2],  # 신검합일
            }
        },
        {
            "jobId": {  # 스트리트파이터 (여)
                "baseId": "a7a059ebe9e6054c0644b40ef316d6e9",
                "advancedId": "6d459bc74ba73ee4fe5cdc4655400193"
            },
            "skillId": {
                "1803b6a67047cafb9e289b4f33cc507b": [10, 2],  # 용독술
            }
        },
        {
            "jobId": {  # 레인저 (남)
                "baseId": "afdf3b989339de478e85b614d274d1ef",
                "advancedId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "b163d099c8cc27fdb6fd3639c2ee6df9": [1.6, 1],  # 죽음의 표식
            }
        },
        {
            "jobId": {  # 런처 (남)
                "baseId": "afdf3b989339de478e85b614d274d1ef",
                "advancedId": "618326026de1a1f1cfba5dbd0b8396e7"
            },
            "skillId": {
                "6e33d47e6622ce03b6defdd912140270": [0.8, 1.6],  # 스펙트럴 서치 아이
            }
        },
        {
            "jobId": {  # 스핏파이어 (남)
                "baseId": "afdf3b989339de478e85b614d274d1ef",
                "advancedId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "c61f5a010370101402b05b21916c2071": [10, 0],  # 섬광류탄
            }
        },
        {
            "jobId": {  # 스핏파이어 (여)
                "baseId": "944b9aab492c15a8474f96947ceeb9e4",
                "advancedId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "c61f5a010370101402b05b21916c2071": [10, 0],  # 섬광류탄
            }
        },
        {
            "jobId": {  # 디멘션워커 (남)
                "baseId": "a5ccbaf5538981c6ef99b236c0a60b73",
                "advancedId": "92da05ec93fb43406e193ffb9a2a629b"
            },
            "skillId": {
                "2a0a39184de92acf1c1375e00b77404c": [10, 0],  # 운명왜곡
            }
        },
        {
            "jobId": {  # 엘레멘탈마스터
                "jobId": "3909d0b188e9c95311399f776e331da5",
                "jobGrowId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "bb34e8854a93fd250347a1c64119f7ab": [30, 2],  # 초월의 룬
            }
        },
        {
            "jobId": {  # 인파이터
                "jobId": "f6a4ad30555b99b499c07835f87ce522",
                "jobGrowId": "618326026de1a1f1cfba5dbd0b8396e7"
            },
            "skillId": {
                "8f73f243041c2d27739fe7696f02bf9b": [1.5, 1.5],  # 윌드라이버
            }
        },
        {
            "jobId": {  # 퇴마사
                "jobId": "f6a4ad30555b99b499c07835f87ce522",
                "jobGrowId": "6d459bc74ba73ee4fe5cdc4655400193"
            },
            "skillId": {
                "f6a4ad30555b99b499c07835f87ce522": [10, 2],  # 신선의 경지
            }
        },
        {
            "jobId": {  # 이단심판관
                "jobId": "0c1b401bb09241570d364420b3ba3fd7",
                "jobGrowId": "618326026de1a1f1cfba5dbd0b8396e7"
            },
            "skillId": {
                "e49e57b2e8fbeceb0a2c56a0c63fe6c5": [1, 1],  # 광적인 믿음
            }
        },
        {
            "jobId": {  # 미스트리스
                "jobId": "0c1b401bb09241570d364420b3ba3fd7",
                "jobGrowId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "852f8ad797db4dca1405cb3e77198401": [13, 0.5],  # 죄를 고하는 자
            }
        },
        {
            "jobId": {  # 로그
                "jobId": "ddc49e9ad1ff72a00b53c6cff5b1e920",
                "jobGrowId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "de3fea2d65c597f4d55c70a02b97fc79": [4, 2],  # 문아크
            }
        },
        {
            "jobId": {  # 로그
                "jobId": "ddc49e9ad1ff72a00b53c6cff5b1e920",
                "jobGrowId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "7f80b887a09e88e2c4728c898bd73654": [10, 1.1],  # 암살자의 마음가짐
            }
        },
        {
            "jobId": {  # 팔라딘
                "jobId": "0ee8fa5dc525c1a1f23fc6911e921e4a",
                "jobGrowId": "6d459bc74ba73ee4fe5cdc4655400193"
            },
            "skillId": {
                "9dc8438e4572d39243c97da31c113acc": [25.5, 0.5],  # 세라픽 페더
            }
        },
        {
            "jobId": {  # 뱅가드
                "jobId": "3deb7be5f01953ac8b1ecaa1e25e0420",
                "jobGrowId": "37495b941da3b1661bc900e68ef3b2c6"
            },
            "skillId": {
                "de3fea2d65c597f4d55c70a02b97fc79": [11, 1],  # 마창 해방
            }
        },
        {
            "jobId": {  # 다크랜서
                "jobId": "3deb7be5f01953ac8b1ecaa1e25e0420",
                "jobGrowId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "fc458e449ee00b01dbf88d09aae65462": [1, 1],  # 다크니스
            }
        },
        {
            "jobId": {  # 패스파인더
                "jobId": "986c2b3d72ee0e4a0b7fcfbe786d4e02",
                "jobGrowId": "c9b492038ee3ca8d27d7004cf58d59f3"
            },
            "skillId": {
                "d53301bb328baf12a3ae482cc6a565dd": [10.5, 0.5],  # 코어 프렉시스
            }
        },
        {
            "jobId": {  # 크리에이터
                "jobId": "b522a95d819a5559b775deb9a490e49a",
                "jobGrowId": "0a49d9c8b5e1358efff324e5cb11d41e"
            },
            "skillId": {
                "2ff50c35efcf0f287c4c418c8454da48": [1, 1],  # 증폭
            }
        }
    ]


settings = Settings()
