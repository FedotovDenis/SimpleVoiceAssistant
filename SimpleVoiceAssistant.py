import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):             # Создаем функцию которая будет выводить слова на экран
   engine = pyttsx3.init()
   engine.say(words)
   engine.runAndWait()

talk("Спроси меня что-либо")

def command():               # Функция которая будет слушать и понимать что говорят и будет переводить слова и выполнять действие
    r = sr.Recognizer()

    with sr.Microphone() as source:                # Открываем прослушивание с помощью оператора
        print("Говорите")                # Говорим пользовотелю что бы говорили
        r.pause_threshold = 1            # после вопроса с помощью этого метода ждем 1 секунду
        r.adjust_for_ambient_noise(source, duration=1)  # библиотека для того что бы не мешали фоновые звуки
        audio = r.listen(source)

        try:               # Выполняем команды с услышах слов пользователя
            zadanie = r.recognize_google(audio, language="ru-Ru").lower()
            print("Вы сказали " + zadanie)
        except sr.UnknownValueError:
            talk("Я Вас не понимаю")   # Если было не понятно задание
            zadanie = command()

        return zadanie                 # Возвращаем переменную задание

def makeSomething(zadanie):          # Эта функция выполняет услышанные задания
    if 'открыть сайт' in zadanie:
        talk("Выполняю задание")
        url = 'https://sefon.pro/genres/trance/'
        webbrowser.open(url)

    elif 'имя' in zadanie:          # узнаем имя
        talk("Меня зовут Сири")

    elif 'стоп' in zadanie:  # останавливает нашу программу
        talk("Да, конечно")
        sys.exit()

while True:                      # В бесконечном цыкле выполняем наше заданипе
    makeSomething(command())




