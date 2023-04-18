board = [' ' for x in range(9)]
endgame = False
options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "EXIT"]

print('| ---------------------- |')
print('| THE PYTHON TIC-TAC-TOE |')
print('| --- by Will Pedroso -- |')
print('| ---------------------- |')
print('| Instructions:          |')
print('|                        |')
print('| The board follows the  |')
print('| numeric keyboard order |')
print('| ---------------------- |')
print('| Example:               |')
print('|                        |')
print('|         |7|8|9|        |')
print('|         |4|5|6|        |')
print('|         |1|2|3|        |')
print('| ---------------------- |')

def print_board():
    row1 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    global endgame
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print('Your turn player {}'.format(number))
    choice = input('Enter your move (1-9): ').strip()
    if not choice.upper() in options:
        print()
        print('Your choice must be a number between 1 and 9 or "Exit" to quit')
        print()
        player_move(icon)
    elif choice.upper() == "EXIT":
        endgame = True
    elif board[int(choice)-1] == ' ':
        board[int(choice)-1] = icon
    else:
        print()
        print('That space is taken! Try again!')
        print_board()
        player_move(icon)

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False
    
def play_again():
    print()
    playAgain = input("Play again? (Press 'N' if you don't): ")
    if playAgain.upper() == 'N':
        return False
    else:
        return True

def reset_board():
    global board
    board = [' ' for x in range(9)]

def finish():
    print()
    print("GAME OVER!")
    print("THANKS FOR PLAYING!")
    print()

while True:
    print_board()
    player_move('X')
    if endgame == True:
        finish()
        break
    elif is_victory('X'):
        print_board()
        print('X Wins! Congratulations!')
        if not play_again():
            finish()
            break
        else:
            reset_board()
    elif is_draw():
        print_board()
        print('The game is a draw!')
        if not play_again():
            finish()
            break
        else:
            reset_board()
    print_board()
    player_move('O')
    if endgame == True:
        finish()
        break
    elif is_victory('O'):
        print_board()
        print('O Wins! Congratulations!')
        if not play_again():
            finish()
            break
        else:
            reset_board()
    elif is_draw():
        print_board()
        print('The game is a draw!')
        if not play_again():
            finish()
            break
        else:
            reset_board()