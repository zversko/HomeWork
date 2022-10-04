# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def covert_dec_to_bin():
    dec = int(input())
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

def main():
    print('Введите десятичное число > ')
    bin = covert_dec_to_bin()
    print(f'В двоичной системе счисления > {bin}')

main()
