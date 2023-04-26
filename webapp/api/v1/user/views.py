from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from . import routes
from main import bot
from aiogram.utils.web_app import check_webapp_signature, safe_parse_webapp_init_data


@routes.post('/checkdata')
async def hello(request: Request):
    data = await request.post()
    if check_webapp_signature(bot.token, data["_auth"]):
        return json_response({"ok": True})
    return json_response({"ok": False, "err": "Unauthorized"}, status=401)
