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

def main():
    new_list = create_list()
    print(new_list)
    if len(new_list) == 0:
        print('Отсутствуют числовые элементы в списке')
        exit()
    new_list = [x for i, x in enumerate(new_list) if i == new_list.index(x)]
    print(new_list)
    
main()        
