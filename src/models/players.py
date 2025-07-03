from TicTacToe.src.models.cellStatus import CellStatus
from TicTacToe.src.customExceptions.customExceptions import GameInterruptedException, InvalidInputException


class Player:
    def __init__(self, name: str, id: int, type, symbol):
        self.name = name
        self.id = id
        self.type = type
        self.symbol = symbol

    def decide_cell(self, board):
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                if 0 <= row < board.board_size and 0 <= col < board.board_size:
                    if board.grid[row][col].status == CellStatus.EMPTY:
                        return board.grid[row][col]
                print("Invalid cell. Try again.")
            except (ValueError, TypeError):
                raise InvalidInputException("Invalid input. Row and column must be numbers.")
            except KeyboardInterrupt:
                raise GameInterruptedException("\nGame interrupted by user. Exiting.")
