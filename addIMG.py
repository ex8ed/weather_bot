# -*- coding: utf-8 -*-
import os
import requests
import config

# change for your directory!
os.chdir("../miem_weather")


def getImage(info):
    """
    Функция находит фото по запросу
    и возаращает его URL.
    :param info:
    :return: URL
    """
    # city = info.lower().strip()
    URL = "https://api.unsplash.com/photos/random/?client_id=%s" \
          % config.unsplashKey
    cityIMG = requests.get(URL)
    try:
        return cityIMG.json()['links']['download']
    except IndexError:
        return config.LINK404
