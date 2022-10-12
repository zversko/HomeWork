# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from curses.ascii import isdigit
import re
from sympy import true


def sum_digits(s):
    if s.isdigit():
        return True
    else:
        return False

def Main():
    s = str(input('Введите число вещественное число - '))
    num = list(filter(sum_digits, s))
    num = [int(i) for i in num]
    print(num)
    print(sum(num))
   
Main()