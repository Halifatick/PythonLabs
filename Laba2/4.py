# Напишите скрипт, который позволяет ввести с клавиатуры имя
# текстового файла, найти в нем с помощью регулярных выражений все
# подстроки определенного вида, в соответствии с вариантом.
# Вариант 9: найдите все донецкие почтовые индексы – подстроки вида
# «83000, Донецк» (первые 2 символа строго закреплены: «83»)

import re  # либа для регулярок

# начинается с 83, остальные 3 цифры не важны, дальше должна быть запятая и название города, до пробела

pattern1 = re.compile(r'\([0-9]{3}\)\d{3}-\d{2}-\d{2}')
pattern2 = re.compile(r'\([0-9]{3}\)[0-9]{7}')
content = ''
matches = []
path = input('Введите название вашего файла: ')
try:
    file = open('.\\' + path, 'r', encoding='UTF-8')
    content = file.read().replace('\n', ' ')
    file.close()
except FileNotFoundError as e:
    print('Файл не найден. ', e.args)

print(content)

result = re.findall(pattern1, content)
result.append(re.findall(pattern2, content))
print(result)
