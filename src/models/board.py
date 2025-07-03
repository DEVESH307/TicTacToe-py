from TicTacToe.src.models.cell import Cell

class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.grid = [[Cell(row, col) for col in range(board_size)] for row in range(board_size)]
        

    def print_board(self):
        for row in self.grid:
            for cell in row:
                cell.display()
            print()

