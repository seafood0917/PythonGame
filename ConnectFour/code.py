PLAYER = 1
GAME_OVER = False
WINNER = "None"

def created_board():
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    return board

def get_coordinate(i):
    row = i // 7
    col = i - row * 7
    return row, col

BOARD = created_board()

def insert(i):
    row, col = get_coordinate(i)
    while BOARD[row][col] is not 0:
        print("There is already a coin placed.")
        i = input_check()
        row, col = get_coordinate(i)
    BOARD[row][col] = PLAYER

def is_game_over():
    return 0 in BOARD

def input_check():
    where = input("Where do you want to place your coin? ")
    if not where.isdigit():   # isdigit() is a built-in str method to check if str is integer
        print("That is an invalid type of input.")
        print("You should enter a positive integer.")
        return input_check()
    else:
        where = int(where)
        if where < 0 or where > 41:
            print("That is an invalid position.")
            print("You should enter an integer between 0 and 41.")
            return input_check()
        return where

def is_over():
    if 0 not in BOARD:
        GAME_OVER = True
    elif [1, 1, 1, 1] in BOARD or [2, 2, 2, 2] in BOARD:
        GAME_OVER = True
        WINNER = PLAYER

def play():
    global PLAYER
    print("Player:", PLAYER)
    print("Enter an integer between 0 and 41, please.")
    where = input_check()
    insert(where)
    print(BOARD)
    PLAYER = 3 - PLAYER

while not GAME_OVER:
    play()
    is_over()
print(WINNER)
