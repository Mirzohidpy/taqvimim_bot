import json

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import djson


async def get_button():
    btn = ReplyKeyboardMarkup(row_width=2)
    for i in djson:
        btn.insert(i)

    return btn


main_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🗓 Taqvim"),
        KeyboardButton(text="🤲 Duolar")
    ],
    [
        KeyboardButton(text="📍 Joylashuvni o'zgaritirish")
    ]
], resize_keyboard=True)

taqvim_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Bugungi"),
        KeyboardButton(text="Ertangi")
    ],
    [
        KeyboardButton(text="📅 Oylik taqvim")
    ],
    [
        KeyboardButton(text="◀️ Bosh menyuga")
    ]
], resize_keyboard=True)

duolar_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Saharlik"),
        KeyboardButton(text="Iftorlik")
    ],
    [
        KeyboardButton(text="◀️ Bosh menyuga")
    ]
], resize_keyboard=True)
