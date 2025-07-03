from TicTacToe.src.helper.strategy.botStrategy.botStrategy import BotStrategy
from TicTacToe.src.models.cellStatus import CellStatus


class EasyBotStrategy(BotStrategy):
    def decide_move(self, board):
        """
        Randomly selects an available cell on the board for the bot's move.
        This is a simple strategy where the bot does not consider winning or blocking moves.
        """
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None