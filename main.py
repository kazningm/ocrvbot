import telebot
from telebot import types
from dev import grid
import reports

TOKEN = "1631851878:AAGv34vSy1NfI3Oz_Uzkpdra3xs4SrY_u5A"
bot = telebot.TeleBot(TOKEN)
MODE = 'TEST'

bot.set_my_commands(commands=[types.BotCommand(command='/start', description='Начать поиск справки'),
                              types.BotCommand(command='/help', description='Описание работы бота и основные команды'),
                              types.BotCommand(command='/menu', description='Аналитические правки ЦОММ'),
                              types.BotCommand(command='/mode', description='Режим работы бота'),
                              types.BotCommand(command='/setmode', description='Установить режим мода (TEST/PROM)'),
                              types.BotCommand(command='/meh', description='Посмотреть на Михалыча')])


@bot.message_handler(commands=['start', 'help', 'meh', 'mode', 'setmode', 'menu'])
def mode(message):
    global MODE
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id, text='Для работы бота введите фрагмент названия справки')
    elif message.text == '/help':
        bot.send_message(chat_id=message.chat.id, text='пока пусто')
    elif message.text == '/meh':
        meh = open('meh.webp', mode='rb')
        bot.send_sticker(chat_id=message.chat.id, data=meh)
    elif message.text == '/mode':
        bot.send_message(chat_id=message.chat.id, text='Установлен режим: ' + MODE)
    elif message.text == '/setmode':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='TEST', url='', callback_data='TEST'))
        markup.add(types.InlineKeyboardButton(text='PROM', url='', callback_data='PROM'))
        bot.send_message(chat_id=message.chat.id, text='Выберите режим работы бота:', reply_markup=markup)
    elif message.text == '/menu':
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton(text='Назад', callback_data=10))
        t = 1
        row = []
        for report_name in reports.ANALIT_SPRAVKI_COMM.keys():
            row.append(types.InlineKeyboardButton(text=report_name, url='', callback_data=report_name))
        for g in grid(it=list(reports.ANALIT_SPRAVKI_COMM.keys()), count=2):
            row = []
            for report_name in g:
                row.append(types.InlineKeyboardButton(text=report_name, callback_data=report_name))
            markup.add(*row)
            row.clear()
        bot.send_message(chat_id=message.chat.id, text='Выберите раздел:', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def send(message):
    global MODE
    # bot.send_message(chat_id=message.chat.id, text='s', reply_markup=types.ReplyKeyboardRemove())
    count_spr = 0  # количество найденных справок по запросу пользователя
    markup = types.InlineKeyboardMarkup()
    for key, value in reports.ANALIT_SPRAVKI_COMM.items():
        for spr in value:
            if message.text.lower() in spr.name:
                count_spr += 1
                # если режим работы мода ПРОМ то ссылки на справки будут выдаваться на пром, иначе на тест
                markup.add(types.InlineKeyboardButton(text=spr.name,
                                                      url=spr.url if MODE == 'PROM' else spr.url_test))
    bot.send_message(chat_id=message.chat.id, text='Справки по вашему запросу (%s шт.)' % count_spr,
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda x: True)
def callback_query(call):
    global MODE
    if call.data in ('TEST', 'PROM'):
        MODE = call.data
        bot.answer_callback_query(callback_query_id=call.id, text='Установлен режим работы бота: ' + MODE)
    elif call.data in reports.ANALIT_SPRAVKI_COMM.keys():
        pass
    else:
        pass


#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='first button first button first button first button first button first button', url='', callback_data='first button')
#     btn2 = types.InlineKeyboardButton(text='second button', url='', callback_data='second button')
#     markup.add(btn1)
#     markup.add(btn2)
#     bot.send_message(chat_id=message.chat.id, text='Нажми на кнопку', reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     bot.send_message(chat_id=message.chat.id,
#                      text='/start',
#                      disable_web_page_preview=False)
#
#
# # bot.reply_to(message, text="Send me another word:")
# # call = {'game_short_name': None,
# # 'chat_instance': '-4779661538860694988',
# # 'id': '2043380786626191060',
# # 'from_user': {'id': 475761663, 'is_bot': False, 'first_name': 'Кирилл', 'username': 'kaznin', 'last_name': 'Казнин', 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None},
# # 'message': {'content_type': 'text', 'id': 398, 'message_id': 398, 'from_user': <telebot.types.User object at 0x04208CD0>, 'date': 1612434951, 'chat': <telebot.types.Chat object at 0x04208D00>, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Нажми на кнопку', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': <telebot.types.InlineKeyboardMarkup object at 0x04208AD8>, 'json': {'message_id': 398, 'from': {'id': 1631851878, 'is_bot': True, 'first_name': 'kzn', 'username': 'kznbotbot'}, 'chat': {'id': 475761663, 'first_name': 'Кирилл', 'last_name': 'Казнин', 'username': 'kaznin', 'type': 'private'}, 'date': 1612434951, 'text': 'Нажми на кнопку', 'reply_markup': {'inline_keyboard': [[{'text': 'first button', 'callback_data': 'first button'}], [{'text': 'second button', 'callback_data': 'second button'}]]}}}, 'data': 'first button', 'inline_message_id': None}
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     print(call.message.message_id)
#     if call.data == 'first button':
#         bot.answer_callback_query(callback_query_id=call.id, text=call.data)
#         markup = types.InlineKeyboardMarkup()
#         btn3 = types.InlineKeyboardButton(text='3 button', url='', callback_data='3 button')
#         btn4 = types.InlineKeyboardButton(text='4 button', url='', callback_data='4 button')
#         markup.add(btn3, btn4)
#         # bot.edit_message_reply_markup(chat_id=call.message.chat.id,
#         #                               message_id=call.message.message_id,
#         #                               reply_markup=markup)
#         bot.edit_message_text(text='Выбери новую кнопку',
#                               chat_id=call.message.chat.id,
#                               message_id=call.message.message_id,
#                               reply_markup=markup)
#

bot.polling()
