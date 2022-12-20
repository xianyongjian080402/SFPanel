# coding=utf-8
import asyncio
from Log import Log
import json as json_y

from sanic import Sanic
from sanic.response import json

app = Sanic("SFPanel_Back")

@app.route("/")
async def test(request):
    return json({"hello": "world"})
async def Start():
    Log.INFO('后端启动成功')

app.add_task(Start())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000)
