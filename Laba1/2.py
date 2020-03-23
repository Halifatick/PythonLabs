# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».

data = [2, 3, 5, 4, 6]
result = "True"
for i in data:
    print(i)
for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        result = "False"
        break
print(result)
