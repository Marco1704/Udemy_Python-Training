from random import randint
from 

def display_board(board):
    print ('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = str(input('Player 1: Choose X or O: ')).upper()
    if marker == 'X':
        return 'X','O'
    else:
        return 'O','X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    flip = randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1,10):
         if space_check(board, i):
             return False

    return True


def player_choice(board):

    position = 0

    while position not in range [1, 10] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')




#While loop to keep the game running


print('-' * 30)
print(f'LETS PLAY TIC TAC TOE'.center(30))
print('-' * 30)

while True:
    #PLAY GAME
    #SET EVERTYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    board_g = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to Play? y or n').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #GAME PLAY
    while game_on:

        if turn == 'Player 1':

            #Show the board
            display_board(board_g)
            #choose the position
            position = player_choice(board_g)
            #place the marker on the position
            place_marker(board_g, player1_marker, position)
            #check if they won
            if win_check(board_g, player1_marker):
                display_board(board_g)
                print('Player 1 has Won')
                game_on = False
            else:
                # check if it is a Tie
                if full_board_check(board_g):
                    display_board(board_g)
                    print('IT is a TIE')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board( board_g)
            # choose the position
            position = player_choice(board_g)
            place_marker ( board_g, player2_marker, position )

            # check if they won

            if win_check ( board_g, player2_marker ) :
                display_board ( board_g )
                print ( 'Player 2 has Won' )
                game_on = False

            else :
                # check if it is a Tie
                if full_board_check ( board_g ) :
                    display_board ( board_g )
                    print('IT is a TIE' )
                    break
                else :
                    turn = 'Player 1'
    if not replay():
        break
# BREAK OUT OF THE WHILE LOOP ON replay()