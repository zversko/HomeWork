# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# import time
from random import randint

def choice_match():                 # Выбор спички рэндомно

    print('      __             ')
    print('     / /  @  @       ')
    print('    / /   |  |       ')
    print('   / /____|__|__     ')
    print('  /_____________)    ')
    print('  |_____________)    ')
    print('  |_____________)    ')
    print('  |_____________)    ')
    print('                     ')

    choice = input('Выберите спичку (Left or Right): ')[0].lower()
    match = int(randint(0, 2))
    
    if (choice == 'l' and match == 1) or (choice == 'r' and match == 0):
        return ('Ваш ход', 1)
    elif (choice == 'l' and match != 1) or (choice == 'r' and match != 0):
        return ('Ход компьютера', 0)
    elif (choice != 'l' or choice != 'r'):
        main()
        exit()

def choice_candy(choice):           # Прогон двух циклов:    
    all_sum_candy = 2021            # 1. Цикл, остаточная сумма выбора более 28
    max_move = 28                   # 2. Цикл, остаточная сумма выбора менее 28
    sum_all_move = 0                # Выбор хода компьютера или человека за счет 
    choice2 = 1 - choice            # переменных choice и choice2
    while sum_all_move <= all_sum_candy:
        if (all_sum_candy - sum_all_move) >= max_move:
            first_player = choice2 * randint(1, 27) # Выбор хода (человек/компьютер)
            if first_player == 0:
                while True:         # Цикл проверки допустимого ввода
                    first_player = int(input('Возьмите максимум 27 конфет '))
                    if 1 <= first_player <= (max_move - 1):
                        break
                    else:
                        True
            print('1-й - ', first_player)
            second_player = choice * randint(1, max_move - first_player)
            if second_player == 0:
                while True:         # Цикл проверки допустимого ввода
                    second_player = int(input(f'Возьмите максимум {max_move - first_player} конфет '))
                    if 1 <= second_player <= (max_move - first_player):
                        break
                    else:
                        True
            print('2-й - ',second_player)                
            sum_all_move = sum_all_move + first_player + second_player
            print('Забрали - ',sum_all_move, '\n')
        elif ((all_sum_candy - sum_all_move) <= max_move):
            first_player = choice2 * randint(1, all_sum_candy - sum_all_move)
            if first_player == 0:
                while True:         # Цикл проверки допустимого ввода
                    first_player = int(input(f'Возьмите максимум {all_sum_candy - sum_all_move} конфет '))
                    if 1 <= first_player <= (all_sum_candy - sum_all_move):
                        break
                    else:
                        True
            sum_all_move = sum_all_move + first_player
            print(f'1-й - {first_player}')
            if sum_all_move == all_sum_candy:
                print(f'Забрали - {sum_all_move}')
                return 1
            second_player = choice * randint(1, all_sum_candy - sum_all_move)
            if second_player == 0:
                while True:         # Цикл проверки допустимого ввода
                    second_player = int(input(f'Возьмите максимум {all_sum_candy - sum_all_move} конфет '))
                    if 1 <= first_player <= (all_sum_candy - sum_all_move):
                        break
                    else:
                        True
            sum_all_move = sum_all_move + second_player
            print(f'2-й - {second_player}')
            if sum_all_move == all_sum_candy:
                print(f'Забрали - {sum_all_move}')
                return 2
            print(f'2 = {sum_all_move}')


def main():
    (choice_str, choice_int) = choice_match()
    print(choice_str)
    print(f'The End, выгирал {choice_candy(choice_int)}-й игрок')



main()
