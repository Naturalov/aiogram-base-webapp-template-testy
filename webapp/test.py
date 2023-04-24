from aiohttp.web_app import Application
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler

from main import bot, dp
from .api import api_app
from .app import routes

app = Application()
app["bot"] = bot

app.add_subapp("/api", api_app)
app.add_routes(routes)
# Подключение глобального маршрутизатора к приложению

SimpleRequestHandler(
    dispatcher=dp,
    bot=bot,
).register(app, path="/webhook")
