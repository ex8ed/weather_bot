# -*- coding: utf-8 -*-
# contains answer string
answer = """Я нашел, я нашел! Смотри: 
Дата: %s , в городе %s (%s, %s) 
%s
  Утром ⛅:
В ближайшее время %s, температура за бортом: %d °С, ощущается как %d °С. 
Минимальная температура: %d °С, максимальная температура: %d °С.
Давление: %d мм. рт. ст.
Вероятность выпадения осадков: %d %%. Влажность %d %%
Скорость ветра: %d м/с, порывы могут достигать %d м/с.
Направление ветра %s.

  Днем ☀:
В ближайшее время %s, температура за бортом: %d °С, ощущается как %d °С.
Минимальная температура: %d °С, максимальная температура: %d °С.
Давление: %d мм. рт. ст.
Вероятность выпадения осадков: %d %%. Влажность %d %%
Скорость ветра: %d м/с, порывы могут достигать %d м/с.
Направление ветра %s.

  Вечером ✨:
В ближайшее время %s, температура за бортом: %d °С, ощущается как %d °С.
Минимальная температура: %d °С, максимальная температура: %d °С.
Давление: %d мм. рт. ст.
Вероятность выпадения осадков: %d %%. Влажность %d %%
Скорость ветра: %d м/с, порывы могут достигать %d м/с.
Направление ветра %s.
"""

# SYSTEM MESSAGES
############################

# contains "start" answer
startMessage = """Привет, я погодный бот! Нажми на соответствующую кнопку под сообщением, \
чтобы меня запустить. \n\
Если ты не знаешь, что делают кнопки, нажми клавишу "Помощь".
Можешь меня поблагодарить, если я помог тебе сэкономить время 👉🏻👈🏻..
"""

# contains "help" answer
helpMessage = """Вы вызвали команду получения краткой справки.\n\n\
Нажмите клавишу "Узнать погоду" для запуска основного алгоритма поиска погоды по наименованию города. \
База данных включает в себя множество российских и крупных зарубежных городов. \
Если я не нашел твой город, то по умолчанию выводится погода по МСК. \
"""