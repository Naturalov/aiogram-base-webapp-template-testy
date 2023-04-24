from aiohttp import web
apiv1_app = web.Application()

from .user import routes as user_routes

apiv1_app.add_routes(user_routes)