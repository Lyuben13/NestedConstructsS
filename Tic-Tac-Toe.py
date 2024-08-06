ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' '


def main():
    """Runs a game of tic-tac-toe."""
    print('Welcome to tic-tac-toe!')
    gameBoard = TTTBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(gameBoard.getBoardStr())

        move = None
        while not gameBoard.isValidSpace(move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
            if not move.isdigit() or move not in ALL_SPACES:
                print("Please enter a valid number between 1 and 9.")
                move = None
                continue

            if gameBoard.isValidSpace(move):
                gameBoard.updateBoard(move, currentPlayer)
                break
            else:
                print("That space is already occupied. Choose another space.")
                move = None

        # Check if the game is over:
        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(f'{currentPlayer} has won the game!')
            break
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print("The game is a tie.")
            break

        # Swap turns
        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    print('Thanks for playing!')


class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic-tac-toe board."""
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return (
            f"{self._spaces['1']} | {self._spaces['2']} | {self._spaces['3']}  1 2 3\n"
            f"--+---+--\n"
            f"{self._spaces['4']} | {self._spaces['5']} | {self._spaces['6']}  4 5 6\n"
            f"--+---+--\n"
            f"{self._spaces['7']} | {self._spaces['8']} | {self._spaces['9']}  7 8 9"
        )

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space number and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        b, p = self._spaces, player  # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((b['1'] == b['2'] == b['3'] == p) or  # Across the top
                (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
                (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
                (b['1'] == b['4'] == b['7'] == p) or  # Down the left
                (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
                (b['3'] == b['6'] == b['9'] == p) or  # Down the right
                (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
                (b['1'] == b['5'] == b['9'] == p))  # Diagonal

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # If a single space is blank, return False.
        return True  # No spaces are blank, so return True.

    def updateBoard(self, space, mark):
        """Sets the space on the board to mark."""
        self._spaces[space] = mark


main()
