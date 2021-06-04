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
                "37495b941da3b1661bc900e68ef3b2c6",
                "618326026de1a1f1cfba5dbd0b8396e7",
            ]
        },
        {
            "baseId": "986c2b3d72ee0e4a0b7fcfbe786d4e02",  # 총검사
            "advancedId": [
                pass
            ]
        },
        {
            "baseId": "b522a95d819a5559b775deb9a490e49a",  # 크리에이터
            "advancedId": [
                "0a49d9c8b5e1358efff324e5cb11d41e",
            ]
        }
    ]

settings = Settings()
