#  Напишите параметризированный декоратор pre_process, который
# осуществляет предварительную обработку (цифровую фильтрацию)
# списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
# коде (по умолчанию равен 0.97). Пример кода:

# @pre_process(a=0.93)
# def plot_signal(s):
#  for sample in s:
# print(sample)


# метод принимает значения a, но по дефолту равен =0.97
def pre_process(a=0.97):
    def decorator(function):
        def wrap(*args):  # * значит, что внутри args содержится 0 или более элементов с данными (wrap - Обёртка с аглийского)
            o = args[0]
            for i in range(1, len(o)):  # в диапазоне от 1 до длины аргумента
                o[i] = o[i] - a * o[i - 1]  # цифровая обработка по формуле задания
            print('a = ', a)
            function(o)  # вызывается сама функция, к которой применяется декторатор

        return wrap

    return decorator


@pre_process(a=0.98)  # вызывается декоратор для даной функции
def plot_signal(s):
    for sample in s:
        print(sample)


arr = [i for i in range(10)]  # генератор списка от 0 до 9
plot_signal(arr)  # типо наш main
