#Первым шагом нужно создать игровое поле.
#Можем использовать список списков (list of lists) для создания матрицы 3x3,
#которая будет представлять игровое поле.

game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]

#Пишем функцию для отображения игрового поля в консоли.

def display_board(board):
    for row in board:
        print(row)

#Пишем функцию для проверки победы.
#Проверяем все возможные комбинации для победы - горизонтали, вертикали и диагонали.

def check_win(board):
    # проверяем горизонтали
    for row in board:
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return True
   
    # проверяем вертикали
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True
   
    # проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True
   
    # если никто не победил
    return False

#Пишем основную функцию для игры.
#Будем использовать цикл while, чтобы игроки могли по очереди делать ходы.

def play_game():
    # создаем игровое поле
    game_board = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]
    # начинаем игру с крестика
    current_player = 'X'
   
    # игра продолжается, пока не будет победы или ничьи
    while not check_win(game_board) and '-' in [cell for row in game_board for cell in row]:
        # выводим игровое поле
        display_board(game_board)
       
        # спрашиваем у игрока, куда он хочет поставить свой символ
        row = int(input('Выберите строку (1, 2 или 3): ')) - 1
        col = int(input('Выберите столбец (1, 2 или 3): ')) - 1
       
        # проверяем, что выбранная ячейка пустая
        if game_board[row][col] == '-':
            # ставим символ игрока на выбранную ячейку
            game_board[row][col] = current_player
           
            # меняем игрока
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print('Выбранная ячейка уже занята!')
   
    # выводим результат игры
    display_board(game_board)
    if check_win(game_board):
        print(f'Игрок {current_player} проиграл!')
    else:
        print('Ничья!')
play_game()
