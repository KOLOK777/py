# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

list_len = int(input('Введите количество элементов: \n'))
list_input = [random.randint(0, 5) for i in range(list_len)]
print('Получился список: ', list_input)
repeat_element = int(input('Введите интересующее вас число: \n'))
count = 0
for i in range(list_len):
    if list_input[i] == repeat_element:
        count += 1
print(f'Число {repeat_element} встречается списке {count} раз(а). ')
