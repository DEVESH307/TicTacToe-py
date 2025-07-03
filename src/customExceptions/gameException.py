from TicTacToe.src.customExceptions.customExceptions import GameException

class GameException(GameException):
    """Base class for exceptions in this game."""
    def __init__(self, message="A game error occurred."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"GameException: {self.message}"