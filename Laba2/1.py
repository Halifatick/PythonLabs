# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.


with open('task1.txt', 'r') as file:  # открытие файла, 'r' - открытие для чтения
    txet = file.read()  # считка в строку всего файла
s = '!@#№$%^&*(),.:;?/|"[]+_-'
vocabulary = {letter: txet.count(letter) for letter in txet if letter not in s}
for key in sorted(vocabulary.keys(), key=vocabulary.get, reverse=True):
    print(key, ': ', vocabulary[key])