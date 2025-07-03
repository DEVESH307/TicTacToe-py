from TicTacToe.src.customExceptions.gameException import GameException


class UnsupportedDifficultyException(GameException):
    """Raised when an unsupported difficulty level is specified."""

    def __init__(self, message="Unsupported difficulty level provided."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"UnsupportedDifficultyException: {self.message}"