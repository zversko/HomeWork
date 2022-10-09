# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_simple_mult(n):                                # Поиск всех простых чисел в промежутке [0,N]
    simple_list = []
    for i in range(2, int(n / 2) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:                                           # Отлавливаем числа, которые не имеют делителей
            if n % i == 0:
                n = n / i
                simple_list.append(i)
    return simple_list

def main():
    num = int(input('Ведите натуральное число - '))
    simple_list = find_simple_mult(num)
    if len(simple_list) > 0:
        print(f'Число {num} имеет простые множители:') 
        print(simple_list)
    else:
        print(f'Число {num} является простым...') 

main()

