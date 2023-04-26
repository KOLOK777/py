# Задача 30: Заполните массив элементами арифметической # прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
#     an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def progress(a, b, c):
    progress_list = []
    for i in range(a, a + (c - 1) * b + 1, b):
        progress_list.append(i)
    return progress_list

while True:
    try:
        first_element = int(input('Введите первый элемент: '))
        break
    except ValueError:
        print('Введите целое число !')
while True:
    try:
        difference_element = int(input('Введите разность элементов: '))
        if difference_element <= 0:
            raise Exception
        break
    except ValueError:
        print('Введите целое число !')
    except Exception:
        print('Требуется положительное число !')
while True:
    try:
        number = int(input('Введите количество элементов: '))
        if number <= 0:
            raise Exception
        break
    except ValueError:
        print('Введите целое число !')
    except Exception:
        print('Требуется положительное число !')

list_final = progress(first_element, difference_element, number)
print(f'Получился массив: {list_final}')