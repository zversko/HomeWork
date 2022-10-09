# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from codecs import utf_8_encode
from random import randint

def input_number():                             # Вводим максимальную степень многочлена
    print('Введите натуральное число')
    try:
        number = int(input('> '))
    except:
        exit()
    return number

def create_coefficient_and_write_in_file(num):  # Генерируем коэффициенты и перемножаем с иксами, потом записываем в файл
    for j in range (0,100):
        list = []
        for i in range (0,num+1):
            koeff = randint(0, 100)
            str(koeff)
            list.append(koeff)
        
        stroka = ' = 0'
        for i in range (0,num+1):
            if list[i] != 0 and i == 0:
                stroka = str(list[0]) + stroka
            elif list[0] == 0 and i == 1 and list[i] != 0:
                stroka = str(list[i]) + '*x' + stroka
            elif list[0] == 0 and i == 1 and list[i] == 0:
                stroka = stroka
            elif list[i] == 0:
                stroka = stroka
            elif i == 1 and list[i] != 1:
                stroka = str(list[i]) + '*x' + ' + ' + stroka
            elif i == 1 and list[i] == 1:
                stroka = 'x' + ' + ' + stroka
            elif list[i] == 1:
                stroka = 'x^' + str(i) + ' + ' + stroka
            else:
                stroka = str(list[i]) + '*x^' + str(i) + ' + ' + stroka

        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(stroka + '\n')    

def main():
    number = input_number()
    list = create_coefficient_and_write_in_file(number)

main()
