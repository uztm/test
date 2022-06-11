from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# dachaUz

dachaUz = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Dacha 10 🏕", callback_data="Dacha 10 🏕"),
      InlineKeyboardButton(text="XonDacha 🏕", callback_data="XonDacha 🏕"),
    ],
    [
      InlineKeyboardButton(text="Labi Anhor 🏕", callback_data="Labi Anhor 🏕"),
      InlineKeyboardButton(text="Dachalar 🏕", callback_data="Dachalar 🏕")
    ]
  ]
)

dachaRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Дача 10 🏕", callback_data="Дача 10 🏕"),
      InlineKeyboardButton(text="ХанДача 🏕", callback_data="ХанДача 🏕"),
    ],
    [
      InlineKeyboardButton(text="Лаби Анхор 🏕", callback_data="Лаби Анхор 🏕"),
      InlineKeyboardButton(text="Дачи 🏕", callback_data="Дачи 🏕")
    ]
  ]
)

dachaEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Dacha 10 🏕", callback_data="Dacha 10"),
      InlineKeyboardButton(text="XonDacha 🏕", callback_data="XonDacha"),
    ],
    [
      InlineKeyboardButton(text="Labi Anhor 🏕", callback_data="Labi Anhor"),
      InlineKeyboardButton(text="Migros 🏕", callback_data="Migros 🏕")
    ]
  ]
)

# relax


relaxUz = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Xonobod Sihatgohi 🏖", callback_data="Xonobod Sihatgohi 🏖"),
    ],
    [
      InlineKeyboardButton(text="Fozilmon Ota 🏖", callback_data="Fozilmon Ota 🏖"),
      InlineKeyboardButton(text="Kemping 🏖", callback_data="Kepmin 🏖")
    ],
    [
      InlineKeyboardButton(text="Oilaviy Dam Olish Maskani 🏖", callback_data="Oilaviy Dam Olish Maskani 🏖")
    ],
    [
      InlineKeyboardButton(text="Olovuddin Lager 🏖", callback_data="Olovuddin Lager 🏖"),
      InlineKeyboardButton(text="Andijon Soy 🏖", callback_data="Andijon Soy 🏖"),
    ],
    [
      InlineKeyboardButton(text="Afsona 🏖", callback_data="Afsona 🍽"),
      InlineKeyboardButton(text="Altin O'rda 🏖", callback_data="O'tov choyxona 🍽"),
    ]
  ]
)

relaxRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Санатория Ханабада 🏖", callback_data="Санатория Ханабада 🏖"),
    ],
    [
      InlineKeyboardButton(text="Фазилмон Ота 🏖", callback_data="Фазилмон Ота 🏖"),
      InlineKeyboardButton(text="Кемпинг 🏖", callback_data="Кепмин 🏖")
    ],
    [
      InlineKeyboardButton(text="Семейный курорт 🏖", callback_data="Семейный курорт 🏖")
    ],
    [
      InlineKeyboardButton(text="Оловуддин Лагер 🏖", callback_data="Оловуддин Лагер 🏖"),
      InlineKeyboardButton(text="Андижан Сой 🏖", callback_data="Андижан Сой 🏖"),
    ],
    [
      InlineKeyboardButton(text="Афсона 🏖", callback_data="Афсона 🍽"),
      InlineKeyboardButton(text="Алтин Орда 🏖", callback_data="Чайхана Отов 🍽"),
    ]
  ]
)

relaxEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Sanatorium Khanabad 🏖", callback_data="Sanatorium Khanabad 🏖"),
    ],
    [
      InlineKeyboardButton(text="Fazilmon Ota 🏖", callback_data="Fazilmon Ota 🏖"),
      InlineKeyboardButton(text="Kemping 🏖", callback_data="Kepmin")
    ],
    [
      InlineKeyboardButton(text="Семейный курорт 🏖", callback_data="Family Resort 🏖")
    ],
    [
      InlineKeyboardButton(text="Lager Olovuddin 🏖", callback_data="Olovuddin Lager"),
      InlineKeyboardButton(text="Andijan Soy 🏖", callback_data="Andijan Soy"),
    ],
    [
      InlineKeyboardButton(text="Afsona 🏖", callback_data="Afsona 🍽"),
      InlineKeyboardButton(text="Altin O'rda", callback_data="Teahouse Otov 🍽"),
    ]
  ]
)

hotel = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Uy Mehmonxonasi 🛎", callback_data="Uy Mehmonxona 🏕"),
      InlineKeyboardButton(text="Mehmonxona 🛎", callback_data="Mehmonxona 🏕"),
    ],
    [      
      InlineKeyboardButton(text="Sherdor Uy Mehmonhonasi 🛎", callback_data="Sherdor"),
    ]
  ]
)

hotelRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Хоум Отель 🛎", callback_data="Хоум Отель 🏕"),
      InlineKeyboardButton(text="Отель 🛎", callback_data="Отель 🏕"),
    ],
    [
      InlineKeyboardButton(text="Хаус Отель Шердор 🛎", callback_data="Sherdorru"),
    ]
  ]
)

hotelEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="House Hotel 🛎", callback_data="Home Hotel 🏕"),
      InlineKeyboardButton(text="Hotel 🛎", callback_data="Hotel 🏕"),
    ],
    [
      InlineKeyboardButton(text="Sherdor House Hotel 🛎", callback_data="Sherdoren"),
    ]
  ]
)