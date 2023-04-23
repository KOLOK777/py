# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def expo(n, m):
    if m > 0:
        if m == 1:
            return n
        return n * expo(n, m - 1)
    elif m == 0:
        return 1
    else:
        if m == -1:
            return n
        return expo(n, m + 1) / n
while True:
    try:
        basic_number = float(input("Введите целое число (база для степени): "))
        break
    except ValueError:
        print('Неверный ввод!')
while True:
    try:
        expon_number = int(input("Введите целое число (степень): "))
        break
    except ValueError:
        print('Неверный ввод!')
print('Результат вычислений: ', expo(basic_number, expon_number))