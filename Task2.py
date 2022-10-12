# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def mult_numbers(n):
    mult_list = []
    i = 1
    j = 1
    while i <= n:
        mult_list.append(i * j)
        j = j * i
        i = i + 1
    return mult_list

def Main():
    number = float(input('Введите число - '))
    print(f'Произведение чисел от 1 до N = {mult_numbers(number)}')
   
Main()