from TicTacToe.src.helper.strategy.winningStrategy.winning import WinningStrategy


class CornerWinningStrategy(WinningStrategy):
    def __init__(self):
        # {symbol: count of corners owned}
        self.corner_counts = {}

    def check_winner(self, board, cell):
        row = cell.row
        col = cell.col
        symbol = cell.player.symbol
        size = board.board_size

        is_corner = (row == 0 and col == 0) or \
                    (row == 0 and col == size - 1) or \
                    (row == size - 1 and col == 0) or \
                    (row == size - 1 and col == size - 1)

        if is_corner:
            if symbol not in self.corner_counts:
                self.corner_counts[symbol] = set()

            self.corner_counts[symbol].add((row, col))

            if len(self.corner_counts[symbol]) == 4:
                return True

        return False

    def undo_handle(self, board, cell):
        row = cell.row
        col = cell.col
        symbol = cell.player.symbol
        size = board.board_size

        is_corner = (row == 0 and col == 0) or \
                    (row == 0 and col == size - 1) or \
                    (row == size - 1 and col == 0) or \
                    (row == size - 1 and col == size - 1)

        if is_corner and symbol in self.corner_counts:
            self.corner_counts[symbol].discard((row, col))
            if not self.corner_counts[symbol]:
                del self.corner_counts[symbol]
