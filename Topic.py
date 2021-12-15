import Const
import Utils
from Utils import call_common
from bot import bot_object


def start_topic_1(call):
    bot_object.send_message(call.message.chat.id, Const.CHOOSE_TOPIC)
    bot_object.send_message(call.message.chat.id, Const.GOOD_CHOICE)
    bot_object.send_message(call.message.chat.id, Const.WHAT_HOMEWORK)
    call_common(call.message, Const.NEED_HELP, Const.MAP_2)


def topic_with_help_4(call):
    Utils.replace_keyboard(call)
    call_common(call.message, Const.ASK_HELP_NOW, Const.MAP_3)
