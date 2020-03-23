# Напишите скрипт, который на основе списка из 16 названий
# футбольных команд случайным образом формирует 4 группы по 4
# команды, а также выводит на консоль календарь всех игр (игры
# должны проходить по средам, раз в 2 недели, начиная с 14 сентября
# текущего года). Даты игр необходимо выводить в формате «14/09/2016,
# 22:45». Используйте модуль random.

from random import shuffle  # смешивание комада
import itertools
import time
from time import strftime
from datetime import timedelta, datetime

format = "%H:%M, %d/%m/%Y"
start = datetime.strptime("22:05, 14/09/2019", format)
teams = ["Barcelona",
         "Real Madrid",
         "PSG",
         "Liverpool",
         "Atletico Madrid",
         "Juventus",
         "Manchester City",
         "Tottenham",
         "Bayern Munich",
         "Shakhtar",
         "Napoli",
         "Inter",
         "Lion",
         "Zenit",
         "Chelsea",
         "Valencia"]
shuffle(teams)  # смешивание команд (из рандома)
teams = [teams[i*4: i*4+4] for i in range(0, 4)]
games = []
for t in teams:
    games.append([c for c in itertools.combinations(t, 2)])
for i in range(0, 6):
    print("День матча: ", end='')
    print(start.strftime(format))
    print("Номер матча: ", i + 1)
    print(games[0][i])
    print(games[1][i])
    print(games[2][i])
    print(games[3][i])
    start = start + timedelta(days=14)
print('\n', start.strftime(format), "Чемпионат закончился !!!")