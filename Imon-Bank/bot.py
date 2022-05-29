import telebot
import config

from telebot import types

import mysql.connector
from mysql.connector import Error

bot=telebot.TeleBot(config.TOKEN)

surname=''
name=''

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE imon_bank"
create_database(connection, create_database_query)

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "", "imon_bank")

def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    surname TEXT,
    name TEXT,
    passport_number TEXT,
    number_phone TEXT,
    region TEXT,
    birthday TEXT,
    INN TEXT,
    pol TEXT,
    mail TEXT,
    doxod TEXT,
    rasxod TEXT,
    address TEXT,
    PRIMARY KEY (id)
)  ENGINE=InnoDB
"""

execute_query(connection, create_users_table)


def db_table_val(surname:str,name: str):
	cursor.execute('INSERT INTO users(surname,name) VALUES(%s,%s)',(surname,name))
	connection.commit()


@bot.message_handler(commands=['start'])
def welcome(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard = False)
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
			markup=types.ReplyKeyboardMarkup(resize_keyboard = False,row_width=1)
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
			markup=types.ReplyKeyboardMarkup(resize_keyboard = False)
			zayavka=types.KeyboardButton("Онлайн Заявка на Кредит")
			kredit=types.KeyboardButton("Просмотр Кредитные Данные")
			product=types.KeyboardButton("Продукты")
			lang=types.KeyboardButton("Язык")
			markup.row(zayavka)
			markup.row(kredit)
			markup.row(product,lang)
			bot.send_message(message.chat.id,config.WELCOME,parse_mode='html', reply_markup=markup)

		if message.text=="Онлайн микрокредитование":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			tajistemol=types.KeyboardButton("ТачИстеъмол")
			tajtijorat=types.KeyboardButton("ТачТичорат")
			favri=types.KeyboardButton("Фаври")
			nazad=types.KeyboardButton("Назад")
			markup.add(tajistemol,tajtijorat,favri,nazad)
			bot.send_message(message.chat.id,config.MICROKREDITOVANIE,parse_mode='html', reply_markup=markup)

		if message.text=="Бизнес микрокредитование":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			predprinimatelstvo=types.KeyboardButton("Предпринимательство и селькое хозяйство")
			zelenie_technologii=types.KeyboardButton("Микрокредит на зеленые технологии")
			women_start_busines=types.KeyboardButton("Женшинам на старт бизнеса")
			razvitie=types.KeyboardButton("Развитие народного ремесленничества")
			skvadjini=types.KeyboardButton("Микрокредит на бурение скважины")
			nazad=types.KeyboardButton("Назад")
			markup.add(predprinimatelstvo,zelenie_technologii,women_start_busines,razvitie,skvadjini,nazad)
			bot.send_message(message.chat.id,config.BUSINES_MICRO,parse_mode='html', reply_markup=markup)

		if message.text=="Потребительский микрокредит":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			obuchenie=types.KeyboardButton("Обучение/Лечение")
			avtomashina=types.KeyboardButton("Покупка автомашины")
			zelenie_technologi=types.KeyboardButton("Зеленые технологии")
			potrebitelskiy_mikrokredit=types.KeyboardButton("'Потребительский микрокредит'")
			nazad=types.KeyboardButton("Назад")
			markup.add(obuchenie,avtomashina,zelenie_technologi,potrebitelskiy_mikrokredit,nazad)
			bot.send_message(message.chat.id,config.POTREBITELSKIY,parse_mode='html', reply_markup=markup)

		if message.text=="Микролизинг":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			innovation_parniki=types.KeyboardButton("Инновационные парники")
			oborudovanie=types.KeyboardButton("Оборудование, техника, грузовой автотранспорт и сельхозтехника")
			nazad=types.KeyboardButton("Назад")
			markup.add(innovation_parniki,oborudovanie,nazad)
			bot.send_message(message.chat.id,config.MICROKREDITOVANIE,parse_mode='html', reply_markup=markup)

		if message.text=="Ипотека":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			stroitelstvo=types.KeyboardButton("Строительство и покупка жилья")
			nedvidjimost=types.KeyboardButton("Строительство и покупка коммерческой недвижимости")
			nazad=types.KeyboardButton("Назад")
			markup.add(stroitelstvo,nedvidjimost,nazad)
			bot.send_message(message.chat.id,config.IPOTEKA,parse_mode='html', reply_markup=markup)

		###############################################################################

		#Онлайн микрокредитование

		if message.text=="ТачИстеъмол":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/C_z8a6lbJeHHyscv_qg4352S71VTVbbkBigtb72u9PlH87NzHFW17Sj-1L2dXE3cI3falIoU8elRLubnkHBadOp_V6-MKvxdwvx_mfycfDZwek72dCoUjwu6tk-TLIiaD_ZfcuSEUyTrhKDyDNNjXMIpCpSmNnOYj3euTiHFhz5xjeBLkrRAJZmKOXb1J5haMv5Ghd_6c2vUVqQzlr5l5SMhL3trAoVNCJxSSiLQBPdqw9pA2rwU1Usw-L5DuJOrsIIMwoQPR2Xa1yg4dCuFi7fQE2Pc8y4Do2KSZQdw7xend-0OHcysICsyJTKf0--vo8lR4sFpprlsa3ABuNNY3JbdfZWjDa8Bz5OyLYpZwrToDPGIb78IPKi2VmvGg0k0dqcE690nhr5mB8IFg4uVFiG6yc1DCY0mnx8Hc8595uc3IvNscgFLUN-n37du4FEv99Pyhh441d5cyeiXjbmSD3iphkbq3wCj1yTEhWjxiVX16yEoJJ-Neq1KCIJPQu0j0WHsIPwDXwESNRl62l91ol5E_YJkXSRnOUXE0U22eAOE8TARXddbvvmRw3Be8GnHmN-U7nBlXa2zqjS3h2EOxA7xXrP9PpnixfpfdD7xz42_e1kF8G9skyJWO2-vx0GU4F0FTgds7kTe3ME5FDZIf25H0f3oVWwdTSvVPW5c7pF4RXYm8P4myiUkdOSny74cW4HDSRK7qYsDn0DlCIkBDLWzJGfMAJIrirYsH_l-OVGyh3Ju0xxYkvSxg94F=w370-h248-no?authuser=0">&#8205;</a> {config.TAJISTEMOL} ',parse_mode='html', reply_markup=markup)

		if message.text=="ТачТичорат":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/XhOJMS7loBey2-5WdL3eebaDOMUi9kSuGoNWCjBdNKPVcN2NBAh2nz6yz7KvE64N1OpbbuDjvMhyiWQpYR_I2cKLNbbgWSSKnOjda1ifMExY5pCPVgAfOnpA7b55gw8q3Xfa5AbCst-6PkC-Bu7VSirqdhhwb5KPN03m9gegFatmgBp9zJA4c9S-kIZLr0OoG4fd_DSvp2ciYQNExagwLzurY_8ppAvAT98qk3e2AGGSWxaQ1guKMNa2dLbHq0a6LGmzZ2N3Q0X0bN_d7PxyFJBquYcr0kcF008rvwCUnxCVrNHI2YOYmbbvduIpDqyq62luvnv3GCYcZRpM4SDB9cJgQTmzTI66Lmf7ob7Q9oCYQu2SYcQEntOsiWhEVjJMUqqaLHAk1wSkLlbF43oeM6BZT7DjJVuJGRrzLcGJe4EkVCobq4yRCIqr87MGST0X9FOnpqsKsA39DnEcdHU_W2LreZNPeeyiVRrsQNliDTJlgpxWGlNVGpZU9WIGElkY_nBtpAfiP23ze8NVk2C3e6b0rbZceikyCrVGh-fM9_gRr6OkMlfrwxY332FvlqfLgOg5upQQdN8gIinU_lTu6COJdFnWcnd9kXNy3uiCHJ_7664UefSD5SvwZ4AV8uYUUY7XBfSRjhoNvKKe2R5XUUAgW0c9kjc5LegTo6abnnh9Y88QfiQPFN75DowQnttwc6i-w6Am2_xW5WJCTDMH8CiS3aH_HENk1fBS3DwssLqQeTwQYEBZWQm-lDQJ=w370-h248-no?authuser=0">&#8205;</a> {config.TAJTIJORAT} ',parse_mode='html', reply_markup=markup)

		if message.text=="Фаври":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/HAt2loKDEo83HEojeJBft-RkdwnmtHM847Ro98vVjcy8tz1cNrF6wzEvgqVdHeKhV7Nm5ZUARyt5IxgzXIIE3nzuSIDt_ctFzQLnBwGl6gLaCERLmz5zIM8utkfdp8d5zhXygN4ZZViAD0e4ipwCxmhCs6QwDRIzII2mlA3dzohzzRxF-QOoA2WRP4lSgvWVtVY5uVgofLiWa-zLUqB--p5rSLLKNwikciZunt8W6WJXxkXQrJ6Ur9hDSNL597fc03e94KkuHk0MZmehIX57xyyO6OvFWmBho7ZKbh6LSUyJVY5Jv2xUDAON4hjy3tHly9UORRUJwvxNg638pxMlYwVxyIb8QVmgYDi3fudObwM-aOatS6gl7vWOLEYfmVT7fGQkQ8cn0yhgJrlTkTCg3Au_ovjdYldtRW8QGTtEUPscapLTkXSyIWcSd5Rh89kN5i3U6kdTURn78dzF986Qmt-dwiIMEQ-4z-qL_M94RLE6dyscII7rCgEgjaYoRrztffbdEpz-JuXprU59-g_IzTnff6Zsw-O2ZEwehgvakmB1vXGKe2HXLb5kr9pXOSu2vk3CcJV4wwxvnI2DybKzLBH9ShtnpEn0ek9gF-HqgynjvZBN3elo9OIjkQkwmy_OiEVlXcW4hk9NqLYcARHuMOVLfC9X3FMWONK-ho9tP_Z8V4wrrW4Z99rpPneVBlqnMqsvet6BgtL0vu_2Th4l8DPUi7j0d4t6pq0dwwip906R2NLSn3hYJl71UHm0=w348-h233-no?authuser=0">&#8205;</a> {config.FAVRI} ',parse_mode='html', reply_markup=markup)

		#################################################################################

		###############################################################################

		#Бизнес микрокредитование

		if message.text=="Предпринимательство и селькое хозяйство":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/36-2IcD2F8ldkFL2c8B4yKUl0RjX2mn5xX-UldSLSkozNDFog_ash0VRHzrCYzRazMgDrp_jWK0hWPRBNIFTd2J2lUcdhMFoCC7pVJfXBX_os7G2GToRPHfkANuF6yCgXWUYXcnC6umsK8dIDPs1FUlC6bqM3wijII518KsS3sZTiKP1yoHAEU_QkUyjrXVdEQ7kRegS00gZPWQVCeuQf7V23rPOXhfzK_YeypbT_h4kuMzouY4Yk4OJd87_ufq3hBgzC4x3-aSho2JCpoxLKP5baLwigpadsN4WfQoXWK-4WEZGITEVzgLIx5TBDpJYzySlmyugkuMNu1FMEItmXOydsn30bNLz-k3So5faBeZ8yM9FhMjv5JZlKO3kXsAr6pA4ZpJZ3jIuzRNhu02LJmDB9wSyOHz4CJoWYxreLBO3fEIPORnVqGvuaC_D8_uU_XqI5G6thpsGcnzjNywzbENn4UdQEkZ9pGMlHAb_MOkdVovBmBsiZyOrXUCK4kBmlQpUTowb93RQTYvQzATf-PlSdnIQ2N0QRKpS5JL0WeLS-6PazD5__nPA6UqlNwaeQOjkNHxsLWArQy_Zsritc6h3xrpOmgvsPIRTG0WDjl9hN_15WVikDWnUwXztR9IaL_ZjJdYKd6nIa1UhoAkwGm9ZL8VgKooUvYmCjwYxPXDBvGDvkDKLcklJHUdhDPk4Qw1Z_Ph20x_mQ_Tc45nJtUvtHXdwAv8OC5DSm9TgmikrNDFO13HV2Z13FWTP=w370-h248-no?authuser=0">&#8205;</a> {config.PREDPRINIMATELSTVO} ',parse_mode='html', reply_markup=markup)

		if message.text=="Микрокредит на зеленые технологии":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/gLPEOKE69Q_W4EGgoqn9kmdBjSX6YGNpqz0X8aMMaS__d24Pbh7l4b56SRrukrTwpLK1JuBpIYr6jqSdtr1CoPF-T23sqhyuQmGhtHWhlk95YNl27gdkM40NDgpl9bf3fF3bWorBEMaf7Ios65J257P8bulzJ4aVsU2bcNt0pTTzR5i44KBEBTjZhxFT2IZavxD-jrTqmU2fn2QUns0ow4ncJTHWU4-zLHp5sDqPVLTx14IxRbWPo21ofJOAc9oEeMH5yUHE1Rpf7DqPFSxn6gUdV25hv9RMtcYTt3k6s75NwAyF3M9V0k7-VM6TJ8Z8YDyz_sakhwtnHyEfkm6NE-gM84bU4v32tI19BcTMq8kOd2Gqkgwymx1uZR5FImK64wZ-o4LICD3aEOA2215tz8dWKdZklNRB7Be8ZRuSterY8xfe1OXMGABIwCvXQkq71vY7GoqNxBFyry4I7wWMQtm1DckqFF8SpzwK_aGdjAIpJHgvZpUF9qnGRDtDVpn5oSXv4i9SIWB7NwIe5KNMSi7x3QycF6lkjMvtZTnMwmn0w6DYelkh2ptbHfqplpEl5AqlzVJwfNMvgCVIfaGIzyldbriSUAqGwlIwqY82Y4Kkn3KM5zgs67K5px1kHkvNAREPmDQEriZ-uUQSUHe15GmbaIZh7t_VQ-8hrkYB8JFi67uB31QJlOXmAbQz0qCEk6v8kNwZNLXTQJysE_Ou4x_yo54PWmgY7NVauutkufFvBkfjlYTh2ak_dbL2=w328-h220-no?authuser=0">&#8205;</a> {config.ZELENIE_TEXNOLOGII} ',parse_mode='html', reply_markup=markup)

		if message.text=="Женшинам на старт бизнеса":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/zDccHhry2rl6QpKhgwUY72xyNfuCK0y4ag0Y7FX7lVF1xB7KoGyqXXxDneFJm1GAvCSG3vZF1LtTW7p74oz0UG6gIxYDwCaioy_pqNr4bb9_T8F1yupAvceaxhA4CSsY8F-1aI9zscqCTbcdqx6qLrRxSD-Wlja3MNNjEs19JOXZpqbAYMPWSBx-ObLhinDzpH7mzxiAvtN58DOyRoVatJQ8aPcP-5GmOfCMXzYjBd-sZUoMkqYqrQTn4DK7NvVl2FQLmhP_PCD5LHdJZx0FME-vyUIMl19bRHXFddj6HNO_x3gXHwTMYSai-WXAkcrnk_vTORxWEgmjuDVyDfavmZeuQBaodpffi5pS3XxyNF8SOPdq8dAXe4zGoy-B3l_8i-u3afJbXVcBhS2xCGbgXdHIMyoxtByIPZloUnBqG8DJr4S91VzS0eTwINaT3cJb-sT2hgea0fZA4UnPR0L1rF7NpEaCwAL5d8BWbPSG_70MQC7JaJoVHLhucpL9m1jqusnxLc5H3-3lXKVEJeZuf2tSpn-fCU_OlLkwKjKVy2y8WvWyuuRG6JXH694q8pcbsBnARsZpLt6AH4HDF_0rv0H9Oj-ySm6CMzIExVg3n4dVCG5cjb82GjwlU5qbq4X4bcM2Pq2kFNTNfwq0pJQ41hg0vgPHN2n7pgndvo7jF8RTDZbNvQ2A6XttWYhdpEfD9c7YyvqwBU_g5BpK7A-EGT2gU9heHvciMbhhXgQDJa1TmxRXUpaHOzwT94zA=w348-h233-no?authuser=0">&#8205;</a> {config.START_BUSINESS} ',parse_mode='html', reply_markup=markup)

		if message.text=="Развитие народного ремесленничества":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/Y7pPK8MsDEOEqP5P27yiBasuuNqW1AKtR2tJZbrrOFhe4snEtoKSyMLR3AhEl3JFJBicas1yqE3x7BgsVNQanT6MurcL5ES4DXuZUrfMgYZdH8_eiYHhu9AzBwDqcnYR4NXwRlTYb5j6QHTcYHHM0Nma2Kvdlus7T6UolSO6fC6O8689h1IYQVAaUHBdZz4fmrzvGsWkLPtE84Js-BZ1RNnkCisJ09-mwYOIz20JM4OPsNyJv7fduWmmALRf2zKwbqeEI67elRw4maUL8nEBp6jioRmDRmpK40J_P9qeGm-VEQ0CAOUCEFLOKXYfPBQK0kaXIR1DHXxHStArlUA0SOHKHCFB5gHsZoXrNA2JmUD0AFeLaBglCbcSgVzMEPOdy-Hfp44OrCDDu-4gHlHUnfubQSyaSRGX7yJQQWwlP2CjMKQeErFjC8rhs3MVKDOkQjEfcJLmzqF_XAvYNpJd1ea4VRY5nOzfjsvRVEMj9wZP9v_CvJRkMlTXgM7LxU0ACVLSEwE8WWq4nRszWTTEw7xFIcc7V_nW9DkPrKES-xDwfyoLzqRvY6FlcoNgudhUJBO5yVS0juaHWZXFZ_-xACCKE1dnhwwMjzcQSSX30IJQFfcLKFFyHLh1OM_YVkUITR2Lw3FtYXh7pSmTjKm8OWdlRnrn3I7g2mG_D74h4emuWdHmj07cCcOz4R9KZOZhpOZyxxnV3kwck3qhHtP_G40rF8hUii_R4XRBsgbxUcC6RlvhCpixaCutvg7V=w348-h233-no?authuser=0">&#8205;</a> {config.RAZVITIE_NAROD} ',parse_mode='html', reply_markup=markup)

		if message.text=="Микрокредит на бурение скважины":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/xKAmsWQQgED4n0ajtTNJQN_13lGOYm_yt9kz0QXEMh59ixNfSSSIZDc1IDIwRxskGw8_KeRJ_1Oqd_BPuP-w70Jfc7L-kXJ6koBhIGQxlYUqD4JKkzznSIOXnBq3zlRsCvnQPs55LaeHcdL1K5bXW2Y4y9bQO2k3gycMfrNMfLF_UwyFwv50YD6wWADHUXTs5Bv8T5NzVpIP-DS4IcrMxPkz0GSE3VeA3wpGlpBxoQiUP4pwsr0-uG1rpquod-1mgSf1G1Bfakh9wnFK5Gy5d83xlP1erPA0568ZcbwTxk3yNVS3o3KhxJijVdZEH95xbhyf9HKIblt6SCLWUj-pRP_aovphc4SzYL3qSheXtcdyzDDKAJbAH331q1CjYsmuY3vVA3RdlgR0sVV273VX7zGi_wxYREvjroJFKg1KlKENudvuCS-hPnu_0cZ54ICTTVI8uRg4pUE0RJBZL8YRTI3Lf4T2TffhsnNd2-WjEx1Q5Bt9y771uu4CyEGBVS18ElB4VkrHwUF0pOTwVcM-w8YBJZe_i4cSiNKCtt0XOYenE-8qCJjE-rT4PuRWEI9oy4uAxZ8FgLiBm2j7Fmxi0QvjXimL4ZRPcN59BoJtZk-KzcW0M5thZz14i2EErVOuI97B3ZiVLO0zBQJQ0Gxw4L6UEfn9OAdSBKPTvIRjkso9QFt2VDxy0wLtLqtVF-6BYf5fG5CmpYPifZ1XRuLMYpUIGhGX13djpsqolWS3CnsnlzqHFuYvEcdqWhyP=w348-h233-no?authuser=0">&#8205;</a> {config.SKVADJINI} ',parse_mode='html', reply_markup=markup)

		#################################################################################



		###############################################################################

		#Потребительский микрокредит

		if message.text=="Обучение/Лечение":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/D3gF7zzmssUJWBEp_TT4DYPfwHJcSMgFUX6FPLebJHZcTbWjqZT60sWVGNXAaEmn2KLyOIOrvAjvlNUj4Kz6S6Pt7A0-NgrVel5q7z7U5neY_lmdFqysAbb9pr1tM7eVXzx-QAM2GFygxHbKRihXS9TYNDqjeihxCCN1UIpgK-5QooI2ewfqH8qvrvgJS7qRJu4py_sN-twNzzoKVcVjtECxGovvWumEkiz-P_tbFizv9YRdDZXdavBx6i9UTIpw0AaeXnYibe6wWfrm0Y6EJahdNPISaeEqtp7YO2MQLiI-1tN7PJhm2sMDuo34UQa7miRY0PHVHTf3nssGW9IBO-y-8MEAOpijykA-4D-6EfVd6WISQWO-D1ERCIz3NTyEpGWL3AQIu2KlbFVwpoHBoHfW_61nr0Q8zI7TKAk17u0rYFDjL2JRTdLbKwgbYSTdhEa82n9LVr1g63ZTjJNMZCaYIPYKEBEx6Q2ig9G2SgfFmlAweZTCpgu7RJzRwx0T0lqtXztwROn0ta1fVXJst3AEemQPIVte619dcmQ9VrloifVHLKdotHQTn_Tvsx2QpSjkNAJjk5yzzwS-IRTgp0CtD5SvOWrQjHpvNStzvoNf5bZKb2guK40fH-WIBaK6Thtop4HpprT5jVU8SE8Kcfe-PQCwCuZZHkUuv1-oAi5lShqklBszu5WjbS6Sk4KZgmPR3Wyp1v-bsOwfHUpr7uGPxoVZnR9qEAsu26VVzqWpea8Ow8EAK258wab9=w348-h233-no?authuser=0">&#8205;</a> {config.OBUCHENIE} ',parse_mode='html', reply_markup=markup)

		if message.text=="Покупка автомашины":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/FSpF4job3rveShkIzd9qU-WdFp3ABu3iC7ly7QfF0XHl6BzVGOGxm1sTCTbH9fY2DZm-_ss3NajeY1ROAMbbNXn1OJ4EBwBJNWDrWUVRhaaZztsCLh434zAf9Cr9kl32Qbr600LyeZ0bM9rjuYnhr61IzFWoE1Fb01WynVimBFUMTEa3xV24q02rluCRhHJhpoNyVB7jCXhNUc3JGrm-qh79Q2C6tvjABXokDB4eoWOsJfaF9S267rF4_jKmzxomFcRq7agNwccCYXhHAIzVxg5-ve39fD27yiLKq_QOCPsBfgm6RKxbBTg1zrtOqQT3KCzSUtL4idHjXokzW-n8nrOcyQJN5vH3gJwF-uoarDG6mGgC1ccQS5_ebxdN52DbDp8kvjIzDLmOEt8-w8MenFDMSMoewumS4dMSg2nPsGH3qEBt16gxhQttSE1nsOStXghebxBVMFf3IvLlNd94YsjetqHMy4N-D0C1C-LikS3EuEspPB-Rgi1FXgtuSo3j1FcJ9w6uj7HZuvWyNzApQQmaYrZejAxJxZ0zph_G4LUPovl5KJCYEtdh_OmiiuYU10KxPZOUqmDhFlQRykpC4Tp5ei-bXYoA1743YnuHjB7mGwUJrHrEHYFInrvmeThDSB-wbn9MDQWSwu-iNSDmxgS-El55TG02t982ihTpltEll8k2prTaoCfs455vSE0WgzFhdITHZjGdkK_al3Kw4z3nLHKa9c1q88Xz-q5BaGeTX3UoCPm6oRkn8AFC=w348-h233-no?authuser=0">&#8205;</a> {config.AVTOMASHINA} ',parse_mode='html', reply_markup=markup)

		if message.text=="Зеленые технологии":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/gLPEOKE69Q_W4EGgoqn9kmdBjSX6YGNpqz0X8aMMaS__d24Pbh7l4b56SRrukrTwpLK1JuBpIYr6jqSdtr1CoPF-T23sqhyuQmGhtHWhlk95YNl27gdkM40NDgpl9bf3fF3bWorBEMaf7Ios65J257P8bulzJ4aVsU2bcNt0pTTzR5i44KBEBTjZhxFT2IZavxD-jrTqmU2fn2QUns0ow4ncJTHWU4-zLHp5sDqPVLTx14IxRbWPo21ofJOAc9oEeMH5yUHE1Rpf7DqPFSxn6gUdV25hv9RMtcYTt3k6s75NwAyF3M9V0k7-VM6TJ8Z8YDyz_sakhwtnHyEfkm6NE-gM84bU4v32tI19BcTMq8kOd2Gqkgwymx1uZR5FImK64wZ-o4LICD3aEOA2215tz8dWKdZklNRB7Be8ZRuSterY8xfe1OXMGABIwCvXQkq71vY7GoqNxBFyry4I7wWMQtm1DckqFF8SpzwK_aGdjAIpJHgvZpUF9qnGRDtDVpn5oSXv4i9SIWB7NwIe5KNMSi7x3QycF6lkjMvtZTnMwmn0w6DYelkh2ptbHfqplpEl5AqlzVJwfNMvgCVIfaGIzyldbriSUAqGwlIwqY82Y4Kkn3KM5zgs67K5px1kHkvNAREPmDQEriZ-uUQSUHe15GmbaIZh7t_VQ-8hrkYB8JFi67uB31QJlOXmAbQz0qCEk6v8kNwZNLXTQJysE_Ou4x_yo54PWmgY7NVauutkufFvBkfjlYTh2ak_dbL2=w328-h220-no?authuser=0">&#8205;</a> {config.ZELENIE_TEXNOLOGI} ',parse_mode='html', reply_markup=markup)

		if message.text=="Потребительский микрокредит":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/v_jJChuz7L_LYden09g_egu6YJbvNHss8CfKb01dTo8Gruzp_8Uj5r8M22bWKgj7DEiDLELzgmIEMyYSz-qdBdEpee2n6hW44l3VUgpvAJd_RAYuhFhfP1GTP8K6mb4bwCZ_0UcVBvOIpJ5NeSFhm7NY6cbDX5UGct7LekJ6c35Lz-0YsfzW2-_8kfNwCY0ukLpui064bn5CXDgsKoKwKS49IIC1X65HMhbSpzfqwXGGIE369oeDp6z_WrnsuzSQDstvbAfOfHl-9__-GvCtngTnY6QGaBFCc6OcGbH4ordlFCAoXh1vESJfxamNpjUELWf8X6UtjbCJuwIU2oYNkZ3qTbB4nWWokRaEpaZ9BF3eWA8RO0UB3uXF15d5KTGl1FB5SeivWkgvSH6UkNEz4w3l2XjYM1EsLaUSO0UGtejs6l8JH7WjQYTeHHXPyJdamOY6C0goq53HEE0Tt58aA9RCdt3VQhTXgplrUKX4vb-_Vv7ZE048UOM82x2yCgLn3dBPTnN9xb2WQ8YEGOy_OiJo77mzrbTMRVLk_4BG6bqQ7cnz4cb4Cohn3clLIUXKQBc5_yVOHIVV9ZaGtZqZ2oAK5VE_w3CclnPteKuTO2gwdgS9I8YNunpFnz_6djtY2pwV_FAmUD-YxljAg_zTF0C8fCSL8Wx467LBP4nup3_66X4JnxECBC7RENru6q9TLJ70r5slHvGyN8xBwmqr0LEWNmPjofrIqCiNXBujAQUDhF8tsq4j73R39Qqc=w348-h233-no?authuser=0">&#8205;</a> {config.POTREBITELSKIY_MICROKREDIT} ',parse_mode='html', reply_markup=markup)

		#################################################################################

		###############################################################################

		#Микролизинг

		if message.text=="Инновационные парники":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/LKx8S31xCfwbFNom39u4wEPj5Zm0pXGFstpTfO_LOhKqQ-8ADT1zWmlZYNSOSDRnxBQfwOhDFKq9RrwGsnbHeZnZWneBrD_I5ug_f8wrgmXQqcLTZjYZfheZB0gcdWE8NfmuvgBlCTvphFzUBk_-xT2zg8FKpYUUTlSNrgN419uvQj0Qo1xd2ruc3Fn0Ka0GH9igz44kHXe2rQEOD149egW0EGSEAf4sa36jcUwh5--sbY4m8tq-3ijCJd0rc7bpDvwM7b3JbXYRiTGlgg0IfLf8ZtV0dUTPp5JPyNQyoKnuLMJbluJVWd0ZilENKqRkmJqncRXSEaB9y4N5ejkLnXddPALhAnBOgMNyCzlhMmRHhBdWNdAyUnvDwLERg7eAuc4B-HrkE3k6XtSY5ol9f9GY8OQKJahFIedefLUx8xUKIt1wobEX_8hYeMHkKtoTIzEC0342AfXbBeep-fzMgloJLcHl8G794wJJd9qaHf3J4m8Iol6UnnDMcjfv8trgqmkpIALeQy6oyIVB-5Wy8mawCBhROdFigEcX4s-1BcxBPwzWF7dLsoaQLlRR_HQbQohTFHSoRChzVRmDRYsFwNVfsywMnhJ3GWC8IZIz8vtbkJlIJJ1iSqv5ORcNmmtx1b_15LDuIgmxtrV6dPRomAOHeHVCbNd7dkO_zdboGjcthqi7M6b5X_yyCejfUtXN7OxWWmjI7j_bqv0uVa6SLoOXMdL9EN-4ld4lEdXdm9tEz4AnchHqK73Ty6Rq=w348-h233-no?authuser=0">&#8205;</a> {config.INNOVATION_PARNIKI} ',parse_mode='html', reply_markup=markup)

		if message.text=="Оборудование, техника, грузовой автотранспорт и сельхозтехника":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/gLPEOKE69Q_W4EGgoqn9kmdBjSX6YGNpqz0X8aMMaS__d24Pbh7l4b56SRrukrTwpLK1JuBpIYr6jqSdtr1CoPF-T23sqhyuQmGhtHWhlk95YNl27gdkM40NDgpl9bf3fF3bWorBEMaf7Ios65J257P8bulzJ4aVsU2bcNt0pTTzR5i44KBEBTjZhxFT2IZavxD-jrTqmU2fn2QUns0ow4ncJTHWU4-zLHp5sDqPVLTx14IxRbWPo21ofJOAc9oEeMH5yUHE1Rpf7DqPFSxn6gUdV25hv9RMtcYTt3k6s75NwAyF3M9V0k7-VM6TJ8Z8YDyz_sakhwtnHyEfkm6NE-gM84bU4v32tI19BcTMq8kOd2Gqkgwymx1uZR5FImK64wZ-o4LICD3aEOA2215tz8dWKdZklNRB7Be8ZRuSterY8xfe1OXMGABIwCvXQkq71vY7GoqNxBFyry4I7wWMQtm1DckqFF8SpzwK_aGdjAIpJHgvZpUF9qnGRDtDVpn5oSXv4i9SIWB7NwIe5KNMSi7x3QycF6lkjMvtZTnMwmn0w6DYelkh2ptbHfqplpEl5AqlzVJwfNMvgCVIfaGIzyldbriSUAqGwlIwqY82Y4Kkn3KM5zgs67K5px1kHkvNAREPmDQEriZ-uUQSUHe15GmbaIZh7t_VQ-8hrkYB8JFi67uB31QJlOXmAbQz0qCEk6v8kNwZNLXTQJysE_Ou4x_yo54PWmgY7NVauutkufFvBkfjlYTh2ak_dbL2=w328-h220-no?authuser=0">&#8205;</a> {config.OBORUDOVANIE} ',parse_mode='html', reply_markup=markup)

		#################################################################################



		###############################################################################

		#Ипотека

		if message.text=="Строительство и покупка жилья":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/U9_IR6aGHfk9FlXThSJwrbZjljAQcWY7XzmNeqMLzm0VTudEgcs9F8DNKb86FY68ej6TjIsmAAz4OAbF8f3GxrKnibmI3Dkt-RABcpfr3vlC1sydPYrFDJilAZv-2PBPTXGrz66P7c_erpj6R2Qv-Jpgd_aHLNcQw2N4KA6Vwm1u487h0566UONh1rQ8SvSCyJTa7LEIGCVFd7xPINL6sGVijlPwhZiY1DtEUQzglSKiZ30wyhLfqFmN72g598oxGk8LZb6flL0k6_95JodGlwyJM4xlDZFjBGDjgIJgwcRMopjeu26XOvTmQ_bElevA0HRdWepkWLpzImtbIiShfq7nGd8jAT1AKEU6bi4pJ6GFrRuNbBWtERdKEZ-1MfEg8-1fRGxR-KJgYoh1AHG9Iy5AcKvuQj2tgARU9ssS7GkLxjIoAKTGcsfPy66LH3GYc46OvVR5k2Y05EP01zEapK5ToFd7pfW2WGaey_wQ8_lKGXJ0kP5hek-ytWYgZJnn8kC3LdmZIXMlWbukBeQAaqLPXXm_OGYQ1y32GP7DLvZVeoEy1VIdyB560QzBw4aZrvD79B72q3r0f4cc-E6GZAjSZ-N2jej1OTM20aDRdYUULZfHTF9yfk6Nuj70zlQzuH-WQR8nHt0wNm3D9uGGrIdC-IGLqX02gQILiQP3UGFSDtE1wbArWRRCfkwpsVN_n15TOsunLJk2lpkMysf8YeXwpcyxDWyv05-ZSu5GOULEtiWLoPduynTi1pQg=w348-h233-no?authuser=0">&#8205;</a> {config.STROITELSTVO} ',parse_mode='html', reply_markup=markup)

		if message.text=="Строительство и покупка коммерческой недвижимости":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.chat.id,f'<a href="https://lh3.googleusercontent.com/CyPWSndUBR4Wy4ZGHdDrt1cP9Hqx4joD2qgNxMvv-Gs4NRbaBFDcK3Gc9qIf2bHqP5zNX5n0ixrxuOgMr4-dwhtmUvqRlXmYGO_FmyfWOl-RsVumCc-pNv4fYYyw4uewOv-55T4IYej4repJoi3C7U2P6b7DFiV8kMUXZkahAEV_173JSjKeqZ4wLoxauEgEUlCABTUOZcFTJM-nLNWwNLgnHRDTfKHInKNH_Ge3tm445406h_81Az1CVgcmMMwfnUlX0ymaV0Xk1ncMfQsWnqf-yDy6d8BLs0UMKixzdWsONeXjeM13o8ZzCBRbEicGlwnE5fm2LgS7JZMnHfhqnCraC5aOtXsBo30xJrOXUtlOCVyqW9S1c2XpR__CixkkOq7-GWrTk0VrbCRZNknaZ1nLviSqUeT6wDzroO_hBZE6DJFFIB7LqoWbUT4sXTpwmwDrqmpo9E1u4MQrjcHE3M6EYIru5mk7v70XpKZzoXZdwHd0NZ8aBDcms4bBKCsDHgpitJ-CmMc4JsEgfXyccQQCQGEVoos5tq1jkidcChURWsZNPNT1sQmRaD88DmMO_8eyndxgVjt75wB7iR61uN4WtC_p4Lyq9K66qwSSyZW0W-MAF5DRVDYjTYMsnbJQKt5xzm3s984fJ3IktRdKl5Hzf8aGJdFyY152Hm7Wl3YWamFoHbCj6iNYQX2gJZXZSLBCcQUUEC-Yizphs_czOQvtaAEr9kkRbYf2_NrgkOzfT84jPv84TyCF-qfz=w370-h248-no?authuser=0">&#8205;</a> {config.NEDVIDJIMOST} ',parse_mode='html', reply_markup=markup)

		#################################################################################

		if message.text=="Онлайн Заявка на Кредит":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			nazad=types.KeyboardButton("Назад")
			markup.add(nazad)
			bot.send_message(message.from_user.id,'Для подачи заявки на микрокредит заполните следующие поля. \nВаша фамилия',parse_mode='html', reply_markup=markup)
			bot.register_next_step_handler(message, dialog1)

def dialog1(message):
	global surname
	surname=message.text
	bot.send_message(message.from_user.id,'Ваше имя (и отчество, если имеется)')
	bot.register_next_step_handler(message, dialog2)

	

def dialog2(message):
	global name
	name=message.text 
	bot.send_message(message.from_user.id,'Серия паспорта (1 буква, 7-8 цифр, например: A12345678)')
	bot.register_next_step_handler(message, dialog3)

	

def dialog3(message):
	global passport_number
	passport_number=message.text
	if len(passport_number)>9:
		bot.send_message(message.from_user.id,f"Пожалуйста, введите данные правильно (Показано на примере)")
		bot.register_next_step_handler(message, dialog2)
	else:
		bot.send_message(message.from_user.id,'Ваш номер телефона (+992 ---------)')
		bot.register_next_step_handler(message, dialog4) 
		
	
	

def dialog4(message):
	global phone_number
	phone_number=message.text 
	if len(passport_number)>9:
		bot.send_message(message.from_user.id,f"Пожалуйста, введите данные правильно (Показано на примере)")
		bot.register_next_step_handler(message, dialog3)
	else:
		bot.send_message(message.from_user.id,"""Ваш регион проживания (пожалуйста, введите номер вашего региона)
1 - город Худжанд
2 - город Кайраккум
3 - город Чкаловск
4 - Бободжон-Гафуровский район
5 - Джаббар-Расуловский район
6 - Истаравшанский район
7 - Канибадамский район
8 - Спитаменский район
9 - район А.Сино
10 - район И.Сомони
11 - район Фирдавси
12 - район Шохмансур""")
	bot.register_next_step_handler(message, dialog5)

def dialog5(message):
	global region
	region=message.text 
	if len(region)>1:
		bot.send_message(message.from_user.id,f"Пожалуйста, введите данные правильно (Показано на примере)")
		bot.register_next_step_handler(message, dialog4)
	else:
		bot.send_message(message.from_user.id,'Дата рождения (дд.мм.гггг)')
		bot.register_next_step_handler(message, dialog6)

def dialog6(message):
	global birthday
	birthday=message.text
	if len(region)>10:
		bot.send_message(message.from_user.id,f"Пожалуйста, введите данные правильно (Показано на примере)")
		bot.register_next_step_handler(message, dialog5)
	else:
		bot.send_message(message.from_user.id,'Введите ваш номер ИНН (8-9 цифр)')
		bot.register_next_step_handler(message, dialog7)

def dialog7(message):
	global INN
	INN=message.text 
	if len(INN)>9:
		bot.send_message(message.from_user.id,f"Пожалуйста, введите данные правильно (Показано на примере)")
		bot.register_next_step_handler(message, dialog6)
	else:
		bot.send_message(message.from_user.id,"""Выберите пол:
1 - Мужской
2 - Женский""")
		bot.register_next_step_handler(message, dialog8)

def dialog8(message):
	global pol
	pol=message.text 
	bot.send_message(message.from_user.id,'Ваша электронная почта (если у вас нет, просто напишите "нет")')
	bot.register_next_step_handler(message, dialog9)

def dialog9(message):
	global mail
	mail=message.text 
	bot.send_message(message.from_user.id,'Ваши ежемесячные доходы (TJS) (включая дополнительный доходы, введите только цифры)')
	bot.register_next_step_handler(message, dialog10)

def dialog10(message):
	global doxod
	doxod=message.text 
	bot.send_message(message.from_user.id,'Ваши ежемесячные расходы (TJS) (Введите только цифры)')
	bot.register_next_step_handler(message, dialog11)

def dialog11(message):
	global rasxod
	rasxod=message.text 
	bot.send_message(message.from_user.id,'Ваш адрес фактического проживания (район, улица, дом)')
	bot.register_next_step_handler(message, dialog12)

def dialog12(message):
	global address
	address=message.text 
	db_table_val(surname=surname,name=name,passport_number=passport_number,number_phone=phone_number,region=region,birthday=birthday,INN=INN,pol=pol,mail=mail,doxod=doxod,rasxod=rasxod,address=address)

	bot.send_message(message.from_user.id,"""Согласны ли вы на проверку ваших данных в КИБТ и обработку персональных данных? 
http://mcf-imon.tj/policy.php""")


def db_table_val(surname:str,name: str,passport_number=str,number_phone=str,region=str,birthday=str,INN=str,pol=str,mail=str,doxod=str,rasxod=str,address=str):
	sql="INSERT INTO users(surname,name,passport_number,number_phone,region,birthday,INN,pol,mail,doxod,rasxod,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=[(surname,name,passport_number,number_phone,region,birthday,INN,pol,mail,doxod,rasxod,address)]
	cursor=connection.cursor()
	cursor.executemany(sql,val)
	connection.commit()
bot.polling(none_stop=False)