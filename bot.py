import telebot
from helpers.ids_saver import saveChatId
from helpers.ids_getter import getIDs
from helpers.check_user import checkUser


bot = telebot.TeleBot('6576429362:AAHqaI6T9DnEC4vfKeQmM-lcnfZWK8079ss', parse_mode=None)


@bot.message_handler(commands=['start'])
def handle_start(message):
    if checkUser(message.from_user.username):
        chat_id = message.chat.id
        if str(chat_id) not in getIDs():
            saveChatId(chat_id)
            bot.send_message(chat_id, "Привет! Я буду делится самыми свежими офферами\n"
                                      "Так же, если ты пользуешься нашими прилами, я скажу, если какая-то из прил забанится")
    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Not accessed !')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if checkUser(message.from_user.username):
        chat_ids = getIDs()
        sender_chat_id = message.chat.id  # Сохраняем ID чата отправителя
        if message.text.lower() != "/start" and message.text.lower() != "/apps":
            for chat_id in chat_ids:
                if chat_id != sender_chat_id:  # Проверяем, не является ли этот чат отправителем
                    bot.send_message(chat_id, message.text)
    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Not accessed !')


bot.infinity_polling()


