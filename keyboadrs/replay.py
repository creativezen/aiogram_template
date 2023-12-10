from aiogram.types import (
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Смайлики"), KeyboardButton(text="Ссылки")],
        [KeyboardButton(text="Калькулятор"), KeyboardButton(text="Спец. кнопки")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True,
)


specials = ReplyKeyboardMarkup(
    keyboard=[
        [
            # отправка карточки контакта
            KeyboardButton(text="Отправить контакт", request_contact=True),
            # создание викторины или голосования
            KeyboardButton(text="Создать голосование", request_poll=KeyboardButtonPollType()),
        ],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True,
)

remove_keyboard = ReplyKeyboardRemove()
