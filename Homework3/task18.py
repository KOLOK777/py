# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random, math

list_len = int(input('Введите количество элементов: '))
list_input = [random.randint(0, 5) for i in range(list_len)]
print('Получился список: ', list_input)
compare_element = int(input('Введите интересующий вас элемент: '))
closest_element = max(list_input)
for i in range(len(list_input)):
    if abs(compare_element - list_input[i]) < abs(closest_element - list_input[i]):
        closest_element = list_input[i]
print(f'Ближайший к заданному элемент: {closest_element}')
