from random import randint
boardState = 0
board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# board[0][0] = 'X'
# board[0][1] = 'O'
# board[0][2] = 'X'

# board[1][0] = 'X'
# board[1][1] = 'O'
# board[1][2] = 'X'

# board[2][0] = 'O'
# board[2][1] = 'X'
# board[2][2] = 'O'


def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


def column(matrix, i):
    return [row[i] for row in matrix]


def does_player_win(whichPlayer, board):
    for b in board:
        if b == [whichPlayer, whichPlayer, whichPlayer]:
            return True
    for i in range(0, 3):
        if column(board, i) == [whichPlayer, whichPlayer, whichPlayer]:
            return True
    if [board[0][0], board[1][1], board[2][2]] == [whichPlayer, whichPlayer, whichPlayer]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [whichPlayer, whichPlayer, whichPlayer]:
        return True
    return False


def generate_position():
    aiChoiseX = randint(0, 2)
    aiChoiseY = randint(0, 2)
    return [aiChoiseX, aiChoiseY]


def ai_move(board):

    for i in range(0, 3):
        if board[i] == ['X', '*', 'X']:
            board[i][1] = 'O'
            return
        if board[i] == ['*', 'X', 'X']:
            board[i][0] = 'O'
            return
        if board[i] == ['X', 'X', '*']:
            board[i][2] = 'O'
            return
        if column(board, i) == ['X', '*', 'X']:
            board[1][i] = 'O'
            return
        if column(board, i) == ['*', 'X', 'X']:
            board[0][i] = 'O'
            return
        if column(board, i) == ['X', 'X', '*']:
            board[2][i] = 'O'
            return

    rng = generate_position()

    while board[rng[0]][rng[1]] != '*':
        rng = generate_position()

    board[rng[0]][rng[1]] = 'O'


def get_user_move(board):
    x, y = input("Your choice (Y, X)\t").split()
    while board[int(x)][int(y)] != '*':
        x, y = input('Your choice (Y, X)\t').split()
    board[int(x)][int(y)] = 'X'
    return board


def is_draw(board):
    xNumber = 0
    oNumber = 0
    for b in board:
        for i in b:
            if i == 'X':
                xNumber += 1
            if i == 'O':
                oNumber += 1
    if [xNumber, oNumber] == [4, 5] or [xNumber, oNumber] == [5, 4]:
        if not does_player_win('X', board) and not does_player_win('O', board):
            return True
    return False


print_board(board)
# print(does_player_win('X', board))
# ai_move(board)
# print_board(board)
print(is_draw(board))

while True:
    get_user_move(board)
    if is_draw(board) or does_player_win('X', board):
        print('Player Won')
        print_board(board)
        break
    print_board(board)
    print('---------------')
    ai_move(board)
    if is_draw(board) or does_player_win('O', board):
        print('Computer Won')
        print_board(board)
        break
    print_board(board)
