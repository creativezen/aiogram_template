from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ссылка 01", url="yandex.ru")],
        [InlineKeyboardButton(text="Ссылка 02", url="yandex.ru")],
        [InlineKeyboardButton(text="Ссылка 03", url="yandex.ru")],
    ]
)
