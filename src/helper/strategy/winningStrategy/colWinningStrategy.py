from TicTacToe.src.helper.strategy.winningStrategy.winning import WinningStrategy

class ColWinningStrategy(WinningStrategy):
    def __init__(self):
        # Structure: {col_index: {symbol: count}}
        self.col_counts = {}

    def check_winner(self, board, cell):
        col = cell.col
        symbol = cell.player.symbol

        if col not in self.col_counts:
            self.col_counts[col] = {}

        if symbol not in self.col_counts[col]:
            self.col_counts[col][symbol] = 0

        self.col_counts[col][symbol] += 1

        if self.col_counts[col][symbol] == board.board_size:
            return True

        return False

    def undo_handle(self, board, cell):
        col = cell.col
        symbol = cell.player.symbol

        if col in self.col_counts and symbol in self.col_counts[col]:
            self.col_counts[col][symbol] -= 1

            if self.col_counts[col][symbol] == 0:
                del self.col_counts[col][symbol]

            if not self.col_counts[col]:  # Remove col key if empty
                del self.col_counts[col]
