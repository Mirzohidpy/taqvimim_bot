from aiogram.types import Message

from keyboards.default.default_menu import duolar_btn
from loader import dp, bot


@dp.message_handler(text="🤲 Duolar")
async def duo_sender(msg: Message):
    await msg.answer("Saxarlik va Iftorlik duolari", reply_markup=duolar_btn)


@dp.message_handler(text="Saharlik")
async def duo_sender(msg: Message):
    await bot.send_audio(msg.from_user.id, open("audios/SAXARLIK.mp3", "rb"), caption="""
            َوَيْتُ أَنْ أَصُومَ صَوْمَ شَهْرَ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ، خَالِصًا لِلهِ تَعَالَى أَللهُ أَكْبَرُ

    <b>Navaytu an asuvma sovma shahro ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta'aalaa, Allohu akbar.</b> \n\nMa'nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.
            \n<i>🌙 @Taqvimim_bot</i>""")


@dp.message_handler(text="Iftorlik")
async def duo_sender(msg: Message):
    await bot.send_audio(msg.from_user.id, open("audios/IFTORLIK.mp3", "rb"), caption="""
            اَللَّهُمَّ لَكَ صُمْتُ وَ بِكَ آمَنْتُ وَ عَلَيْكَ تَوَكَّلْتُ وَ عَلَى رِزْقِكَ أَفْتَرْتُ، فَغْفِرْلِى مَا قَدَّمْتُ وَ مَا أَخَّرْتُ بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِينَ

    <b>Allohumma laka sumtu va bika amantu va a'alayka tavakkaltu va 'ala rizqika aftartu, fag‘firli, ya G‘offaru, ma qoddamtu vama axxortu.</b> \n\nMa'nosi: Ey Alloh, ushbu ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil!
            \n<i>🌙 @Taqvimim_bot</i>""")
