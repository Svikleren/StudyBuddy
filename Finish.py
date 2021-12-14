import Const
import Utils
from bot import bot_object


def finish_13(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.PRAISE)
    bot_object.send_message(call.message.chat.id, Const.GIFT)
    bot_object.send_message(call.message.chat.id, Const.BOT_HAPPY)
