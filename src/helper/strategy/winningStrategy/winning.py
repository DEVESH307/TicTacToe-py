from abc import ABC, abstractmethod

class WinningStrategy(ABC):
    """
    Abstract base class for winning
    strategies in a Tic Tac Toe game.
    """

    @abstractmethod
    def check_winner(self, board, cell):
        """
        Check if the current move results in a win.
        This method should be implemented by subclasses to
        define how to check for a winning condition.
        """
        pass

    @abstractmethod
    def undo_handle(self, board, cell):
        """
        Handle the undo operation for the winning strategy.
        This method should be implemented by subclasses to
        define how to handle undo operations specific to
        the winning strategy.
        """
        pass