import Const
from Utils import call_common
from bot import bot_object


def start_check_vso(message):
    call_common(message, Const.HOW_ARE_YOU, Const.MAP_4)


def check_not_finished_8(message):
    bot_object.send_message(message.chat.id, Const.I_TRUST_YOU)


def check_finished_9(message):
    bot_object.send_message(message.chat.id, Const.PRAISE)
    bot_object.send_message(message.chat.id, Const.GREAT)
    call_common(message, Const.ANY_OTHER_HOMEWORK, Const.MAP_5)


def check_other_homeworks_11(message):
    call_common(message, Const.ANY_POSTPONED_HOMEWORK, Const.MAP_6)
