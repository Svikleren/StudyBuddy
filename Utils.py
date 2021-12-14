from telebot import types

from bot import bot_object


def call_common(message, question, use_map: dict):
    keyboard = types.InlineKeyboardMarkup()
    for k in use_map.keys():
        keyboard.add(types.InlineKeyboardButton(text=k, callback_data=use_map[k]))
    bot_object.send_message(message.chat.id, text=question, reply_markup=keyboard)
