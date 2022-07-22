import logging

from aiogram.types import Message
from loader import dp, db, bot, djson
from datetime import time, date, datetime, timedelta


async def notify_sender(msg: Message):
    list_users = await db.get_users()
    for users in list_users:
        try:
            chat_id = users['user_id']
            region = await db.user_info(chat_id)
            day = int(date.today().strftime("%d"))
            time_now = datetime.now().strftime('%H:%M')

            # fajr = djson[region][str(day - 1)]['fajr']
            fajr = '16:55'
            fajr_time = (datetime.strptime(fajr, '%H:%M') - timedelta(minutes=5)).strftime('%H:%M')

            maghrib = djson[region][str(day - 1)]['maghrib']
            maghrib_time = (datetime.strptime(maghrib, '%H:%M') - timedelta(minutes=5)).strftime('%H:%M')

            if fajr_time == time_now:
                text = f"5 daqiqadan so'ng <b>{fajr}</b> da Saharlik vaqti tugaydi.\n\nOg'izni yopishni unutmang birodar 😊 \n\n<i>🌙 @Taqvimim_bot</i>"
                print("success")
                await bot.send_message(chat_id, text)

            if maghrib_time == time_now:
                text = ""
        except Exception as err:
            logging.exception(err)
