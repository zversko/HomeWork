# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list_frac_part():
    print('С клавиатуры введите список элементов, по окончанию ввода нажмите Enter(округление до 100 долей)')
    list = []
    list_frac_part = []
    while True:
        try:
            a = abs(float(input('> ')))
            list.append(a)
            a = int((a - int(a)) * 100)
            list_frac_part.append(a)
        except:
            break
    print(list)
    return list_frac_part

def diff_max_min(list):
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]
    diff_max_min = max - min
    return diff_max_min

def main():
    list = create_list_frac_part()
    print(f'Разница между максимальным и минимальным значением дробной части элементов = {diff_max_min(list)}')

main()