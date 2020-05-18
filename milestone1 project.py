def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])













board=['#', 'X', 'O','X', 'O','X', 'O','X', 'O', 'X']
print('-' * 30)
print(f'LETS PLAY TIC TAC TOE'.center(30))
print('-' * 30)
player1 = str(input('Enter X or O: ')).upper().strip()
position = int(input('Use the number pad to play. Enter the position number: '))
print(display_board(board))