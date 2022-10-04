# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibonacci(n):
    if (n==1 or n==2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def nega_fibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nega_fibonacci(n + 2) - nega_fibonacci(n + 1)

def main():
    list = [0]
    for i in range(1,int(input('Введите последний индекс числа Фибоначчи '))+1):
        list.insert(0, nega_fibonacci(-i))
        list.append(fibonacci(i))
    print(list)

main()
