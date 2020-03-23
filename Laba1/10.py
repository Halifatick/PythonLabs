# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.

import string


password = input('Введите пароль: ')
pass_safety = 0
if password.islower() or password.isupper() or password is "":
    print('Ваш парол очень плахой, ухадите')
    exit(0)

if 8 < len(password) < 16:
    pass_safety += 8
elif 6 < len(password) < 8:
    pass_safety += 6

for i in password:
    if i in string.ascii_uppercase or i.isdigit():
        pass_safety += 1

print('Сложность вашего ПАРОЛ\'ЬЯ: ', pass_safety)

