import telebot

bot=telebot.TeleBot('5151249056:AAFS6LkG5VlBvv_dpblIoRvmsWQK3VU21Vo')

@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id,f'бла-бла <a href="https://picsum.photos/200/300">&#8205;</a>',parse_mode='html')
bot.polling(none_stop=False)