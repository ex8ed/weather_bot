# -*- coding: utf-8 -*-
"""
Главный скрипт бота.
Вызывает все необходимые функции и модули.
"""
from telebot import *
from random import randint
import addIMG  # картинка города из поиска
import config  # токен и URL
import dataFind  # поисковый движок
import yandexReq  # запрос на сервер
import checkInput  # функции проверки
import sysMessages  # служебные сообщения

# CLIENT
client = TeleBot(config.token)

# KEYBOARD
keyboard = types.InlineKeyboardMarkup()
weather_b = types.InlineKeyboardButton(text='Узнать погоду ☁',
                                       callback_data='wantweather')
help_b = types.InlineKeyboardButton(text='Помощь 🆘',
                                    callback_data='help')
keyboard.add(weather_b, help_b)


# COMMANDS:
@client.message_handler(commands=['start'])
def startMessage(message):
    """
    Функция, отвечающая за приветствие при первом запуске.
    :param message:
    :return:
    """
    ID = message.chat.id
    client.send_message(ID, sysMessages.startMessage,
                        reply_markup=keyboard)
    pass


# CALLBACK:
@client.callback_query_handler(func=lambda call: call.data == 'help')
def sendHelp(call):
    """
    Функция, отвечающая за справку по клавише "help".
    Выводит сообщение краткой справки, если в очереди присутствует соответствующая клавиша.
    :param call:
    :return:
    """
    ID = call.message.chat.id
    client.send_message(ID, sysMessages.helpMessage,
                        reply_markup=keyboard)
    pass


@client.callback_query_handler(func=lambda call: call.data == 'wantweather')
def helloFunc(call):
    """
    Функция, отвечающая за взаимодействие с клавишей "wantweather".
    Вызывает функцию поиска, если в очереди присутствует соответствующая клавиша.
    :param: call
    :return:
    """
    ID = call.message.chat.id
    mess = client.send_message(ID,
                               'Привет! Пришли мне свой город в следующем сообщении.')
    client.register_next_step_handler(mess, enterCity)
    pass


def enterCity(message):
    """
    Функция c главным алгоритмом.
    Получает в параметры объект с сообщением, из которого
    вытаскивает город для поиска
    :param: message
    :return:
    """
    ID = message.chat.id
    info = message.text
    #   info - главное взаимодействие пользователя с программным интерфейсом:
    #   ВВЕДЕННЫЙ ГОРОД
    if checkInput.isCorrect(info):
        client.send_message(ID, 'Понял, ищу погоду по городу %s.' % info)
        lat, lon, isFound = dataFind.getCords(info)
        if isFound is True:
            answer = yandexReq.getForecast(lat, lon, info)
            client.send_photo(ID, addIMG.getImage(info))
            client.send_message(ID, answer,
                                reply_markup=keyboard)
        else:
            client.send_message(ID, 'Увы, такого города не нашлось. Вывожу по МСК.')
            info = 'Москва'
            answer = yandexReq.getForecast(lat, lon, info)
            client.send_message(ID, answer,
                                reply_markup=keyboard)
    else:
        mess = client.send_message(ID, 'Название города должно быть корректным!')
        client.register_next_step_handler(mess, enterCity)
        return


@client.message_handler(content_types=['text'])
def thanks(message):
    """
    Функция ответа на выражение благодарности.
    :param message:
    :return:
    """
    ID = message.chat.id
    thnx = message.text.lower()
    if checkInput.isItThanks(thnx):
        client.send_message(ID, 'Пожалуйста! 😊')
        client.send_sticker(ID,
                            config.stickersID[randint(0, 6)])


if __name__ == "__main__":
    client.polling(none_stop=True, interval=1)
