# Dungeon & Fighter 크리티컬 계산기

캐릭터의 크리티컬을 계산합니다.



## TODO list

- [x] 액티브 스킬에 의한 크리티컬 계산

- [ ] 장비에 의한 크리티컬 계산  

- [x] 스위칭 장비에 의한 크리티컬 계산

- [x] 패시브 스킬에 의한 크리티컬 계산

  

## How to build

- docker-compose up -d --build

- [127.0.0.1:16000/docs](127.0.0.1:16000/docs) : swagger

- POST /server and POST /job to mongoDB initialize
  

## endpoints

- GET /search : 캐릭터 검색 크리티컬을 함께 검색하고 상세검색이 되지않은 캐릭터들은 null, 상세검색이 된 캐릭터들은 가장 마지막 검색된 크리티컬을 표시
- GET /search/detail : 캐릭터 상세검색 및 캐릭터 크리티컬 업데이트


## Test

```
GET /search HTTP/1.1
Content-Type: application/json 
{
  "name": "zer.ostone"
} 
```

>crit : 0

```
GET /search/detail HTTP/1.1
Content-Type: application/json 
{
  "serverId": "cain",
  "characterId": "36c2e00d244e9ae89ad41d2ffe772858"
}
```

>crit calculated

```
GET /search HTTP/1.1
Content-Type: application/json 
{
  "name": "zer.ostone"
} 
```

>crit : 96



