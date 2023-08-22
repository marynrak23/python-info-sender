import telebot
import threading
from time import sleep

from helpers.ids_saver import saveChatId
from helpers.ids_getter import getIDs
from helpers.check_user import checkUser
from helpers.apps_ids_getter import getIdsApps
from helpers.apps_ids_saver import saveChatIdApps
from helpers.get_nsq import getApps


bot = telebot.TeleBot('6576429362:AAHJk4nKvNHO7aEm9K_zvDLPJzN7cP1vuJ4', parse_mode=None)

sent_messages = {}

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
        chat_ids = getIdsApps()
        if str(chat_id) not in chat_ids:
            saveChatIdApps(chat_id)
            bot.send_message(chat_id, 'Прилы подключены')
        else:
            bot.send_message(chat_id, "Прилы уже подключены")


@bot.message_handler(commands=['delete'])
def handle_delete(message):
    print(sent_messages)
    for chat_id, message_id in sent_messages.items():
        try:
            bot.delete_message(str(chat_id), message_id)
        except Exception as e:
            print(f"Could not delete message in chat {chat_id}. Error: {e}")
    sent_messages.clear()



@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if checkUser(message.from_user.username):
        chat_ids = getIDs()
        sender_chat_id = message.chat.id
        if message.text.lower() != "/start" and message.text.lower() != "/apps" and message.text.lower() != "/delete":
            for chat_id in chat_ids:
                if chat_id != sender_chat_id:
                    sent_message = bot.send_message(chat_id, message.text)
                    sent_messages[str(chat_id)] = sent_message.message_id
    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Not accessed !')


@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    if checkUser(message.from_user.username):
        sender_chat_id = message.chat.id
        chat_ids = getIDs()
        photo = message.photo[-1]
        caption = message.caption
        for other_chat_id in chat_ids:
            if other_chat_id != sender_chat_id:  # Не отправляйте фото обратно в исходный чат
                sent_message = bot.send_photo(other_chat_id, photo.file_id, caption=caption)
                sent_messages[str(other_chat_id)] = sent_message.message_id  # Исправленная часть
    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Not accessed !')


def send_periodic_messages():
    while True:
        apps_chat_id = getIdsApps()
        banned_apps = getApps()
        print(banned_apps)
        print(apps_chat_id)
        for chat_id in apps_chat_id:
            for item in banned_apps:
                bot.send_message(chat_id, f"Приложение {item} забанено")
        sleep(3600)


threading.Thread(target=send_periodic_messages).start()

bot.infinity_polling()


