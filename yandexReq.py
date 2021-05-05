# -*- coding: utf-8 -*-

import requests
import config
import sysMessages
import parserJSON


def getForecast(lat, lon, info):
    """Функция getForecast отправляет запрос на сервер,
    который в обработанном виде возвращается в виде строки.
    Примитивный парсер вычленяет нужную информацию из json."""
    params = {'lat': lat,
              'lon': lon,
              'lang': 'ru_RU',
              'limit': 1,
              'hours': False,
              'extra': True,
              }
    current = requests.get(config.address,
                           params=params,
                           headers=config.YandexAPIKey)
    # полученные с сервера значения в формате dict:
    dCurrent = current.json()
    conditions = parserJSON.forecastGenerator(info, dCurrent)
    return sysMessages.answer % conditions
