# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
#
# for x in frange(1, 5, 0.1):
# print(x)
# выводит 1 1.1 1.2 1.3 1.4 … 5.0


def frange(otkuda, posledniy, shag):
    while otkuda <= posledniy:
        yield round(otkuda, 1)  # округление до десятых
        otkuda += shag


for z in frange(3, 6, 0.2):
    print(z)

# yield - возвращает значение без выхода из функции, или что-то в этом роде
