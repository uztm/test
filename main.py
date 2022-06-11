from email import message
import logging
from unittest import skip
from aiogram import  Dispatcher, Bot , executor, types
from aiogram.types import CallbackQuery, Message
# from telegram import InputFile

import markups as nav
import dbText as tex
import cafeArena
import maps as mp
import mapru as mpru
import mapeng as mpeng
import relaxDacha as relax

from languages import lang
from markups import inkey
import sosbank as sos


bot = Bot(token='5581912464:AAE_TEA3VFpUFF6ZOOGx9iqe28pInueeGjs')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)
 

# Uzbek tili

@dp.callback_query_handler(text='uz')
async def leng_uz(call: CallbackQuery):
    text = "Siz O‘zbek tilini muvaffaqiyatli tanladingiz!🇺🇿"
    await call.message.answer(text, reply_markup=nav.mainMenu)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.message_handler()
async def leng_u(message: Message):
    if message.text == "Tilni O'zgartirish🇺🇿":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == "Изменить Язык🇷🇺":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == "Change Language🇺🇸":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == 'Xonobod 🏛':
      await message.answer("Xonobod Tarixi 🏛", reply_markup=inkey)
    
    if message.text == 'Masjidlar 🕌':
      await message.answer("Masjidlar 🕌", reply_markup=nav.MasjidlarIn)

    if message.text == 'Kafelar 🍽':
      await message.answer("Kafelar 🍽", reply_markup=cafeArena.cafeUz)

    if message.text == 'Foodbol Arenalar ⚽️':
      await message.answer("Foodbol Arenalar ⚽️", reply_markup=cafeArena.arenaUz)

    if message.text == 'Dachalar 🏕':
      await message.answer("Dachalar 🏕", reply_markup=relax.dachaUz)
    
    if message.text == 'Dam olish maskanlari 🏖':
      await message.answer("Dam olish maskanlari 🏖", reply_markup=relax.relaxUz)
    
    if message.text == 'Mehmonhonalar 🛎':
      await message.answer("Mehmonhonalar 🛎", reply_markup=relax.hotel)
    
    

    # ru
    if message.text == 'Мечети 🕌':
      await message.answer("Мечети 🕌", reply_markup=nav.MasjidlarInRu)

    if message.text == 'Кафе 🍽':
      await message.answer("Кафе 🍽", reply_markup=cafeArena.cafeRu)

    if message.text == 'Футбольные Арены ⚽️':
      await message.answer("Футбольные Арены ⚽️", reply_markup=cafeArena.arenaRu)

    if message.text == 'Дачи 🏕':
      await message.answer("Дачи 🏕", reply_markup=relax.dachaRu)

    if message.text == 'Зоны отдыха 🏖':
      await message.answer("Зоны отдыха 🏖", reply_markup=relax.relaxRu)
    
    if message.text == 'Ханабад 🏛':
      await message.answer("Ханабад 🏛", reply_markup=nav.xonobodRu)
    
    if message.text == 'Отели 🛎':
      await message.answer("Отели 🛎", reply_markup=relax.hotelRu)

    # eng
    if message.text == 'Mosques 🕌':
      await message.answer("Mosques 🕌", reply_markup=nav.MasjidlarInEng)
    
    if message.text == 'Cafe 🍽':
      await message.answer("Cafe 🍽", reply_markup=cafeArena.cafeEng)

    if message.text == 'Football Arenas ⚽️':
      await message.answer("Football Arenas ⚽️", reply_markup=cafeArena.arenaEng)

    if message.text == 'Dachas 🏕':
      await message.answer("Dachas 🏕", reply_markup=relax.dachaEng)

    if message.text == 'Recreation areas 🏖':
      await message.answer("Recreation areas 🏖", reply_markup=relax.relaxEng)

    if message.text == 'Khonobod 🏛':
      await message.answer("Khonobod 🏛", reply_markup=nav.XonobodEng)

    if message.text == 'Hotels 🛎':
      await message.answer("Hotels 🛎", reply_markup=relax.hotelEng)
    
    # end

    if message.text == 'Bank 🏦':
      await message.answer("Bank 🏦", reply_markup=sos.bank)
    if message.text == 'Банк 🏦':
      await message.answer("Банк 🏦", reply_markup=sos.bankru)
    if message.text == 'Banks 🏦':
      await message.answer("Banks 🏦", reply_markup=sos.bankEng)

    if message.text == 'Favqulodda qo"ng"iroq 🆘':
      await message.answer("Favqulodda qo'ng'iroq 🆘", reply_markup=sos.sos)
    if message.text == 'Экстренный вызов 🆘':
      await message.answer("Экстренный вызов 🆘", reply_markup=sos.sosru)
    if message.text == 'SOS 🆘':
      await message.answer("SOS 🆘", reply_markup=sos.sosEng)
    

# 
@dp.callback_query_handler(text="Hokim")
async def leng_uz(call: CallbackQuery):
    # dir2 = 'images\Sihatgoh.png'
    # with open(dir2, 'rb') as pic2:
    #     await bot.send_photo(call.message.chat.id, pic2, caption='XXXXXX', reply_markup=mp.hokimiyat)
    await bot.send_photo(call.message.chat.id, photo='https://cdn3.vectorstock.com/i/1000x1000/96/47/error-pixel-glitch-vector-20409647.jpg',caption='HOKIMIYAT 🏛 \n\n ☎️: +998-74-734-44-41 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.hokimiyat)
    # test = 'ссылка'
    #     await bot.send_photo(message.chat.id, test)
    # await bot.send_photo(call.message.chat.id, photo=photo, caption='HOKIMIYAT 🏛 \n\n ☎️: +998-74-734-44-41 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.hokimiyat)
    # await message.answer_photo('https://github.com/uztm/new1/blob/main/images/Hokim.jpg')

@dp.callback_query_handler(text="Markaz")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='Shahr Markazi 🏙 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.markaz)

@dp.callback_query_handler(text="Vokzal")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Vokzal 🚉 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.vogzal)

@dp.callback_query_handler(text="Bozor")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='Markaziy Dexqon Bozori 🏪 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.bozor)

@dp.callback_query_handler(text="Makro")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='O"zbegim trade Center 🏪 \n\n ☎️: +998-94-901-00-42 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.makro)

@dp.callback_query_handler(text="Xontog")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Xontog ⛰ \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.xontog)

@dp.callback_query_handler(text="Oyingox")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Bolalar o‘yingoxi ⛹️ \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.oyingoh)

@dp.callback_query_handler(text="Muzey")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Abdulhay xalq amaliy sanat tarixi S.Mehmonov uy muzeyi 🏤 \n\n ☎️: +998-93-414-76-28 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.muzey)

# sherdor
@dp.callback_query_handler(text="Sherdor")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sherdor.jpg', 'rb'), caption='Sherdor Uy Mehmonxonasi 🛎 \n\n ☎️: +998-93-213-35-02 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.sherdor)

@dp.callback_query_handler(text="Sherdorru")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sherdor.jpg', 'rb'), caption='Хаус Отель Шердор 🛎 \n\n ☎️: +998-+998-93-213-35-02 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.sherdor)

@dp.callback_query_handler(text="Sherdoren")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sherdor.jpg', 'rb'), caption='Sherdor House Hotel 🛎 \n\n ☎️: +998-+998-93-213-35-02 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.sherdor)


# sihatgoh

@dp.callback_query_handler(text="Xonobod Sihatgohi 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sihatgoh.png', 'rb'), caption='Xonobod Sihatgohi 🏖 \n\n ☎️: +998-78-150-86-86 \n\n +998-97-582-71-00 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.sihatgoh)

@dp.callback_query_handler(text="Санатория Ханабада 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sihatgoh.png', 'rb'), caption='Санатория Ханабада 🏖 \n\n ☎️: +998-78-150-86-86 \n\n +998-97-582-71-00 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.sihatgoh)

@dp.callback_query_handler(text="Sanatorium Khanabad 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sihatgoh.png', 'rb'), caption='Sanatorium Khanabad 🏖 \n\n ☎️: +998-78-150-86-86 \n\n +998-97-582-71-00 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.sihatgoh)

# masjid

@dp.callback_query_handler(text='Xonobod jome masjidi🕌')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption=tex.tJome, reply_markup=mp.Jome)

@dp.callback_query_handler(text='Tapalina masjidi🕌')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption=tex.tTapolino, reply_markup=mp.MasjidTop)

# choyhonalar
@dp.callback_query_handler(text='Shams choyxona 🍽')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Shams choyxona 🍽 \n\n ☎️: +998-93-177-88-33 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ShamsMap)

@dp.callback_query_handler(text="O'tov choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='Altin Orda Qirg"iz milliy dam olish maskani \n\n ☎️:+998-99-909-00-28 \n\n 📍Manzilni bilish uchun ushbu tigmaga bosing 👇', reply_markup=mp.otovMap)

@dp.callback_query_handler(text="Ulfatlar choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Ulfatlar choyxona 🍽 \n\n ☎️: +998-93-691-55-00 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ulfatlarMap)

@dp.callback_query_handler(text="Afsona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Afsona 🍽 \n\n ☎️: +998-93-249-01-00 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.afsonaMap)

@dp.callback_query_handler(text="Bexruz choyxonasi 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bexruz choyxonasi 🍽 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.BexruzMap)

@dp.callback_query_handler(text="Majnuntol choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Majnuntol choyxona 🍽 \n\n ☎️: +998-97-472-98-55 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.MajnuntolMap)

@dp.callback_query_handler(text="Oqshom Kafe 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Oqshom Kafe 🍽 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.oqshomMap)

@dp.callback_query_handler(text="Arslon meros 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Arslon meros 🍽 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.arislonMap)

@dp.callback_query_handler(text="Bek oshxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bek oshxona 🍽 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.bekMap)

@dp.callback_query_handler(text="Lazzat oshxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Lazzat oshxona 🍽 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.lazzatMap)

@dp.callback_query_handler(text="Daxshad choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Daxshad choyxona 🍽\n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.daxshatMap)


# arenalar

@dp.callback_query_handler(text="Bek Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Bek Arena ⚽️ \n\n ☎️: +998-99-327-11-01 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.arenaBek)

@dp.callback_query_handler(text="Dilkush Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Dilkush Arena ⚽️ \n\n ☎️: +998-93-245-80-00 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.arenaDilkush)

@dp.callback_query_handler(text="Bosm Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Bosm Arena ⚽️ \n\n ☎️: +998-99-810-54-59 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.arenaBosm)

@dp.callback_query_handler(text="Football Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Football Arena ⚽️ \n\n ☎️: +998-99-474-26-19 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.arenaFootbal)

# dachalar

@dp.callback_query_handler(text="Dacha 10 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dacha 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.dachaOn)

@dp.callback_query_handler(text="XonDacha 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='XonDacha 🏕 \n\n ☎️: +998-93-410-00-41 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.xonDacha)

@dp.callback_query_handler(text="Uy Mehmonxona 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Uy Mehmonxona 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.hotelHouse)

@dp.callback_query_handler(text="Dachalar 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dachalar 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.dachalar)

@dp.callback_query_handler(text="Mehmonxona 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Mehmonxona 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.mehmonxona)

@dp.callback_query_handler(text="Labi Anhor 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Labi Anhor 🏕 \n\n ☎️: +998-94-632-74-39 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.labiAn)

# damOlish zonalar

@dp.callback_query_handler(text="Fozilmon Ota 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Fozilmon Ota Ziyoratgoh 🏖 \n\n ☎️: +998-99-315-00-66 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.fozilmon)

@dp.callback_query_handler(text="Kepmin 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Kepming 🏖 \n\n ☎️: +998-99-798-45-61 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.kepmin)

@dp.callback_query_handler(text="Oilaviy Dam Olish Maskani 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Oilaviy Dam Olish Maskani 🏖 \n\n ☎️: +998-93-251- \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.oilaviy)

@dp.callback_query_handler(text="Olovuddin Lager 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Olovuddin Lager 🏖 \n\n ☎️: +998-99-974-20-44 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.oloviddin)

@dp.callback_query_handler(text="Andijon Soy 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Andijon Soy 🏖  \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.soy)


# Русский язык bot.send_photo(c.chat_id, )

@dp.callback_query_handler(text='ru')
async def leng_ru(call: CallbackQuery):
    text = "Вы успешно выбрали РУССКИЙ язык!🇷🇺"
    await call.message.answer(text, reply_markup=nav.mainMenuRu)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

# @dp.message_handler()
# async def leng_ru(message: Message):
#     if message.text == 'Xonobod 🏛':
#       await message.answer("Xonobod Tarixi 🏛", reply_markup=inkey2)


# мечеты

@dp.callback_query_handler(text='Мечеть Джоме Ханабада🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption='Мечеть Джоме Ханабада🕌 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.Jome)

@dp.callback_query_handler(text='Мечеть Топалины🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption='Мечеть Абдулхамида Кори🕌 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.MasjidTop)

# кафе

@dp.callback_query_handler(text='Чайхана Шамс 🍽')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Чайхана Шамс 🍽 \n\n ☎️: +998-93-177-88-33 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.ShamsMap)

@dp.callback_query_handler(text="Чайхана Отов 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='Кыргызский национальное место отдыха Алтын Орда \n\n ☎️:+998-99-909-00-28 \n\n 📍Нажмите на эту кнопку, чтобы узнать местоположение 👇', reply_markup=mpru.otovMap)

@dp.callback_query_handler(text="Чайхана Ульфатлар 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Ульфатлар 🍽 \n\n ☎️: +998-93-691-55-00 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.ulfatlarMap)

@dp.callback_query_handler(text="Афсона 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Афсона 🍽 \n\n ☎️: +998-93-249-01-00 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.afsonaMap)

@dp.callback_query_handler(text="Чайхана Бехруз 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Бехруз 🍽 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.BexruzMap)

@dp.callback_query_handler(text="Чайхана Майнунтол 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Майнунтол 🍽 \n\n ☎️: +998-97-472-98-55 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.MajnuntolMap)

@dp.callback_query_handler(text="Окшом Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Окшом Кафе 🍽 \n\n 📍Нажмите на эту кнопку, чтобы узнать местоположение 👇', reply_markup=mpru.oqshomMap)

@dp.callback_query_handler(text="Арслон мерос 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Арслон мерос 🍽 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.arislonMap)

@dp.callback_query_handler(text="Бек Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Бек Кафе 🍽  \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.bekMap)

@dp.callback_query_handler(text="Лаззат Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Лаззат Кафе 🍽 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.lazzatMap)

@dp.callback_query_handler(text="Чайхана Дахшад 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Дахшад 🍽 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.daxshatMap)


# football arena ru

@dp.callback_query_handler(text="Арена Бек ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Бек ⚽️ \n\n ☎️: +998-99-327-11-01 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.arenaBek)

@dp.callback_query_handler(text="Арена Дилкуш ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Дилкуш ⚽️ \n\n ☎️: +998-93-245-80-00 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.arenaDilkush)

@dp.callback_query_handler(text="Арена Босм ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Босм ⚽️ \n\n ☎️: +998-99-810-54-59 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.arenaBosm)

@dp.callback_query_handler(text="Арена Фудбол ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Фудбол ⚽️ \n\n ☎️: +998-99-474-26-19 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.arenaFootbal)

# дачи

@dp.callback_query_handler(text="Дача 10 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Дача 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.dachaOn)

@dp.callback_query_handler(text="ХанДача 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='ХанДача 🏕 \n\n ☎️: +998-93-410-00-41 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.xonDacha)

@dp.callback_query_handler(text="Хоум Отель 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Хоум Отель 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.hotelHouse)

@dp.callback_query_handler(text="Дачи 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Дачи 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.dachalar)

@dp.callback_query_handler(text="Отель 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Отель 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.mehmonxona)

@dp.callback_query_handler(text="Лаби Анхор 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Лаби Анхор 🏕 \n\n ☎️: +998-93-632-74-39 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.labiAn)


# RELAX RU

@dp.callback_query_handler(text="Фазилмон Ота 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Фазилмон Ота 🏖 \n\n ☎️: +998-99-315-00-66 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.fozilmon)

@dp.callback_query_handler(text="Кепмин 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Кемпинг 🏖 \n\n ☎️: +998-99-798-45-61 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.kepmin)

@dp.callback_query_handler(text="Семейный курорт 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Семейный курорт 🏖 \n\n ☎️: +998- \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.oilaviy)

@dp.callback_query_handler(text="Оловуддин Лагер 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Оловуддин Лагер 🏖 \n\n ☎️: +998-99-974-20-44 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.oloviddin)

@dp.callback_query_handler(text="Андижан Сой 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Андижан Сой 🏖 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.soy)


# ханабад 

@dp.callback_query_handler(text="ПРАВИТЕЛЬСТВО")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hokim.jpg', 'rb'), caption='ПРАВИТЕЛЬСТВО 🏛 \n\n ☎️: +998-74-734-44-41 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.hokimiyat)


@dp.callback_query_handler(text="Центр")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='Центр города 🏙 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.markaz)

@dp.callback_query_handler(text="Вогзал")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Вогзал 🚉  \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.vogzal)

@dp.callback_query_handler(text="Городской Рынок 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='Городской Рынок 🏪 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.bozor)

@dp.callback_query_handler(text="Макро 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='Макро 🏪 \n\n ☎️: +998-94-901-00-42 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.makro)

@dp.callback_query_handler(text="Хонтог ⛰")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Хонтог ⛰ \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.xontog)

@dp.callback_query_handler(text="Детская площадка ⛹️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Детская площадка ⛹️\n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.oyingoh)

@dp.callback_query_handler(text="музей")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Дом-музей истории народного творчества Абдулхая 🏤 \n\n ☎️: +998-93-414-76-28 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mpru.muzey)


# English

@dp.callback_query_handler(text='eng')
async def leng_uz(call: CallbackQuery):
    text = "You have successfully chosen the ENGLISH language!🇺🇸"
    await call.message.answer(text, reply_markup=nav.mainMenuEng)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

# musque

@dp.callback_query_handler(text='Jome Mosque Xonobod🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption='Jome Mosque Xonobod🕌 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.Jome)

@dp.callback_query_handler(text='Mosque Topolina🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption='Abdulhamid Qori Mosque🕌 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.MasjidTop)

# cafe eng

@dp.callback_query_handler(text='Teahouse Shams 🍽')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Teahouse Shams 🍽 \n\n ☎️: +998-93-177-88-33 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.ShamsMap)

@dp.callback_query_handler(text="Teahouse Otov 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='Altin Orda is a Kyrgyz national holiday destination \n\n ☎️:+998-99-909-00-28 \n\n 📍Click this button to find out the location 👇', reply_markup=mpeng.otovMap)

@dp.callback_query_handler(text="Teahouse Ulfatlar 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Ulfatlar 🍽 \n\n ☎️: +998-93-691-55-00 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.ulfatlarMap)

@dp.callback_query_handler(text="Afsona 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Afsona 🍽 \n\n ☎️: +998-93-249-01-00 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.afsonaMap)

@dp.callback_query_handler(text="Teahouse Behruz 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Behruz 🍽\n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.BexruzMap)

@dp.callback_query_handler(text="Teahouse Majnuntol 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Majnuntol 🍽 \n\n ☎️: +998-97-472-98-55 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.MajnuntolMap)

@dp.callback_query_handler(text="Okshom Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Okshom Cafe 🍽 \n\n 📍Click this button to find out the location 👇', reply_markup=mpeng.oqshomMap)

@dp.callback_query_handler(text="Arslon Meros 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Arslon Meros 🍽 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.arislonMap)

@dp.callback_query_handler(text="Bek Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bek Cafe 🍽 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.bekMap)

@dp.callback_query_handler(text="Lazzat Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Lazzat Cafe 🍽 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.lazzatMap)

@dp.callback_query_handler(text="Teahouse Dahshad 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Dahshad 🍽 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.daxshatMap)

# arenas eng

@dp.callback_query_handler(text="Arena Bek ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Bek ⚽️ \n\n ☎️: +998-99-327-11-01 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.arenaBek)

@dp.callback_query_handler(text="Arena Dilkush ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Dilkush ⚽️ \n\n ☎️: +998-93-245-80-00 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.arenaDilkush)

@dp.callback_query_handler(text="Arena Bosm ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Bosm ⚽️ \n\n ☎️: +998-99-810-54-59 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.arenaBosm)

@dp.callback_query_handler(text="Arena Football ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Football ⚽️ \n\n ☎️: +998-99-474-26-19 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.arenaFootbal)

# dachas

@dp.callback_query_handler(text="Dacha 10")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dacha 10 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.dachaOn)

@dp.callback_query_handler(text="XonDacha")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='XonDacha 🏕 \n\n ☎️: +998-93-410-00-41 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.xonDacha)

@dp.callback_query_handler(text="Home Hotel 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Home Hotel 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.hotelHouse)

@dp.callback_query_handler(text="Migros 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Migros 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.dachalar)

@dp.callback_query_handler(text="Hotel 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Hotel 🏕 \n\n ☎️: +998-93-427-48-23 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.mehmonxona)

@dp.callback_query_handler(text="Labi Anhor")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Labi Anhor 🏕 \n\n ☎️: +998-93-632-74-39 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.labiAn)

# relax ENG

@dp.callback_query_handler(text="Fazilmon Ota 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Fazilmon Ota 🏖 \n\n ☎️: +998-99-315-00-66 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.fozilmon)

@dp.callback_query_handler(text="Kepmin")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Kepmin 🏖 \n\n ☎️: +998-99-798-45-61 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.kepmin)

@dp.callback_query_handler(text="Family Resort 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Family Resort 🏖 \n\n ☎️: +998-93- \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.oilaviy)

@dp.callback_query_handler(text="Olovuddin Lager")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Lager Olovuddin 🏖 \n\n ☎️: +998-99-974-20-44 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.oloviddin)

@dp.callback_query_handler(text="Andijan Soy")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Andijan Soy 🏖 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.soy)


# Khonobod

@dp.callback_query_handler(text="GOVERNMENT")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hokim.jpg', 'rb'), caption='GOVERNMENT 🏛 \n\n ☎️: +998-74-734-44-41 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.hokimiyat)


@dp.callback_query_handler(text="Center")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='City Center 🏙 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.markaz)

@dp.callback_query_handler(text="Railway")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Railway station 🚉 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.vogzal)

@dp.callback_query_handler(text="Market")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='City Market 🏪 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.bozor)

@dp.callback_query_handler(text="Makro 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='Makro 🏪 \n\n ☎️: +998-94-901-00-42 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.makro)

@dp.callback_query_handler(text="Xontog ⛰")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Xontog ⛰ \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.xontog)

@dp.callback_query_handler(text="Children's playground ⛹️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Children"s playground ⛹️ \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.oyingoh)

@dp.callback_query_handler(text="Museum")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Abdulhay Folk Art History House Museum 🏤 \n\n ☎️: +998-93-414-76-28 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mpeng.muzey)




# anhor choy

@dp.callback_query_handler(text="Anhor choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Anhor choyxonasi 🍽 \n\n ☎️: +998-90-380-88-88 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.anhorChoyxona)

@dp.callback_query_handler(text="Чайхана Анхор 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Анхор 🍽 \n\n ☎️: +998-90-380-88-88 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.anhorChoyxona)

@dp.callback_query_handler(text="Teahouse Anhor 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Anhor 🍽 \n\n ☎️: +998-90-380-88-88 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.anhorChoyxona)

# sos
@dp.callback_query_handler(text="Tez Yordam 🚑")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Tez Tibbiy Yordam 🚑 \n\n ☎️: +998-55-201-75-03 \n☎️:103 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.tezYordam)

@dp.callback_query_handler(text="Скорая помощь 🚑")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Скорая помощь 🚑 \n\n ☎️: +998-55-201-75-03 \n☎️:103 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.tezYordam)

@dp.callback_query_handler(text="Ambulance 🚑")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Ambulance 🚑 \n\n ☎️: +998-55-201-75-03 \n☎️:103 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.tezYordam)

# 

@dp.callback_query_handler(text="IIB 🚓")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Ichki Ishlar Bo"limi 🚓 \n\n ☎️: +998-74-734-40-02 \n☎️:102 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="УВД 🚓")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Министерство Внутренних Дел 🚓 \n\n ☎️: +998-74-734-40-02 \n☎️:102 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="POLICE 🚓")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='POLICE 🚓 \n\n ☎️: +998-74-734-40-02 \n☎️:102 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)

# 

@dp.callback_query_handler(text="FVV 🚒")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Favqulodda Vaziyatlar Vazirligi 🚒 \n\n ☎️: +998-74-734-78-01 \n☎️:101 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="МЧС 🚒")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Министерство Чрезвычайным Ситуациям 🚒 \n\n ☎️: +998-74-734-78-01 \n☎️:101 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="MES 🚒")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Ministry of Emergency Situations 🚒 \n\n ☎️: +998-74-734-78-01 \n☎️:101 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)

# 

@dp.callback_query_handler(text="Milliy Gvardiya 🚔")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Milliy Gvardiya 🚔 \n\n ☎️: +998-74-734-41-40 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="Гвардия 🚔")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Гвардия 🚔 \n\n ☎️: +998-74-734-41-40 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="Guard 🚔")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sos.jpg', 'rb'), caption='Guard 🚔 \n\n ☎️: +998-74-734-41-40 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)


# bank

@dp.callback_query_handler(text="Halqbank 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Halq.jpg', 'rb'), caption='Xalq Banki 🏦 \n\n ☎️: +998-74-734-42-23 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="Народный банк 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Halq.jpg', 'rb'), caption='Народный банк 🏦 \n\n ☎️: +998-74-734-42-23 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="National bank 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Halq.jpg', 'rb'), caption='National bank 🏦 \n\n ☎️: +998-74-734-42-23 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)

# 

@dp.callback_query_handler(text="SQB 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sqb.jpg', 'rb'), caption='Sanoat Qurilish Bank 🏦 \n\n ☎️: +998-94-109-03-09 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="ПСБ 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sqb.jpg', 'rb'), caption='Промстройбанк 🏦 \n\n ☎️: +998-94-109-03-09 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="ICB 🏦")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Sqb.jpg', 'rb'), caption='Industrial Construction Bank 🏦 \n\n ☎️: +998-94-109-03-09 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)

# hunar

@dp.callback_query_handler(text="Hunarmandlar")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hunar.jpg', 'rb'), caption='Hunarmandlar 👨‍🎨 \n\n 📍Ushbu manzilga borish uchun \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="Ремесленники")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hunar.jpg', 'rb'), caption='Ремесленники 👨‍🎨 \n\n 📍Для перехода по этому адресу \n                              👇👇👇', reply_markup=mp.ichkiIsh)

@dp.callback_query_handler(text="Artisans")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hunar.jpg', 'rb'), caption='Artisans 👨‍🎨 \n\n 📍To go to this address \n                              👇👇👇', reply_markup=mp.ichkiIsh)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)