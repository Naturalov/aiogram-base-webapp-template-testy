from aiohttp.web_request import Request

from aiohttp import web


from . import routes


import pathlib


@routes.get('/')
async def index(request: Request):
    file_path = pathlib.Path(__file__).parent / "../static/index.html"
    return web.FileResponse(file_path)

routes.static('/', path = pathlib.Path(__file__).parent / "../static/")
