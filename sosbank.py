from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sos = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Tez Yordam 🚑", callback_data="Tez Yordam 🚑"),
      InlineKeyboardButton(text="IIB 🚓", callback_data="IIB 🚓"),
    ],
    [
      InlineKeyboardButton(text="FVV 🚒", callback_data="FVV 🚒"),
      InlineKeyboardButton(text="Milliy Gvardiya 🚔", callback_data="Milliy Gvardiya 🚔"),
    ]
  ]
)

sosru = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Скорая помощь 🚑", callback_data="Скорая помощь 🚑"),
      InlineKeyboardButton(text="УВД 🚓", callback_data="УВД 🚓"),
    ],
    [
      InlineKeyboardButton(text="МЧС 🚒", callback_data="МЧС 🚒"),
      InlineKeyboardButton(text="Гвардия 🚔", callback_data="Гвардия 🚔"),
    ]
  ]
)

sosEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Ambulance 🚑", callback_data="Ambulance 🚑"),
      InlineKeyboardButton(text="POLICE 🚓", callback_data="POLICE 🚓"),
    ],
    [
      InlineKeyboardButton(text="MES 🚒", callback_data="MES 🚒"),
      InlineKeyboardButton(text="Guard 🚔", callback_data="Guard 🚔"),
    ]
  ]
)

bank = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Xalq Banki 🏦", callback_data="Halqbank 🏦"),
      InlineKeyboardButton(text="SQB 🏦", callback_data="SQB 🏦"),
    ]
  ]
)

bankru = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Народный банк 🏦", callback_data="Народный банк 🏦"),
      InlineKeyboardButton(text="ПСБ 🏦", callback_data="ПСБ 🏦"),
    ]
  ]
)

bankEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="National bank 🏦", callback_data="National bank 🏦"),
      InlineKeyboardButton(text="ICB 🏦", callback_data="ICB 🏦"),
    ]
  ]
)