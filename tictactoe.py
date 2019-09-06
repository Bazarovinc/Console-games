# Игра крестики-нолики

import random


def draw_board(board):
    # Вывод игрового поля на экран.
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')


def input_player_letter():
    # Выбор игрока крестика или нолика
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Вы выбираете Х или О?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        elif letter == 'O':
            return ['O', 'X']


def who_goes_first():
    # Случайный выбор игрока,который одит первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    # С учетом заполнения поля, эта функция вернет True, если игрок выиграл
    return((bo[7] == le and bo[8] == le and bo[9] == le) or  # через верх
           (bo[4] == le and bo[5] == le and bo[6] == le) or  # через центр
           (bo[1] == le and bo[2] == le and bo[3] == le) or  # через низ
           (bo[7] == le and bo[4] == le and bo[1] == le) or  # вниз по левой стороне
           (bo[8] == le and bo[5] == le and bo[2] == le) or  # вниз по центру
           (bo[9] == le and bo[6] == le and bo[3] == le) or  # вниз по правой стороне
           (bo[9] == le and bo[5] == le and bo[1] == le) or  # / диагональ
           (bo[7] == le and bo[5] == le and bo[3] == le))   # \ диагональ


def get_board_copy(board):
    # Создает копию игрового поля и возвращает ее
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    # Возвращает True, если сделан ход в свободную клетку
    return board[move] == ' '


def get_player_move(board):
    # разрешает игроку делат ход
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, move_list):
    # Возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток.
    # Возвращает значение None, если больше нет допустимых ходов
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
          possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Учитывая заполнение игрового поля и букву компьютера, определяет допустимый ход и возвращает его
    if computer_letter == 'X':
        player_letter = 'O'
    elif computer_letter == 'O':
        player_letter = 'X'

    # Алгоритм ИИ для игры "Крестики-Нолики"
    # Сначала проверка победного хода
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Проверка- победит ли игрок, сделав следующий ход, блокировка его хода.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Попытка компьютера занять угловую клетку, если она свободна.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    elif is_space_free(board, 5):  # Попытка сходить в центр
        return 5
    # Попытка хода в одну из боковых клеток
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    # Возвращает True, если клетка на игровом поле занята
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print("К Р Е С Т И К И - Н О Л И К И")
while True:
    the_board = [' '] * 10  # Перезагрузка игрового поля
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('' + turn + ' ходит первым.')
    gameIspPlaying = True
    while gameIspPlaying:
        if turn == 'Человек':
            # Ход игрока
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)
            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Ура! Вы выиграли!')
                gameIspPlaying = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничь!')
                    break
                else:
                    turn = 'Компьютер'
        else:
            # Ход компьютера
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)
            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('Компьютер победил! Вы проиграли!')
                gameIspPlaying = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничь!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз?(да/нет)')
    if not input().lower().startswith('д'):
        break