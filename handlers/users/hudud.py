from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.default_menu import main_menu, get_button
from loader import dp, db, bot
from states.register_state import Location


@dp.message_handler(regexp="📍 Joylashuvni o'zgaritirish")
async def change_location(msg: Message):
    btn = await get_button()
    await msg.answer(
        f"Assalom Alaykum, {msg.from_user.full_name}! \n\nYashash hududingizni tanlang. ",
        reply_markup=btn)
    await Location.location.set()


@dp.message_handler(content_types="text", state=Location.location)
async def end_register(msg: Message, state: FSMContext):
    location = msg.text
    chat_id = msg.from_user.id
    await db.update_user(location, chat_id)
    await state.finish()
    await msg.answer(f"Sizning hududingiz {location}ga o'zgartirildi:", reply_markup=main_menu)
