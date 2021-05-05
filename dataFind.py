# -*- coding: utf-8 -*-

from pandas import read_excel
from os import chdir


def getCords(info):
    """
    Функция getCords на вход получает название города
    и из базы данных data_RU вычленяет географические
    координаты, возвращаемые в виде кортежа (lat, lon),
    а также индикатор выполнения алгоритма
    По умолчанию - координаты МСК.
    :param info:
    :return:
    """
    city = info.lower().strip()
    chdir('C:/Users/Nick/Documents/miem_weather')
    path = './data/data_wT15_%s.xlsx'
    data_ = read_excel(path % city[0])

    try:
        index = data_.loc[data_['city'] == city].index[0]
        isFound = True
        lat = data_.iloc[index]['lat']
        lon = data_.iloc[index]['lon']
        return float(lat), float(lon), isFound
    # ошибка нахождения города
    except IndexError:
        lat = 55.558741
        lon = 37.378847
        isFound = False
        return float(lat), float(lon), isFound
    # ошибка формата ячейки:
    except ValueError:
        lat = 55.558741  # кординаты МСК
        lon = 37.378847
        isFound = False
        return float(lat), float(lon), isFound
