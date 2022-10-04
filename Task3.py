# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def create_list():                                   # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(числа), по окончанию ввода нажмите Enter')
    new_list = []
    while True:
        try:
            element = int(input('> '))
            float(element)
            new_list.append(element)
        except:
            break
    return new_list

def sort_bubble(sort_list):                          # Сортируем по возрастанию
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list)-i-1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list

def find_not_duplicated_numbers(list):               # Переносим все не повторяющиеся элементы в новый список
    not_duplicated_list = []
    list.append(None)
    list.insert(0, None)
    for i in range(1,len(list)-1):
        if list[i] != list[i+1] and list[i] != list[i-1]:
            not_duplicated_list.append(list[i])
    return not_duplicated_list

def main():
    new_list = create_list()
    print(new_list)
    if len(new_list) == 0:
        print('Отсутствуют числовые элементы в списке')
        exit()
    sort_list = sort_bubble(new_list)
    print(sort_list)
    double_list = find_not_duplicated_numbers(sort_list)
    print(double_list)
    
main()        
