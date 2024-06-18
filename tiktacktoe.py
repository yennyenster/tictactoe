game_matrix = [['_','_','_'],
                ['_','_','_'],
                [' ',' ',' ']]
p1_turn = True
have_winner = False
p1 = ""
p1_sym = ""
p2 = ""
p2_sym = ""

def init_players():
    global p1
    global p1_sym
    global p2
    global p2_sym
        
    p1 = str(input("What's player 1's name? "))
    p1_sym = str(input("What symbol will " + p1 + " play with? no spaces/underscores "))
    while p1_sym == " " or p1_sym == "_":
        print("\n:< I said no underscores/spaces.\n")
        p1_sym = str(input("What symbol will " + p1 + " play with? no spaces/underscores "))
    p2 = str(input("What's player 2's name? "))
    p2_sym = str(input("What symbol will " + p2 + " play with? no spaces/underscores "))
    while p2_sym == " " or p2_sym == "_":
        print("\n:< I said no underscores/spaces.\n")
        p2_sym = str(input("What symbol will " + p2 + " play with? no spaces/underscores "))
    while p2_sym == p1_sym:
        print("\nNo using the same symbol darn u\n")
        p2_sym = str(input("What symbol will " + p2 + " play with? no spaces/underscores "))

def change_turn():
    global p1_turn
    
    if p1_turn == True:
        p1_turn = False
    else:
        p1_turn = True
        
def find_current_player():
    global p1
    global p1_sym
    global p2
    global p2_sym
    
    if p1_turn == True:
        return (p1, p1_sym)
    return(p2, p2_sym)
    
def is_horizonal_win(row_index, col_index):
    if game_matrix[row_index][0] == game_matrix[row_index][1]:
        if game_matrix[row_index][1] == game_matrix[row_index][2]:
            return True
        
def is_vertical_win(row_index, col_index):
    if game_matrix[0][col_index] == game_matrix[1][col_index]:
        if game_matrix[1][col_index] == game_matrix[2][col_index]:
            return True

def is_diagonal_win():
    if game_matrix[0][0] == game_matrix[1][1]:
        if game_matrix[1][1] == game_matrix[2][2]:
            return True
    if game_matrix[2][0] == game_matrix[1][1]:
        if game_matrix[1][1] == game_matrix[0][2]:
            return True
    
def check_game_status(row_index, col_index, cur_player, cur_sym):
    if is_horizonal_win(row_index, col_index) == True or is_vertical_win(row_index, col_index) == True or is_diagonal_win() == True:
        return True
    return False

def update_game_matrix(row_index, col_index, cur_sym):
    game_matrix[row_index][col_index] = cur_sym
        
def is_sym_there(row_index, col_index):
    global p1_sym
    global p2_sym
    
    if game_matrix[row_index][col_index] == p1_sym or game_matrix[row_index][col_index] == p2_sym:
        return True
    return False
    
def put_symbol(cur_player, cur_sym):
    global have_winner
    
    print("It's " + cur_player + "'s turn! :D")
    while(True):
        row_index = int(input("Pick a row to put symbol in (0-2) "))
        while row_index not in range(0,3):
            print("\nMate, pick 0, 1, or 2 for the row ouo\n")
            row_index = int(input("Pick a row to put symbol in (0-2) "))
        col_index = int(input("Pick a column to put the symbol in (0-2) "))
        while col_index not in range(0,3):
            print("\nMate, pick 0, 1, or 2 for the column ouo\n")
            col_index = int(input("Pick a column to put the symbol in (0-2) "))
        if is_sym_there(row_index, col_index) == False:
            break
        else:
            print("\nSomething's there silly :c pick a different place\n")
        
        
    update_game_matrix(row_index, col_index, cur_sym)
    if check_game_status(row_index, col_index, cur_player, cur_sym) == True:
        print_game_board()
        have_winner = True
        
    else:
        print_game_board()
        change_turn()


def print_game_board():
    print("\nCurrent game board\n")
    print(game_matrix[0][0] + "|" + game_matrix[0][1] + "|" + game_matrix[0][2])
    print(game_matrix[1][0] + "|" + game_matrix[1][1] + "|" + game_matrix[1][2])
    print(game_matrix[2][0] + "|" + game_matrix[2][1] + "|" + game_matrix[2][2])
    
def play_game():
    global have_winner
    global p1_turn
    turn_number = 0
    
    print("Sweet! Let's set you and your buddy up before playing.")
    init_players()
    print("\n~~~~~~~~~~~~~~")
    print_game_board()
    
    while have_winner == False and turn_number < 9:
        (cur_player, cur_sym) = find_current_player()
        put_symbol(cur_player, cur_sym)
        if have_winner == True:            
            return("\nBOOOOMM!!! CONGRATS " + cur_player.upper() + "!!!!")
        turn_number += 1
    
    return("\nWe have no winners here gg")

    
    
def launch_game():
    print("Welcome to yenster's tic tac toe")
    key = str(input("press space bar to play :D"))
              
    while key != " ":
        print(":) wrong button")
        launch_game()
        
    print(play_game())
    
launch_game()
    
