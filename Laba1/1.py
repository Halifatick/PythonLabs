#  Напишите скрипт, который преобразует введенное с клавиатуры
# вещественное число в денежный формат. Например, число 12,5 должно
# быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
# отрицательного числа выдайте сообщение «Некорректный формат!»

number = float(input('Введенное с клавиатуры вещественное число: '))  # ввод числа в num и преобразование строки во float
if number >= 0:
    print(int(number), 'руб. ', round((number - int(number)) * 100), ' коп.')  # целая часть числа + копейки
elif number < 0:  # elif = else if
    print('Некорректный формат!')
