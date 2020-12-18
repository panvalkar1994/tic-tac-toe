def fill_board(place):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(len(place)):
        row = i // 3
        col = i % 3
        board[row][col] = place[i]
    return board


def display_field(board):
    print('---------')
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=' ')
        print("|")
    print('---------')
    return None


def win(board, target):
    # winning row
    for row in range(3):
        if target == board[row][0] and board[row][0] == board[row][1] == board[row][2]:
            return True

    # winning column
    for col in range(3):
        if '_' != board[0][col] and board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == target:
                return True
    # winning diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == target:
            return True
    # winning trailing diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == target:
            return True
    return False


def impossible(board):
    if win(board, 'X') and win(board, 'O'):
        return True
    xs = 0
    os = 0
    for i in places:
        if i == 'X':
            xs += 1
        elif i == 'O':
            os += 1
    if abs(xs - os) > 1:
        return True
    return False


def draw():
    if empty(boards):
        return False
    else:
        return not win(boards, 'X') or not win(boards, 'O')


def empty(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' or board[row][col] != 'O':
                return True
    return False


def not_finished(board):
    return empty(board)


# result codes
# impossible = -1
# x_win = 10
# o_win = -10
# not_finish = 5
# draw_match = 0


def result(board):
    if impossible(board):
        return f'Impossible'
    elif win(board, 'X'):
        return f'X wins'
    elif win(board, 'O'):
        return f'O wins'
    elif not_finished(board):
        return f'Game not finished'
    elif draw():
        return f'Draw'
    return 'IDK'


def print_board(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col] == 'X', end=' ')


def change_player(player):
    if player == 'X':
        return '0'
    return 'X'


def get_coordinates(board, player):
    while True:
        coordinates = input('Enter the coordinates: ')
        x, y = coordinates.split()
        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)
            if 0 < x < 4 and 0 < y < 4:
                if board[x - 1][y - 1] == 'X' or board[x - 1][y - 1] == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    board[x - 1][y - 1] = player
                    break
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


places = ' ' * 9
boards = fill_board(places)
# display_field(boards)
player = 'X'
# print(result(boards))
# get_coordinates(boards)
# display_field(boards)

# while True:
#     display_field(boards)
#     get_coordinates(boards, player)
#     # if win(boards,'X') or win(boards, 'O') or draw():
#     #     break
#     if win(boards, 'X'):
#         break
#     elif win(boards, 'O'):
#         break
#     elif draw():
#         break
#     player = change_player(player)

for _ in range(9):
    display_field(boards)
    get_coordinates(boards, player)
    if win(boards, 'X') or win(boards, 'O'):
        break

if win(boards, 'X'):
    display_field(boards)
    print("X wins")
elif win(boards, 'O'):
    display_field(boards)
    print("O wins")
elif draw():
    display_field(boards)
    print("Draw")

# display_field(boards)
# print(result(boards))
# print("Game over")


# print(empty(boards))
# print(win(boards, 'X'))
# print_board(boards)
