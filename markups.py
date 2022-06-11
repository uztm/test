from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnMain = KeyboardButton('Bosh Sahifa')
# --- change lang ---
btnUz = KeyboardButton("Tilni O'zgartirish🇺🇿")
btnRu = KeyboardButton('Изменить Язык🇷🇺')
btnEng = KeyboardButton('Change Language🇺🇸')

# --- main menu ---
btnXonobod = KeyboardButton('Xonobod 🏛')
btnMasjid = KeyboardButton('Masjidlar 🕌')
btnKafe =  KeyboardButton('Kafelar 🍽')
btnArena = KeyboardButton('Foodbol Arenalar ⚽️')
btnChoyxona = KeyboardButton('Dam olish maskanlari 🏖')
btnDacha = KeyboardButton('Dachalar 🏕')
btnMehmon = KeyboardButton('Mehmonhonalar 🛎')
btnSos = KeyboardButton('Favqulodda qo"ng"iroq 🆘')
btnBank = KeyboardButton('Bank 🏦')

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobod, btnChoyxona, btnKafe,  btnMehmon, btnDacha, btnMasjid, btnBank,btnSos,btnArena, btnUz)
                                                          
# --- manin ru ---
btnXonobodru = KeyboardButton('Ханабад 🏛')
btnMasjidru = KeyboardButton('Мечети 🕌')
btnKaferu =  KeyboardButton('Кафе 🍽')
btnArenaru = KeyboardButton('Футбольные Арены ⚽️')
btnChoyxonaru = KeyboardButton('Зоны отдыха 🏖')
btnDacharu = KeyboardButton('Дачи 🏕')
btnMehmonru = KeyboardButton('Отели 🛎')
btnSosru = KeyboardButton('Экстренный вызов 🆘')
btnBankru = KeyboardButton('Банк 🏦')

mainMenuRu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobodru, btnChoyxonaru, btnKaferu,  btnMehmonru, btnDacharu, btnMasjidru, btnBankru,btnSosru,btnArenaru, btnRu)

# --- main eng ---
btnXonobodEng = KeyboardButton('Khonobod 🏛')
btnMasjidEng = KeyboardButton('Mosques 🕌')
btnKafeEng =  KeyboardButton('Cafe 🍽')
btnArenaEng = KeyboardButton('Football Arenas ⚽️')
btnChoyxonaEng = KeyboardButton('Recreation areas 🏖')
btnDachaEng = KeyboardButton('Dachas 🏕')
btnMehmonEng = KeyboardButton('Hotels 🛎')
btnSosEng = KeyboardButton('SOS 🆘')
btnBankEng = KeyboardButton('Banks 🏦')

mainMenuEng = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobodEng, btnChoyxonaEng, btnKafeEng,  btnMehmonEng, btnDachaEng, btnMasjidEng, btnBankEng,btnSosEng,btnArenaEng, btnEng)



# inline markups

inkey = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="XONOBOD SHAHR HOKIMLIGI 🏛", callback_data="Hokim")
    ],
    [
      InlineKeyboardButton(text="Shahar Markazi 🏙", callback_data="Markaz"),
      InlineKeyboardButton(text="Vokzal 🚉", callback_data="Vokzal")
    ],
    [
      InlineKeyboardButton(text="Markaziy Dexqon Bozori 🏪", callback_data="Bozor")
    ],
    [
      InlineKeyboardButton(text="O'zbegim Trade Center 🏪", callback_data="Makro"),
      InlineKeyboardButton(text="Xontog' ⛰", callback_data="Xontog"),
    ],
    [
      InlineKeyboardButton(text="Bolalar o‘yingoxi ⛹️", callback_data="Oyingox")
    ],
    [
      InlineKeyboardButton(text="Abdulhay xalq amaliy sanat tarixi S.Mehmonov uy muzeyi 🏤", callback_data="Muzey")
    ],
    [
      InlineKeyboardButton(text="Hunarmandlar 👨‍🎨", callback_data="Hunarmandlar")
    ]
  ]
)

xonobodRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="ПРАВИТЕЛЬСТВО ГОРОДА ХАНАБАДА 🏛", callback_data="ПРАВИТЕЛЬСТВО")
    ],
    [
      InlineKeyboardButton(text="Центр города 🏙", callback_data="Центр"),
      InlineKeyboardButton(text="Вокзал 🚉", callback_data="Вогзал")
    ],
    [
      InlineKeyboardButton(text="Городской Рынок 🏪", callback_data="Городской Рынок 🏪")
    ],
    [
      InlineKeyboardButton(text="Торговый Центр Узбеним🏪", callback_data="Макро 🏪"),
      InlineKeyboardButton(text="Хонтог ⛰", callback_data="Хонтог ⛰"),
    ],
    [
      InlineKeyboardButton(text="Детская площадка ⛹️", callback_data="Детская площадка ⛹️")
    ],
    [
      InlineKeyboardButton(text="Дом-музей С.Михманова истории народного творчества Абдулхая 🏤", callback_data="музей")
    ],
    [
      InlineKeyboardButton(text="Ремесленники 👨‍🎨", callback_data="Ремесленники")
    ]
  ]
)

XonobodEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="GOVERNMENT OF CITY KHONOBOD 🏛", callback_data="GOVERNMENT")
    ],
    [
      InlineKeyboardButton(text="City Center 🏙", callback_data="Center"),
      InlineKeyboardButton(text="Railway station 🚉", callback_data="Railway")
    ],
    [
      InlineKeyboardButton(text="City Market 🏪", callback_data="Market")
    ],
    [
      InlineKeyboardButton(text="Trade Center Uzbegim 🏪", callback_data="Makro 🏪"),
      InlineKeyboardButton(text="Xontog' ⛰", callback_data="Xontog ⛰"),
    ],
    [
      InlineKeyboardButton(text="Children's playground ⛹️", callback_data="Children's playground ⛹️")
    ],
    [
      InlineKeyboardButton(text="Abdulhay Folk Art History House Museum of S.Mehmanov🏤", callback_data="Museum")
    ],
    [
      InlineKeyboardButton(text="Artisans 👨‍🎨", callback_data="Artisans")
    ]
  ]
)






MasjidlarIn = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Xonobod jome masjidi🕌", callback_data="Xonobod jome masjidi🕌")
    ],
    [
      InlineKeyboardButton(text="Abdulhamid Qori jome masjidi🕌", callback_data="Tapalina masjidi🕌")
    ]
  ]
)
MasjidlarInRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Мечеть Джоме Ханабада🕌", callback_data="Мечеть Джоме Ханабада🕌")
    ],
    [
      InlineKeyboardButton(text="Мечеть Абдулхамида Кори🕌", callback_data="Мечеть Топалины🕌")
    ]
  ]
)
MasjidlarInEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Jome Mosque Xonobod🕌", callback_data="Jome Mosque Xonobod🕌")
    ],
    [
      InlineKeyboardButton(text="Abdulhamid Qori Mosque🕌", callback_data="Mosque Topolina🕌")
    ]
  ]
)