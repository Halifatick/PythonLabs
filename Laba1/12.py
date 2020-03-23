# Напишите генератор get_frames(), который производит «оконную
# декомпозицию» сигнала: на основе входного списка генерирует набор
# списков – перекрывающихся отдельных фрагментов сигнала размера
# size со степенью перекрытия overlap. Пример вызова:
# for frame in get_frames(signal, size=1024, overlap=0.5):
# print(frame)


def get_frames(beep, size, overlaps):
    shag = int(size * overlaps)  #
    start = 0
    while start < len(beep) - 1:
        yield beep[start: start + size]
        start += shag


signal = [i for i in range(40)]
print(signal)
print('\n')
for frame in get_frames(signal, 6, 0.8):
    print(frame)

# Перекрытие - это значение, на которое следующий лист будет заходить на пределы предыдущего(с округлением)
