import telebot
import config

from telebot import types

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	markup=types.ReplyKeyboardMarkup()
	zayavka=types.KeyboardButton("Онлайн Заявка на Кредит")
	kredit=types.KeyboardButton("Просмотр Кредитные Данные")
	product=types.KeyboardButton("Продукты")
	lang=types.KeyboardButton("Язык")
	markup.row(zayavka)
	markup.row(kredit)
	markup.row(product,lang)
	bot.send_message(message.chat.id,config.WELCOME,parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type=='private':
		if message.text=="Продукты":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			mikrokreditovanie=types.KeyboardButton("Онлайн микрокредитование")
			busines=types.KeyboardButton("Бизнес микрокредитование")
			potrebitel=types.KeyboardButton("Потребительский микрокредит")
			microlizing=types.KeyboardButton("Микролизинг")
			ipoteka=types.KeyboardButton("Ипотека")
			home=types.KeyboardButton("На главное меню")
			markup.add(mikrokreditovanie,busines,potrebitel,microlizing,ipoteka,home)
			bot.send_message(message.chat.id,config.PRODUCTS,parse_mode='html', reply_markup=markup)



		#################################################################################

		# Назад
		if message.text=="Назад":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			mikrokreditovanie=types.KeyboardButton("Онлайн микрокредитование")
			busines=types.KeyboardButton("Бизнес микрокредитование")
			potrebitel=types.KeyboardButton("Потребительский микрокредит")
			microlizing=types.KeyboardButton("Микролизинг")
			ipoteka=types.KeyboardButton("Ипотека")
			home=types.KeyboardButton("На главное меню")
			markup.add(mikrokreditovanie,busines,potrebitel,microlizing,ipoteka,home)
			bot.send_message(message.chat.id,config.PRODUCTS,parse_mode='html', reply_markup=markup)
			
		#######################################################################################


		if message.text=="На главное меню":
			markup=types.ReplyKeyboardMarkup()
			zayavka=types.KeyboardButton("Онлайн Заявка на Кредит")
			kredit=types.KeyboardButton("Просмотр Кредитные Данные")
			product=types.KeyboardButton("Продукты")
			lang=types.KeyboardButton("Язык")
			markup.row(zayavka)
			markup.row(kredit)
			markup.row(product,lang)
			bot.send_message(message.chat.id,config.WELCOME,parse_mode='html', reply_markup=markup)

		if message.text=="Онлайн микрокредитование":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			tajistemol=types.KeyboardButton("ТачИстеъмол")
			tajtijorat=types.KeyboardButton("ТачТичорат")
			favri=types.KeyboardButton("Фаври")
			nazad=types.KeyboardButton("Назад")
			markup.add(tajistemol,tajtijorat,favri,nazad)
			bot.send_message(message.chat.id,config.MICROKREDITOVANIE,parse_mode='html', reply_markup=markup)

		if message.text=="Бизнес микрокредитование":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			predprinimatelstvo=types.KeyboardButton("Предпринимательство и селькое хозяйство")
			zelenie_technologii=types.KeyboardButton("Микрокредит на зеленые технологии")
			women_start_busines=types.KeyboardButton("Женшинам на старт бизнеса")
			razvitie=types.KeyboardButton("Развитие народного ремесленничества")
			skvadjini=types.KeyboardButton("Микрокредит на бурение скважины")
			nazad=types.KeyboardButton("Назад")
			markup.add(predprinimatelstvo,zelenie_technologii,women_start_busines,razvitie,skvadjini,nazad)
			bot.send_message(message.chat.id,config.BUSINES_MICRO,parse_mode='html', reply_markup=markup)

		if message.text=="Потребительский микрокредит":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			obuchenie=types.KeyboardButton("Обучение/Лечение")
			avtomashina=types.KeyboardButton("Покупка автомашины")
			zelenie_technologi=types.KeyboardButton("Зеленые технологии")
			potrebitelskiy_mikrokredit=types.KeyboardButton("'Потребительский микрокредит'")
			nazad=types.KeyboardButton("Назад")
			markup.add(obuchenie,avtomashina,zelenie_technologi,potrebitelskiy_mikrokredit,nazad)
			bot.send_message(message.chat.id,config.POTREBITELSKIY,parse_mode='html', reply_markup=markup)

		if message.text=="Микролизинг":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			innovation_parniki=types.KeyboardButton("Инновационные парники")
			oborudovanie=types.KeyboardButton("Оборудование, техника, грузовой автотранспорт и сельхозтехника")
			nazad=types.KeyboardButton("Назад")
			markup.add(innovation_parniki,oborudovanie,nazad)
			bot.send_message(message.chat.id,config.MICROKREDITOVANIE,parse_mode='html', reply_markup=markup)

		if message.text=="Ипотека":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			stroitelstvo=types.KeyboardButton("Строительство и покупка жилья")
			nedvidjimost=types.KeyboardButton("Строительство и покупка коммерческой недвижимости")
			nazad=types.KeyboardButton("Назад")
			markup.add(stroitelstvo,nedvidjimost,nazad)
			bot.send_message(message.chat.id,config.IPOTEKA,parse_mode='html', reply_markup=markup)

		###############################################################################

		#Онлайн микрокредитование

		if message.text=="ТачИстеъмол":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('ТачИстеъмол.jpg','rb'),caption=config.TAJISTEMOL,parse_mode='html', reply_markup=markup)

		if message.text=="ТачТичорат":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('ТачТичорат.jpg','rb'),caption=config.TAJTIJORAT,parse_mode='html', reply_markup=markup)

		if message.text=="Фаври":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Фаври.jpg','rb'),caption=config.FAVRI,parse_mode='html', reply_markup=markup)

		#################################################################################

		###############################################################################

		#Бизнес микрокредитование

		if message.text=="Предпринимательство и селькое хозяйство":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Предпринимательство.jpg','rb'),caption=config.PREDPRINIMATELSTVO,parse_mode='html', reply_markup=markup)

		if message.text=="Микрокредит на зеленые технологии":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('зеленые технологии.jpg','rb'),caption=config.ZELENIE_TEXNOLOGII,parse_mode='html', reply_markup=markup)

		if message.text=="Женшинам на старт бизнеса":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('женшинам на старт бизнеса.jpg','rb'),caption=config.START_BUSINESS,parse_mode='html', reply_markup=markup)

		if message.text=="Развитие народного ремесленничества":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Развитие народного ремесленничества.jpg','rb'),caption=config.RAZVITIE_NAROD,parse_mode='html', reply_markup=markup)

		if message.text=="Микрокредит на бурение скважины":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Микрокредит на бурение скважины.jpg','rb'),caption=config.SKVADJINI,parse_mode='html', reply_markup=markup)

		#################################################################################



		###############################################################################

		#Потребительский микрокредит

		if message.text=="Обучение/Лечение":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Обучение.jpg','rb'),caption=config.OBUCHENIE,parse_mode='html', reply_markup=markup)

		if message.text=="Покупка автомашины":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Покупка автомашины.jpg','rb'),caption=config.AVTOMASHINA,parse_mode='html', reply_markup=markup)

		if message.text=="Зеленые технологии":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('зеленые технологии.jpg','rb'),caption=config.ZELENIE_TEXNOLOGI,parse_mode='html', reply_markup=markup)

		if message.text=="'Потребительский микрокредит'":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('Потребительский микрокредит.jpg','rb'),caption=config.POTREBITELSKIY_MICROKREDIT,parse_mode='html', reply_markup=markup)

		#################################################################################

		###############################################################################

		#Микролизинг

		if message.text=="Инновационные парники":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('инновационные парники.jpg','rb'),caption=config.INNOVATION_PARNIKI,parse_mode='html', reply_markup=markup)

		if message.text=="Оборудование, техника, грузовой автотранспорт и сельхозтехника":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('ТачИстеъмол.jpg','rb'),caption=config.OBORUDOVANIE,parse_mode='html', reply_markup=markup)

		#################################################################################



		###############################################################################

		#Ипотека

		if message.text=="Строительство и покупка жилья":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('строительство.jpg','rb'),caption=config.STROITELSTVO,parse_mode='html', reply_markup=markup)

		if message.text=="Строительство и покупка коммерческой недвижимости":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_photo(message.chat.id,open('недвижимости.jpg','rb'),caption=config.NEDVIDJIMOST,parse_mode='html', reply_markup=markup)

		#################################################################################


bot.polling(none_stop=True)