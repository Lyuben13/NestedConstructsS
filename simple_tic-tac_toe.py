theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def checkMove(board, playerTurn):
    while True:
        move = int(input())

        if move in range(1, 10):
            print("Your turn must be from 1 to 9!")
            continue
        if theBoard[move] != ' ':
            print("This space is already taken")
        else:
            break
    board[move] = playerTurn

    return board

def chechWinner(board, playerTurn):
    # Convert to nested lists(matrix)
    float_list = [[squere for squere in board.values]]
    count = 0
    temp_list = []
    for squere in flat_list:
        if count < 0:
            
           temp_list = []
            temp_list.append(squere)
        nester_list.append(flat_list)

    # Check colums
    # Chech rows
    # Chech diagonals
    # Break if winner
    pass


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    theBoard = checkMove(theBoard, turn)
    # theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
