import json

from aiogram import executor
from handlers.users.iftorlik_notify import notify_sender
import logging

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    # Database ishlatish
    await db.conf()

    # user table yaratadi
    await db.create_table_users()

    await notify_sender('msg')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
