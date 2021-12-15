import logging
import time

import Check
import Const
import Finish
import Topic
import Utils
from Utils import call_common
from bot import bot_object

logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s')


@bot_object.message_handler(commands=['vso'])
def vso(message):
    Check.start_check_vso(message)


@bot_object.message_handler(content_types=['text'])
def start_bot(message):
    logging.warning("We are starting session with user %s", message.from_user.full_name)
    call_common(message, Const.LETS_LEARN, Const.MAP_1)


def callback_2_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.HORRAY)


def callback_5_7_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.I_TRUST_YOU)
    bot_object.send_message(call.message.chat.id, Const.WHEN_FINISH)


def callback_10_12_method(call):
    Utils.replace_keyboard(call)
    Topic.start_topic_1(call)


def callback_6_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.LETS_POSTPONE)
    Topic.start_topic_1(call)


def callback_1_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.GOOD_LUCK)
    Topic.start_topic_1(call)


def callback_3_method(call):
    Utils.replace_keyboard(call)
    time.sleep(15)
    start_bot(call.message)


def callback_with_one_message(call, text):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, text)


@bot_object.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    lambdas_map = {Const.CALLBACK_1: lambda x: callback_1_method(x),
                   Const.CALLBACK_2: lambda x: callback_2_method(x),
                   Const.CALLBACK_3: lambda x: callback_3_method(x),
                   Const.CALLBACK_4: lambda x: Topic.topic_with_help_4(x),
                   Const.CALLBACK_5: lambda x: callback_5_7_method(x),
                   Const.CALLBACK_6: lambda x: callback_6_method(x),
                   Const.CALLBACK_7: lambda x: callback_5_7_method(x),
                   Const.CALLBACK_8: lambda x: Check.check_not_finished_8(x),
                   Const.CALLBACK_9: lambda x: Check.check_finished_9(x),
                   Const.CALLBACK_10: lambda x: callback_10_12_method(x),
                   Const.CALLBACK_11: lambda x: Check.check_other_homeworks_11(x),
                   Const.CALLBACK_12: lambda x: callback_10_12_method(x),
                   Const.CALLBACK_13: lambda x: Finish.finish_13(x),
                   Const.CALLBACK_14: lambda x: Topic.topic_with_help_4(x)}
    if lambdas_map.get(call.data) is not None:
        lambdas_map.get(call.data)(call)


bot_object.polling(none_stop=True, interval=0)
