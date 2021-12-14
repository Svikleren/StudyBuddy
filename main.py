import Check
import Const
import Finish
import Topic
import Utils
from Utils import call_common
from bot import bot_object


@bot_object.message_handler(commands=['vso'])
def vso(message):
    Check.start_check_vso(message)


@bot_object.message_handler(content_types=['text'])
def start_bot(message):
    call_common(message, Const.LETS_LEARN, Const.MAP_1)


def callback_2_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.HORRAY)


def callback_5_7_method(call):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, Const.I_TRUST_YOU)
    bot_object.send_message(call.message.chat.id, Const.WHEN_FINISH)


def callback_with_one_message(call, text):
    Utils.replace_keyboard(call)
    bot_object.send_message(call.message.chat.id, text)


@bot_object.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    lambdas_map = {Const.CALLBACK_1: lambda x: Topic.start_topic_1(x),
                   Const.CALLBACK_2: lambda x: callback_2_method(x),
                   Const.CALLBACK_3: lambda x: callback_with_one_message(x, Const.POSTPONE),
                   # TODO delay functionality,
                   Const.CALLBACK_4: lambda x: Topic.topic_with_help_4(x),
                   Const.CALLBACK_5: lambda x: callback_5_7_method(x),
                   Const.CALLBACK_6: lambda x: callback_with_one_message(x, Const.LETS_POSTPONE),
                   Const.CALLBACK_7: lambda x: callback_5_7_method(x),
                   Const.CALLBACK_8: lambda x: Check.check_not_finished_8(x),
                   Const.CALLBACK_9: lambda x: Check.check_finished_9(x),
                   Const.CALLBACK_10: lambda x: callback_with_one_message(call, "TODO: go to the beginning of Topic"),
                   Const.CALLBACK_11: lambda x: Check.check_other_homeworks_11(x),
                   Const.CALLBACK_12: lambda x: callback_with_one_message(call, "TODO: go to the beginning of Topic"),
                   Const.CALLBACK_13: lambda x: Finish.finish_13(x),
                   'nothing': lambda x: x}
    lambdas_map.get(call.data)(call)


bot_object.polling(none_stop=True, interval=0)
