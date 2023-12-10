from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from filters.admin import isAdmin
from keyboadrs import replay

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}", reply_markup=replay.main
    )
