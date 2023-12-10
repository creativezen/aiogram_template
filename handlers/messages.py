from aiogram import F, Router
from aiogram.types import Message

from keyboadrs import inline, replay

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "ссылки":
        await message.answer("Ссылки:", reply_markup=inline.links)

    if msg == "спец. кнопки":
        await message.answer("Специальные кнопки:", reply_markup=replay.specials)
