import json
from molotov import scenario


@scenario(5)
async def scenario_one(session):
    async with session.get("http://localhost:5000/api") as res:
        assert res.status == 200
        d = await res.json()
        assert d["Hello"] == "World!"
    

@scenario(30)
async def scenario_two(session):
    somedata = json.dumps({"OK": 1})
    async with session.post("http://localhost:5000/api", data=somedata) as res:
        assert res.status_code == 405


# molotov .\chapter03\molotov_test.py -w 10 -d 30
