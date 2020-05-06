import string
import re

"""

Напишите простой класс StringFormatter для форматирования строк со
следующим функционалом:
– удаление всех слов из строки, длина которых меньше n букв;
– замена всех цифр в строке на знак «*»;
– вставка по одному пробелу между всеми символами в строке;
– сортировка слов по размеру;
– сортировка слов в лексикографическом порядке.
Примечание. Разделители слов можно задавать отдельно. По
умолчанию в качестве разделителя принимается только символ
пробела

"""


class StringFormatter(object):
    separator = [' ']

    def __init__(self, line):
        self._line = line

    def delete_by_n(self, n):
        temp = []
        words = self._line.split(' ')
        for i in range(len(words)):
            if len(words[i]) < n:
                temp.append(words[i])
        return ' '.join(temp)

    def replace_digits(self):
        return re.sub('\d', '*', self._line)

    def insert_spaces(self):
        tmp = list(self._line)
        return " ".join(tmp)

    def sort_by_size(self):
        words = self._line.split()
        return ' '.join(sorted(words, key=lambda word: len(word)))

    def sort_by_lec(self):
        words = self._line.split()
        return ' '.join(sorted(words))


sentence = 'Привет это дистанцон0чка'

obj = StringFormatter(sentence)
print('Начальная строка: ', sentence, end='\n')
print('Строка, где были удалены все слова, длинна которых меньше 6 символов: ', obj.delete_by_n(6), end='\n')
print('Строка, где все цифры были заменены на символ \'*\': ', obj.replace_digits(), end='\n')
print('Строка, где между всеми символами был поставлен пробел \' \': ', obj.insert_spaces(), end='\n')
print('Строка, которая была отсортирована по размеру слов: ', obj.sort_by_size(), end='\n')
print('Строка, которая была отсортирована лексикографически: ', obj.sort_by_lec(), end='\n')
