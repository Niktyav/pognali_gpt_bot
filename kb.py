from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


menu_intro = [
    [InlineKeyboardButton(text="📝👤 Заполнить инфо о себе", callback_data="fill_info"),],
]
# menu_reg = [
#     [InlineKeyboardButton(text="🎉 Куда сходить на выходных?!", callback_data="my_city_events"),],    
#     [InlineKeyboardButton(text="🗼 Я в другом городе. Куда сходить?!", callback_data="another_city"),],
#     [InlineKeyboardButton(text="🏁 Сгенерировать квесты в городе", callback_data="gen_quests")],
#     [InlineKeyboardButton(text="👤 Заполнить инфо о себе?!", callback_data="my_info")],
#     [InlineKeyboardButton(text="🔎 Помощь?!", callback_data="help"),
#      InlineKeyboardButton(text="📄 Информация?!", callback_data="about_us"),]
# ]
menu_reg = [
    [InlineKeyboardButton(text="🎉 Куда сходить на выходных?!", callback_data="my_city_events"),],    
    [InlineKeyboardButton(text="👤 Заполнить инфо о себе?!", callback_data="my_info")],
    [InlineKeyboardButton(text="🔎 Помощь?!", callback_data="help"),
     InlineKeyboardButton(text="📄 Информация?!", callback_data="about_us"),]
]
    
exit_button= [[KeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]]

menu_intro = InlineKeyboardMarkup(inline_keyboard=menu_intro)
menu_reg = InlineKeyboardMarkup(inline_keyboard=menu_reg)
exit_kb = ReplyKeyboardMarkup(keyboard=exit_button, resize_keyboard=True)

update_info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="👤 Рассказать о себе?!", callback_data="my_info")]])

