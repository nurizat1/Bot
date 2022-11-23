import telebot

bot = telebot.TeleBot("5384193735:AAG0PY2Ncc1Zgj-uHE-y89AKNX8k6DL-D50")


@bot.message_handler(func=lambda message: True)
def create(message):
    if message.text == "привет" :
        bot.reply_to(message, "Здраствуйте,добро пожаловать в наш бот")
    elif message.text == "hi" :
        bot.reply_to(message, "Hello.Wellcome to our bot")
    elif message.text == "кто тебя создал":
        bot.reply_to(message,"я создана девушкой по имени Нуризат")
    elif message.text == "как тебя зовут":
        bot.reply_to(message, "меня зовут Lisa названа честь корейской поп звезды из группы Blackpink")
    else:
        bot.reply_to(message, "Я вас не понимаю")
bot.infinity_polling()



