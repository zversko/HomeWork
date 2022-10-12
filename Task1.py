# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum_digits(number):
    int_num = 0
    sum = 0
    while number != int_num:
        number = float(number * 10)
        int_num = int(number)
    number = int(number)
    while number != 0:
        ostatok = number % 10
        number = int(number / 10)
        sum = sum + ostatok
    return sum

def Main():
    number = float(input('Введите число вещественное число - '))
    print(f'Сумма цифр числа = {sum_digits(number)}')
   
Main()