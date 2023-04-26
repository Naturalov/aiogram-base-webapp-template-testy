import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import User
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp.web import run_app
from aiogram.webhook.aiohttp_server import setup_application

import betterlogging as bl

from tortoise import Tortoise

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from commands import set_bot_commands
from config_reader import config, Settings

# Создаем экземпляр бота.
storage = MemoryStorage()
bot = Bot(token=config.bot_token, parse_mode="HTML")
dp = Dispatcher(storage=storage)
dp["config"] = config

# Создаем экземпляр таймера по Московскому времени.
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

# Загружаем логгер.
logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
logging.basicConfig(
    level=log_level,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
logging.getLogger('aiogram.event').setLevel(logging.WARNING)
logging.getLogger('aiohttp.access').setLevel(logging.INFO)


async def on_startup(app):
    await bot.set_webhook(f"{config.base_url}/webhook")
    webhook = await bot.get_webhook_info()
    logging.info(f"Configured webhook {webhook.url} on ip {webhook.ip_address}")
    user: User = await bot.me()
    logging.info(
        "Run server for bot @%s id=%d - %r", user.username, bot.id, user.full_name
    )
    # Регистрация /-команд в интерфейсе.
    await set_bot_commands(bot)

    await Tortoise.init({
        'connections': {
            'default': config.database_dns
        },
        "apps": {
            "models": {
                "models": ["models"],
                "default_connection": "default",
            },
        },
    })
    await Tortoise.generate_schemas()

async def on_shutdown(app):
    await Tortoise.close_connections()
    await bot.delete_webhook()
    await bot.close()
    logging.info(
        "Good bye"
    )



def main():
    from tgbot import dp
    from webapp import app
    from aiohttp import web
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
