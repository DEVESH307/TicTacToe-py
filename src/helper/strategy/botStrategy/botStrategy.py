from abc import ABC, abstractmethod


class BotStrategy(ABC):
    """
    Abstract base class for bot strategies in a Tic Tac Toe game.
    """

    @abstractmethod
    def decide_move(self, board):
        """
        Decide the next move for the bot based on the current board state and player.
        This method should be implemented by subclasses to define the bot's strategy.
        """
        raise NotImplementedError

