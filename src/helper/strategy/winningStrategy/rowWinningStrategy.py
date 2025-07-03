from TicTacToe.src.helper.strategy.winningStrategy.winning import WinningStrategy

class RowWinningStrategy(WinningStrategy):
    def __init__(self):
        # Structure: {row_index: {symbol: count}}
        self.row_counts = {}

    def check_winner(self, board, cell):
        row = cell.row
        symbol = cell.player.symbol

        if row not in self.row_counts:
            self.row_counts[row] = {}

        if symbol not in self.row_counts[row]:
            self.row_counts[row][symbol] = 0

        self.row_counts[row][symbol] += 1

        if self.row_counts[row][symbol] == board.board_size:
            return True

        return False

    def undo_handle(self, board, cell):
        row = cell.row
        symbol = cell.player.symbol

        if row in self.row_counts and symbol in self.row_counts[row]:
            self.row_counts[row][symbol] -= 1

            if self.row_counts[row][symbol] == 0:
                del self.row_counts[row][symbol]

            if not self.row_counts[row]:  # If inner dict is empty
                del self.row_counts[row]
