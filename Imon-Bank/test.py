import sqlite3
import telebot

bot = telebot.TeleBot("5151249056:AAFS6LkG5VlBvv_dpblIoRvmsWQK3VU21Vo")

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
        
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


bot.polling(none_stop=True)
"""import telebot

bot = telebot.TeleBot("2145763251:AAH7lMEcX1jcr-4Y44FzHq7dGIUYdwF2oXk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "55.75376167")

bot.infinity_polling()"""
"""
import random
list_word=["СЧАСТЛИВЫЙ", "ДВЕРЬ", "КАМЕНЬ", "НАУШНИК"]
count=8



for i in range(len(list_word)):
    print(list_word[i])
print()
random_word=list_word[random.randint(0,len(list_word)-1)]
print(random_word)

print()
for letters in range(len(random_word)):
    print("-",end='')
print()
print(f"У вас осталось {count} догадок")

print()
print()
for r in random_word:
    a=input("Введите здесь одну букву, затем нажмите Enter:")
    if(random_word[letters]==a):
        print("Yes")
    else:
        print("No")"""
"""
import cv2

cap=cv2.VideoCapture(0);

while(True):
    ret, frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()"""
# Подключение всех необходимых библиотек
# Нам нужно: speech_recognition, os, sys, webbrowser
# Для первой бибилотеки прописываем также псевдоним
"""import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import subprocess



t=pyttsx3.init()


# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
    print(words) # Дополнительно выводим на экран
    os.system(" :" + words) # Проговариваем слова

# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером
talk("Привет, чем я могу помочь вам?")


    Функция command() служит для отслеживания микрофона.
    Вызывая функцию мы будет слушать что скажет пользователь,
    при этом для прослушивания будет использован микрофон.
    Получение данные будут сконвертированы в строку и далее
    будет происходить их проверка.
def command():
    # Создаем объект на основе библиотеки
    # speech_recognition и вызываем метод для определения данных
    r = sr.Recognizer()

    # Начинаем прослушивать микрофон и записываем данные в source
    with sr.Microphone() as source:
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
        r.pause_threshold = 1
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)

    try: # Обрабатываем все при помощи исключений
        
        Распознаем данные из mp3 дорожки.
        Указываем что отслеживаемый язык русский.
        Благодаря lower() приводим все в нижний регистр.
        Теперь мы получили данные в формате строки,
        которые спокойно можем проверить в условиях
        
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        # Просто отображаем текст что сказал пользователь
        print("Вы сказали: " + zadanie)
    # Если не смогли распознать текст, то будет вызвана эта ошибка
    except sr.UnknownValueError:
        # Здесь просто проговариваем слова "Я вас не поняла"
        # и вызываем снова функцию command() для
        # получения текста от пользователя
        talk("Я вас не поняла")
        zadanie = command()

    # В конце функции возвращаем текст задания
    # или же повторный вызов функции
    return zadanie

# Данная функция служит для проверки текста, 
# что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
    # Попросту проверяем текст на соответствие
    # Если в тексте что сказал пользователь есть слова
    # "открыть сайт", то выполняем команду
    if 'открыть сайт' in zadanie:
        # Проговариваем текст
        talk("Уже открываю")
        # Указываем сайт для открытия
        url = 'https://google.com'
        # Открываем сайт
        webbrowser.open(url)
    # если было сказано "стоп", то останавливаем прогу
    elif 'hello' in zadanie:
        print("hello")

    elif 'телеграм' or 'telegram' in zadanie:
        subprocess.call('D:/Programs/Sublime Text/sublime_text.exe')
    elif 'стоп' in zadanie:
        # Проговариваем текст
        talk("Да, конечно, без проблем")
        # Выходим из программы
        sys.exit()
    # Аналогично
    elif 'имя' in zadanie:
        talk("Меня зовут Сири")

    t.runAndWait()

# Вызов функции для проверки текста будет 
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
    makeSomething(command())"""


"""
import cv2
import numpy as np

#################################
widthImg=640
heightImg=480
################################

img=cv2.imshow('20220522_084722.jpg',0)


def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,200,200)
    kernel=np.ones((5,5))
    imgDial=cv2.dilate(imgCanny, kernel,iterations=2)
    imgThres=cv2.erode(imgDial,kernel,iterations=1)

    return imgThres

def getContours(img):
    biggest=np.array([])
    maxArea=0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx)==4:
                biggest=approx
                maxArea=area 
    return biggest


imgThres=preProcessing(img)
getContours(imgThres)
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
###########

"""

execute_query(connection, create_posts_table)
###########################
"""
"""
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#############################

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)

###################################

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

#################################

connection = create_connection("localhost", "root", "", "sm_app")


"""