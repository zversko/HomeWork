# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list():
    print('С клавиатуры введите список элементов, по окончанию ввода нажмите Enter')
    list = []
    while True:
        try:
            list.append(int(input('> ')))
        except:
            break
    return list

def sum_odd(list):
    sum = 0
    for i in range(0, len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum
    

def main():
    list = create_list()
    print(list)
    print(f'Сумма элементов расположенных на нечетных позициях = {sum_odd(list)}')

main()