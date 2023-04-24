from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from models import UserModel

import tgbot.keyboards as keyboards

from . import router


@router.message(CommandStart())
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    await message.reply("Вітаю!", reply_markup=await keyboards.test())
