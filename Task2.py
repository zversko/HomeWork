# Создайте программу для игры в "Крестики-нолики".

from select import select
from os import system

def new_board(board):       # Рисуем доску
    print ("-------------")
    for i in range(3):
        print ("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print ("-------------")

def play_game(board):       # Заполняем клетки + или o       
    count = 0
    while True:             # Проверка ввода на число и на выигрышь
        new_board(board)
        if check_winner(board) == 1:
            print('Выиграли > ' + choiceXorO(count-1) + '-ки')
            break
        cell_select = input('Выберите клетку для ' + choiceXorO(count) + ' > ')
        try:
            cell_select = int(cell_select)
        except:
            system("cls")
            print('Это не число')
            continue
        while True:         # Проверка ввода на допустимое число и заполнение
            if 1 <= cell_select <= 9:
                if board[cell_select-1] != '+' and board[cell_select-1] != 'о':
                    board[cell_select-1] = choiceXorO(count)
                    count += 1
                    system("cls")
                    break
                else:
                    system("cls")
                    print('Клетка уже занята')
                    break
            else:
                system("cls")
                print('Ведите число от 1 до 9')
                break

def check_winner(board):    # Проверка выигрышных позиций
    winner_position = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winner_position:
        if (board[i[0]] == board[i[1]]) and (board[i[0]] == board[i[2]]):
            return 1

def choiceXorO(count):     
    if count % 2 == 0:
        return '+'
    else:
        return 'о'

def main():
    board = [x for x in range(1,10)]
    play_game(board)

main()