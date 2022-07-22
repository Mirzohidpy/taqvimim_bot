from aiogram.types import Message

from keyboards.default.default_menu import taqvim_menu
from loader import dp, db, bot, djson
from datetime import date, timedelta


@dp.message_handler(text="🗓 Taqvim")
async def taqvim_sender(msg: Message):
    await msg.answer("Kunni tanlang: ", reply_markup=taqvim_menu)


@dp.message_handler(text="Bugungi")
async def today_time(msg: Message):
    chat_id = msg.chat.id
    await db.insert_user(chat_id)
    region = await db.user_info(chat_id)
    month = int(date.today().strftime("%m"))
    day = int(date.today().strftime("%d"))
    today = date.today().strftime("%d.%m.%Y")

    if month == 4:
        fajr = djson[region][str(day - 1)]['fajr']
        maghrib = djson[region][str(day - 1)]['maghrib']
        day_name = djson[region][str(day - 1)]['day_name']
    else:
        fajr = djson[region]['30']['fajr']
        maghrib = djson[region]['30']['maghrib']
        day_name = djson[region]['30']['day_name']
    text = f"<b>Bugun {today} {day_name}</b>\n\n{'=' * 25}\n\n" \
           f"♦️ <b>Saharlik vaqti:</b> {fajr}\n" \
           f"♦️ <b>Iftorlik vaqti:</b> {maghrib}" \
           f"\n\n{'=' * 25}"
    try:
        await bot.send_photo(chat_id, photo=open(f"images/duo.png", 'rb'), caption=f"{text}\n\n<i>🌙 @Taqvimim_bot</i>")
    except Exception as m:
        print(m)


@dp.message_handler(text="Ertangi")
async def today_time(msg: Message):
    chat_id = msg.chat.id
    region = await db.user_info(chat_id)
    month = int(date.today().strftime("%m"))
    day = int(date.today().strftime("%d"))
    today_date = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")

    if month == 4:
        fajr = djson[region][str(day)]['fajr']
        maghrib = djson[region][str(day)]['maghrib']
        day_name = djson[region][str(day)]['day_name']
        text = f"<b>Bugun {today_date} {day_name}</b>\n\n{'=' * 25}\n\n" \
               f"♦️ <b>Saharlik vaqti:</b> {fajr}\n" \
               f"♦️ <b>Iftorlik vaqti:</b> {maghrib}" \
               f"\n\n{'=' * 25}"
        try:
            await bot.send_photo(chat_id, photo=open(f"images/duo.png", 'rb'),
                                 caption=f"{text}\n\n<i>🌙 @Taqvimim_bot</i>")
        except Exception as m:
            print(m)

    else:
        text = "<b>Ramazon Hayiti muborak bo'lsin !!!</b>"

        try:
            await bot.send_photo(chat_id, photo=open(f"images/ramadan.png", 'rb'),
                                 caption=f"{text}\n\n<i>🌙 @Taqvimim_bot</i>")
        except Exception as m:
            print(m)


@dp.message_handler(regexp="📅 Oylik taqvim")
async def send_takvim(msg: Message):
    chat_id = msg.chat.id
    region = await db.user_info(chat_id)
    try:
        await bot.send_photo(chat_id, photo=open(f"images/{region}.png", 'rb'),
                             caption=f"<b>{region}</b> hududi uchun <i>Ramazon taqvimi</i>\n\n<i>🌙 @Taqvimim_bot</i>")
    except Exception as m:
        print(m)
