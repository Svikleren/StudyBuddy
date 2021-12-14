import Const
import Utils
from bot import bot_object


def start_check_vso(message):
    Utils.call_common(message, Const.HOW_ARE_YOU, Const.MAP_4)


def check_not_finished_8(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.I_TRUST_YOU)


def check_finished_9(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.PRAISE)
    bot_object.send_message(call.message.chat.id, Const.GREAT)
    Utils.call_common(call.message, Const.ANY_OTHER_HOMEWORK, Const.MAP_5)


def check_other_homeworks_11(call):
    Utils.replace_keyboard(call)
    Utils.call_common(call.message, Const.ANY_POSTPONED_HOMEWORK, Const.MAP_6)
