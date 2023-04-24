from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request
from aiohttp.web_response import json_response


from . import routes
from main import bot
from aiogram.utils.web_app import check_webapp_signature, safe_parse_webapp_init_data


@routes.get('/hey')
async def hello(request: Request):
    print("Hey")