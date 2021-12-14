import Const
from bot import bot_object


def finish_13(message):
    bot_object.send_message(message.chat.id, Const.PRAISE)
    bot_object.send_message(message.chat.id, Const.GIFT)
    bot_object.send_message(message.chat.id, Const.BOT_HAPPY)
