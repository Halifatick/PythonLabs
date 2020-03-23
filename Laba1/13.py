# Напишите собственную версию генератора enumerate под названием
# extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
#  print(elem, cum, frac)
#
# В переменной cum хранится накопленная сумма на момент текущей
# итерации, в переменной frac – доля накопленной суммы от общей
# суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
# вывод будет таким:
#  (1, 1, 0.1)   (3, 4, 0.4)     (4, 8, 0.8)     (2, 10, 1)

# element - текущий элемент
# asd  - сумма текущего элемента с суммой предыдущих элементов
# (fracion) - сумма всех элементов
# fract - доля накопленной суммы от общей суммы на момент текущей итерации.


def extra_enumerate(x):
    asd = 0
    fraction = 0
    for step in x:
        fraction += step
    for y in range(len(x)):
        element = x[y]
        asd += x[y]
        fract = asd / fraction
        yield y, element, asd, round(fract, 1)


x = [x for x in range(15)]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
