from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.default_menu import get_button, main_menu
from loader import dp, db
from states.register_state import Register


@dp.message_handler(CommandStart())
async def bot_start(msg: Message):
    await db.insert_user(msg.chat.id)
    btn = await get_button()
    user_status = await db.user_info(msg.chat.id)
    if user_status:
        await msg.answer("Asosiy menu:", reply_markup=main_menu)
    else:

        await msg.answer(
            f"Assalom Alaykum, {msg.from_user.full_name}! Taqvimim Bot'ga Xush kelibsiz. \n\nBotingizdan to'liq foydalanish uchun Yashash hududingizni tanlang. ",
            reply_markup=btn)
        await Register.location.set()


@dp.message_handler(regexp="◀️ Bosh menyuga")
async def back_menu(msg: Message):
    await msg.answer("Asosiy menu:", reply_markup=main_menu)

@dp.message_handler(state=Register.location)
async def end_register(msg: Message, state: FSMContext):
    location = msg.text
    chat_id = msg.from_user.id
    await db.update_user(location, chat_id)
    await state.finish()
    await msg.answer("Asosiy menu:", reply_markup=main_menu)
