# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

letter_value_list_eng_1 = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1', }
letter_value_list2_eng_2 = {'D': '2', 'G': '2'}
letter_value_list2_eng_3 = {'B': '3', 'C': '3', 'M': '3', 'P': '3'}
letter_value_list2_eng_4 = {'F': '4', 'H': '4', 'V': '4', 'W': '4', 'Y': '4'}
letter_value_list2_eng_5 = {'K': '5'}
letter_value_list2_eng_8 = {'J': '8', 'X': '8'}
letter_value_list2_eng_10 = {'Q': '10', 'Z': '10'}
letter_value_list_rus_1 = {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1'}
letter_value_list_rus_2 = {'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2'}
letter_value_list_rus_3 = {'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3'}
letter_value_list_rus_4 = {'Й': '4', 'Ы': '4'}
letter_value_list_rus_5 = {'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5'}
letter_value_list_rus_8 = {'Ш': '8', 'Э': '8', 'Ю': '8'}
letter_value_list_rus_10 = {'Ф': '10', 'Щ': '10', 'Ъ': '10'}

merged_value_list = {**letter_value_list_eng_1, **letter_value_list2_eng_2, **letter_value_list2_eng_3}
merged_value_list = {**merged_value_list, **letter_value_list2_eng_4, **letter_value_list2_eng_5}
merged_value_list = {**merged_value_list, **letter_value_list2_eng_8, **letter_value_list2_eng_10}
merged_value_list = {**merged_value_list, **letter_value_list_rus_1, **letter_value_list_rus_2}
merged_value_list = {**merged_value_list, **letter_value_list_rus_3, **letter_value_list_rus_4}
merged_value_list = {**merged_value_list, **letter_value_list_rus_5, **letter_value_list_rus_8}
merged_value_list = {**merged_value_list, **letter_value_list_rus_10}
print('Сформирован словарь ценности букв: ', merged_value_list)

word = input('Введите слово для подсчета суммы очков: \n')
word = word.upper()
summ = 0
for i in range(len(word)):
    summ += int(merged_value_list.get(word[i]))
print(f'Ваше слово набрало {summ} очков.')