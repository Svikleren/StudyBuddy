from telebot import types

from bot import bot_object


def call_common(message, question, use_map: dict):
    keyboard = types.InlineKeyboardMarkup()
    for key in use_map.keys():
        keyboard.add(types.InlineKeyboardButton(text=key, callback_data=use_map[key]))
    bot_object.send_message(message.chat.id, text=question, reply_markup=keyboard)


def replace_keyboard(call):
    bot_object.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=None)
    msg_text = '* Твой выбор: ' + find_element(call.message.reply_markup.keyboard, call.data) + '*'
    bot_object.send_message(call.message.chat.id, msg_text, parse_mode='Markdown')


def find_element(list, callback_data):
    for element in list:
        if element[0].callback_data == callback_data:
            return element[0].text
    return "Incorrect information!"
