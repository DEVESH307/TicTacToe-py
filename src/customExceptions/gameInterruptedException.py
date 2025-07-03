from TicTacToe.src.customExceptions.gameException import GameException


class GameInterruptedException(GameException):
    """Raised when the user manually interrupts the game."""
    def __init__(self, message="Game interrupted by user."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"GameInterruptedException: {self.message}"