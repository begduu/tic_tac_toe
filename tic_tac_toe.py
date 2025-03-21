



board = {"1":"-", "2":"-", "3":"-",
         "4":"-", "5":"-", "6":"-",
         "7":"-", "8":"-", "9":"-"}

player_turn = 1

def x_turn():
    x_input = input("Choose a place to put an X (1-9): ")
    if int(x_input) >= 1 and int(x_input) <= 9 and board[x_input] == "-":
        board[x_input] = "X"
    else:
        x_turn()
def o_turn():
    o_input = input("Choose a place to put an O (1-9): ")
    if int(o_input) >= 1 and int(o_input) <= 9 and board[o_input] == "-":
        board[o_input] = "O"
    else:
        o_turn()
        
def win_vert(board):    
    if board["1"] == board["4"] == board["7"] and board["1"] != "-":
        return True
    elif board["2"] == board["5"] == board["8"] and board["2"] != "-":
        return True
    elif board["3"] == board["6"] == board["9"] and board["3"] != "-":
        return True
    return False

def win_hori(board):    
    if board["1"] == board["2"] == board["3"] and board["1"] != "-":
        return True
    elif board["4"] == board["5"] == board["6"] and board["4"] != "-":
        return True
    elif board["7"] == board["8"] == board["9"] and board["7"] != "-":
        return True
    return False

def win_diag(board): 
    if board["1"] == board["5"] == board["9"] and board["1"] != "-":
        return True
    elif board["3"] == board["5"] == board["7"] and board["3"] != "-":
        return True
    return False

def tie(board):
    if "-" not in board.values():
        return True
    return False

def winner(board):
    if win_vert(board) or win_hori(board) or win_diag(board):
        return True
    return False


while True:
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print(board["7"] + "|" + board["8"] + "|" + board["9"])

    if player_turn == 1:
        x_turn()
        if winner(board):
            print("\nPlayer X wins!")
            break
        if tie(board):
            print("\nIt's a tie!")
            break
        player_turn = 0 
    else: 
        o_turn()
        if winner(board):
            print("\nPlayer O wins!")
            break
        if tie(board):
            print("\nIt's a tie!")
            break
        player_turn = 1  
print(board["1"] + "|" + board["2"] + "|" + board["3"])
print(board["4"] + "|" + board["5"] + "|" + board["6"])
print(board["7"] + "|" + board["8"] + "|" + board["9"])

