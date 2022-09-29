# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def create_list():
    print('С клавиатуры введите список элементов, по окончанию ввода нажмите Enter')
    list = []
    while True:
        try:
            list.append(int(input('> ')))
        except:
            break
    return list

def mult_pair_numbers(list):
    size = len(list)
    mult_pair_numbers_list = []
    while size != 0:
        if size == 1:
            mult = list[0] ** 2
            list.pop(0)
        else:
            mult = list[0] * list[size - 1]
            list.pop(size - 1), list.pop(0)
        mult_pair_numbers_list.append(mult)
        size = len(list)
    return mult_pair_numbers_list
    

def main():
    list = create_list()
    print(list)
    print(f'Произведение пар списка = {mult_pair_numbers(list)}')

main()