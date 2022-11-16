def board_display(ttt_board):
    for i in range(3):
        for j in range(3):
            print(ttt_board[i][j], end="")
        print(end=("\n"))
    return ttt_board

def is_move_valid(ttt_board, line_move, column_move): 
    if ttt_board[line_move - 1][column_move - 1] != "-":
        return False
    elif line_move not in [1, 2, 3] or column_move not in [1, 2, 3]:
        return False
    return True

def take_move(ttt_board):
    while True:
        line_move = int(input("Choose line of move: "))
        column_move = int(input("Choose column of move: "))
        if is_move_valid(ttt_board, line_move, column_move):
            break
    return line_move, column_move 

def pawn_choice():
    player_one = input("Player one - choose X or O: ")
    player_two = ""

    if player_one == "X":   #Player one is choosing pawn to play
        player_two = "O"
    else:
        player_two = "X"
    return player_one, player_two

def check_winner(ttt_board):
    win_pos = ([ttt_board[0][0], ttt_board[0][1], ttt_board[0][2]],
                    [ttt_board[1][0], ttt_board[1][1], ttt_board[1][2]],
                    [ttt_board[2][0], ttt_board[2][1], ttt_board[2][2]],
                    [ttt_board[0][0], ttt_board[1][0], ttt_board[2][0]],
                    [ttt_board[0][1], ttt_board[1][1], ttt_board[2][1]],
                    [ttt_board[0][2], ttt_board[1][2], ttt_board[2][2]],
                    [ttt_board[0][0], ttt_board[1][1], ttt_board[2][2]],
                    [ttt_board[2][0], ttt_board[1][1], ttt_board[0][2]])
    
    for i in win_pos:
        if i == ["X", "X", "X"] or i == ["O", "O", "O"]:
            return True
        else:
            return False
    
ttt_board = ([["-", "-", "-"], 
              ["-", "-", "-"], 
              ["-", "-", "-"]])

board_display(ttt_board)

player_config = pawn_choice()

iteration_count = 0

while True:
    player = iteration_count % 2
    print("ACTUAL BOARD")   #Printing out actual board
    board_display(ttt_board)
    print(f"Player {player + 1} move")
    line_move, column_move = take_move(ttt_board)
    ttt_board[line_move - 1][column_move - 1] = player_config[player]
    if check_winner(ttt_board):
        print(f"The winner is player {player + 1}")
        break
    iteration_count += 1
    










