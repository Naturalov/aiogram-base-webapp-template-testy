from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

from config_reader import config

async def test():
    _ = InlineKeyboardBuilder()
    _.button(text="test1", web_app=WebAppInfo(url=f"{config.base_url}/"))
    return _.as_markup()
