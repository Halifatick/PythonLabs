import os
from glob import glob
import os.path
# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен


"""
Короче, в винде нельзя в имени файла использовать двоеточие. Я долбился с этим две недели.
Поэтому двоеточие заменил на нижнее подчёркивание и пусть будет так.
"""

path = ".\\Music"
os.chdir(path)

# trackFiles = list(filter(None, [None if i == 'fileLists.txt' else i for i in os.listdir(path)]))
trackFiles = glob('*.mp3')

namesFiles = list(filter(None, [text.replace('\n', '') if text is not 'fileLists.txt' else None for text in
                                open('fileLists.txt', 'r', encoding='UTF-8')]))

cnt = 0
Done = False

for i in range(len(trackFiles)):
    try:
        os.rename(trackFiles[i], namesFiles[i])
        if cnt == len(trackFiles) - 1:
            Done = True
        cnt += 1
    except Exception as e:
        print('Ошибки с файлами #' + str(cnt) + ': ', e.args)

if Done:
    print('Все файлы переименованы!')
else:
    print('У нас проблемы, Хьюстон!')
