# Напишите скрипт, который разделяет введенный с клавиатуры текст на
# слова и выводит сначала те слова, длина которых превосходит 7
# символов, затем слова размером от 4 до 7 символов, затем – все
# остальные

txet = input('Введите текст: ').replace('.', '').replace(',', '').split(' ')
our_txet = [print(i) for i in [print(i) if(i is not None and 3 < len(i) < 8) else i for i in [print(i) if len(i) > 6 else i for i in txet]] if i is not None and len(i) < 4]

