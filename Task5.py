# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def read_polynom_in_list(file):                                         # Считывание многочлена из файла и перевод в список
    file = open(file, "r")
    s = file.readline()
    file.close()
    new_list = []
    new_list = s.split()
    new_list.pop(len(new_list) - 1), new_list.pop(len(new_list) - 1)    # Удаляем концовку
    i = 0
    while i < len(new_list):                                            # Добавляем минус к коэффициенту, если он есть
        if new_list[i] == '-':
            new_list[i+1] = new_list[i] + new_list[i+1]
            new_list.pop(i)
        elif new_list[i] == '+':
            new_list.pop(i)
        i = i + 1
    return new_list

def add_zero(with_zero_list):                                           # Добавление нулей в список, если коэффициенты нулевые
    while True:                                         
        try:
            int(with_zero_list[len(with_zero_list)-1])
            with_zero_list[len(with_zero_list)-1] = int(with_zero_list[len(with_zero_list)-1])
            break
        except:
            with_zero_list.append(0)
            break

    if with_zero_list[(len(with_zero_list)-2)].find('x^') != -1:
        with_zero_list.insert((len(with_zero_list)-1), '0')
    size = len(with_zero_list) - 1
    i = 0
    while i < size:
        char = 'x^' + str(2+i)
        if with_zero_list[(len(with_zero_list)-3-i)].find(char) == -1:
            with_zero_list.insert((len(with_zero_list)-2-i), '0')
        size = len(with_zero_list) - 2
        i = i + 1

    size = len(with_zero_list) - 1 
    i = 0
    while i < size:
        if with_zero_list[i] == '0':
            with_zero_list[i] = with_zero_list[i]
        elif with_zero_list[i].find('-x') != -1:
            with_zero_list[i] = '-1*' + with_zero_list[i].replace('-', '')
        elif with_zero_list[i].find('*x') == -1:
            with_zero_list[i] = '1*' + with_zero_list[i]
        i = i + 1
    
    return with_zero_list

def get_coefficients_without_X(coefficient_list):                         # Отделение коэффициентов от исков

    if coefficient_list[len(coefficient_list)-2] == '0':
        coefficient_list[len(coefficient_list)-2] = int(coefficient_list[len(coefficient_list)-2])
    else:
        coefficient_list[len(coefficient_list)-2] = int(coefficient_list[len(coefficient_list)-2].replace('*x', ''))
    size = len(coefficient_list) - 2 
    i = 0
    while i < size:
        if coefficient_list[i] == '0':
            coefficient_list[i] = int(coefficient_list[i])
        else:
            char = '*x^' + str(len(coefficient_list)-1-i)
            coefficient_list[i] = int(coefficient_list[i].replace(char, ''))
        i = i + 1
    return coefficient_list

def sum_polynom(list1, list2):                                              # Складываем коэффиценты многочленов
    if len(list1) >= len(list2):
        for i in range(0, len(list2)):
            list1[len(list1) - 1 - i] = list1[len(list1) - 1 - i] + list2[len(list2) - 1 - i]
        return list1
    else:
        for i in range(0, len(list1)):
            list2[len(list2) - 1 - i] = list2[len(list2) - 1 - i] + list1[len(list1) - 1 - i]
        return list2

def general_form_polynom(finish_list, file):                                # Составляем строку из коэффициентов и иксов
    finish_string = ' = 0'                                                  # И записываем в файл
    for i in range (0,len(finish_list)):
        if finish_list[len(finish_list) - 1 - i] != 0 and i == 0:
            finish_string = str(finish_list[len(finish_list) - 1 - i]) + finish_string
        elif finish_list[len(finish_list) - 1 - i] == 0 and i == 0:
            finish_string = '0' + finish_string
        elif finish_list[0] == 0 and i == 1 and finish_list[len(finish_list) - 1 - i] != 0:
            finish_string = str(finish_list[len(finish_list) - 1 - i]) + '*x' + finish_string
        elif finish_list[0] == 0 and i == 1 and finish_list[len(finish_list) - 1 - i] == 0:
            finish_string = finish_string
        elif finish_list[len(finish_list) - 1 - i] == 0:
            finish_string = finish_string
        elif i == 1 and finish_list[len(finish_list) - 1 - i] != 1:
            finish_string = str(finish_list[len(finish_list) - 1 - i]) + '*x' + ' + ' + finish_string
        elif i == 1 and finish_list[len(finish_list) - 1 - i] == 1:
            finish_string = 'x' + ' + ' + finish_string
        elif finish_list[len(finish_list) - 1 - i] == 1:
            finish_string = 'x^' + str(len(finish_list) - 1 - i) + ' + ' + finish_string
        elif finish_list[len(finish_list) - 1 - i] < 0:
            finish_string = '(' + str(finish_list[len(finish_list) - 1 - i]) + ')' + '*x^' + str(i) + ' + ' + finish_string
        else:
            finish_string = str(finish_list[len(finish_list) - 1 - i]) + '*x^' + str(i) + ' + ' + finish_string
    with open(file, 'a', encoding='utf-8') as file:
            file.write(finish_string + '\n')    
    

def main():
    polynom_1 = read_polynom_in_list('file.txt')
    polynom_1 = add_zero(polynom_1)
    polynom_1 = get_coefficients_without_X(polynom_1)
    print(f'Первый многочлен = {polynom_1}')
    polynom_2 = read_polynom_in_list('file2.txt')
    polynom_2 = add_zero(polynom_2)
    polynom_2 = get_coefficients_without_X(polynom_2)
    print(f'Первый многочлен = {polynom_2}')
    sum_polyn = sum_polynom(polynom_1, polynom_2)
    print(f'Сумма коэффициентов = {sum_polyn}')
    general_form_polynom(sum_polyn, 'file_sum.txt')

main()
