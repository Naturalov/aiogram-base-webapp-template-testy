from aiohttp.web_request import Request

from aiohttp import web


from . import routes


import pathlib


@routes.get('/')
async def index(request: Request):
    file_path = pathlib.Path(__file__).parent / "../template/demo.html"
    return web.FileResponse(file_path)

# @routes.static('/')
# async def static(request: Request):
#     file_path = pathlib.Path(__file__).parent / "../react_build" / request.match_info['filename']
#     return web.FileResponse(file_path)
