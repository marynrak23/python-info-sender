import telebot
from helpers.ids_saver import saveChatId
from helpers.ids_getter import getIDs
from helpers.check_user import checkUser
from helpers.apps_ids_getter import getIdsApps
from helpers.apps_ids_saver import saveChatIdApps
import threading
from time import sleep


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


@bot.message_handler(commands=['apps'])
def send_message(message):
    if checkUser(message.from_user.username):
        chat_id = message.chat.id
        saveChatIdApps(chat_id)
        bot.send_message(chat_id, 'Прилы подключены')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if checkUser(message.from_user.username):
        chat_ids = getIDs()
        sender_chat_id = message.chat.id
        if message.text.lower() != "/start" and message.text.lower() != "/apps":
            for chat_id in chat_ids:
                if chat_id != sender_chat_id:
                    bot.send_message(chat_id, message.text)
    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Not accessed !')


def send_periodic_messages():
    while True:
        for chat_id in getIDs():
            bot.send_message(chat_id, "Это периодическое сообщение.")
        sleep(40)


# threading.Thread(target=send_periodic_messages).start()

bot.infinity_polling()


