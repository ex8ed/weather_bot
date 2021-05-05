# -*- coding: utf-8 -*-

import config


def forecastGenerator(info, dCurrent):
    """
    Функция получает на вход словарь и возвращает
    кортеж, который содержит ответы на поля, которые
    выделены по умолчанию в файле sysMessages
    """
    if dCurrent['fact']['is_thunder']:
        thunder = 'Ой, кажется будет гроза.. Возьмите зонт!☂⛈'
    else:
        thunder = 'Грозным быть нужды нет - гроза не ожидается!🌤'
    return (dCurrent['forecasts'][0]['date'],
            info,  # наименование населенного пункта из ввода
            dCurrent['geo_object']['locality']['name'],
            dCurrent['geo_object']['province']['name'],
            thunder,
            # утро
            config.conditions[dCurrent['forecasts'][0]['parts']['morning']['condition']],
            dCurrent['forecasts'][0]['parts']['morning']['temp_avg'],
            dCurrent['forecasts'][0]['parts']['morning']['feels_like'],
            dCurrent['forecasts'][0]['parts']['morning']['temp_min'],
            dCurrent['forecasts'][0]['parts']['morning']['temp_max'],
            dCurrent['forecasts'][0]['parts']['morning']['pressure_mm'],
            dCurrent['forecasts'][0]['parts']['morning']['prec_prob'],
            dCurrent['forecasts'][0]['parts']['morning']['humidity'],
            dCurrent['forecasts'][0]['parts']['morning']['wind_speed'],
            dCurrent['forecasts'][0]['parts']['morning']['wind_gust'],
            config.windDirection[dCurrent['forecasts'][0]['parts']['morning']['wind_dir']],
            # день
            config.conditions[dCurrent['forecasts'][0]['parts']['day']['condition']],
            dCurrent['forecasts'][0]['parts']['day']['temp_avg'],
            dCurrent['forecasts'][0]['parts']['day']['feels_like'],
            dCurrent['forecasts'][0]['parts']['day']['temp_min'],
            dCurrent['forecasts'][0]['parts']['day']['temp_max'],
            dCurrent['forecasts'][0]['parts']['day']['pressure_mm'],
            dCurrent['forecasts'][0]['parts']['day']['prec_prob'],
            dCurrent['forecasts'][0]['parts']['day']['humidity'],
            dCurrent['forecasts'][0]['parts']['day']['wind_speed'],
            dCurrent['forecasts'][0]['parts']['day']['wind_gust'],
            config.windDirection[dCurrent['forecasts'][0]['parts']['day']['wind_dir']],
            # вечер
            config.conditions[dCurrent['forecasts'][0]['parts']['evening']['condition']],
            dCurrent['forecasts'][0]['parts']['evening']['temp_avg'],
            dCurrent['forecasts'][0]['parts']['evening']['feels_like'],
            dCurrent['forecasts'][0]['parts']['evening']['temp_min'],
            dCurrent['forecasts'][0]['parts']['evening']['temp_max'],
            dCurrent['forecasts'][0]['parts']['evening']['pressure_mm'],
            dCurrent['forecasts'][0]['parts']['evening']['prec_prob'],
            dCurrent['forecasts'][0]['parts']['evening']['humidity'],
            dCurrent['forecasts'][0]['parts']['evening']['wind_speed'],
            dCurrent['forecasts'][0]['parts']['evening']['wind_gust'],
            config.windDirection[dCurrent['forecasts'][0]['parts']['evening']['wind_dir']]
            )
