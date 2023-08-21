import telebot


bot = telebot.TeleBot('6576429362:AAHqaI6T9DnEC4vfKeQmM-lcnfZWK8079ss', parse_mode=None)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    print(f"Received a message in chat {chat_id}: {message.text}")


bot.infinity_polling()


