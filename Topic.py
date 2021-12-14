import Const
from Utils import call_common
from bot import bot_object


def start_topic_1(message):
    bot_object.send_message(message.chat.id, Const.GOOD_LUCK)
    bot_object.send_message(message.chat.id, Const.CHOOSE_TOPIC)
    bot_object.send_message(message.chat.id, Const.GOOD_CHOICE)
    bot_object.send_message(message.chat.id, Const.WHAT_HOMEWORK)
    call_common(message, Const.NEED_HELP, Const.MAP_2)


def topic_with_help_4(message):
    call_common(message, Const.ASK_HELP_NOW, Const.MAP_3)


def topic_without_help_5_7(message):
    bot_object.send_message(message.chat.id, Const.I_TRUST_YOU)
    bot_object.send_message(message.chat.id, Const.WHEN_FINISH)


def topic_without_help_6(message):
    bot_object.send_message(message.chat.id, Const.LETS_POSTPONE)