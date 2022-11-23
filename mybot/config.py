import telebot


bot = telebot.TeleBot("5911113933:AAHjK5m5F6d3RkZdBbsvAU1qhaGlHjsQc6Y")





@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
