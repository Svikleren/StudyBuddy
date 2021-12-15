YES = 'Да'
NO = 'Нет'
NOT_TODAY = 'Сегодня ничего делать не надо'
POSTPONE = 'Отложим'
CHOOSE_TOPIC = 'Выбери предмет'
WHAT_HOMEWORK = 'А что задали?'
NEED_HELP = 'Нужна помощь?'
I_NEED_HELP = 'Нужна помощь'
ASK_HELP_NOW = 'Ты можешь попросить помощи сейчас?'
WHEN_FINISH = 'Когда закончишь напиши /vso'
LETS_POSTPONE = 'Тогда давай отложим и сделаем пока что-то другое'
NOT_YET = 'Еще не все'
FINISH = 'Все'
GREAT = 'Класс!'
ANY_OTHER_HOMEWORK = 'Еще что-то задали?'
ANY_POSTPONED_HOMEWORK = 'А отложенные предметы остались?'
GIFT = 'Пора получать награду'

LETS_LEARN = 'Будем делать уроки?'  # read from DB
HORRAY = 'Ура!'  # read from DB
GOOD_LUCK = 'Удачи!'  # read from DB
GOOD_CHOICE = 'Отличный выбор!'  # read from DB
I_TRUST_YOU = 'Я верю, что ты справишься!'  # read from DB
HOW_ARE_YOU = 'Как успехи?'  # read from DB
PRAISE = 'Ты умница!'  # read from DB
BOT_HAPPY = 'Я очень рада, что у тебя все получилось!'  # read from DB

CALLBACK_1 = '1'
CALLBACK_2 = '2'
CALLBACK_3 = '3'
CALLBACK_4 = '4'
CALLBACK_5 = '5'
CALLBACK_6 = '6'
CALLBACK_7 = '7'
CALLBACK_8 = '8'
CALLBACK_9 = '9'
CALLBACK_10 = '10'
CALLBACK_11 = '11'
CALLBACK_12 = '12'
CALLBACK_13 = '13'
CALLBACK_14 = '14'

MAP_1 = {YES: CALLBACK_1,
         NOT_TODAY: CALLBACK_2,
         POSTPONE: CALLBACK_3}

MAP_2 = {YES: CALLBACK_4,
         NO: CALLBACK_5}

MAP_3 = {NO: CALLBACK_6,
         YES: CALLBACK_7}

MAP_4 = {NOT_YET: CALLBACK_8,
         FINISH: CALLBACK_9,
         I_NEED_HELP: CALLBACK_14}

MAP_5 = {YES: CALLBACK_10,
         NO: CALLBACK_11}

MAP_6 = {YES: CALLBACK_12,
         NO: CALLBACK_13}
