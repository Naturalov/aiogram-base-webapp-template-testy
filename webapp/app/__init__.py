from aiohttp import web
routes = web.RouteTableDef()

from .send_files import routes
