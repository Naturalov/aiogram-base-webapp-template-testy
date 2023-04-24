from aiohttp import web
api_app = web.Application()

from .v1 import apiv1_app

api_app.add_subapp("/v1", apiv1_app)
