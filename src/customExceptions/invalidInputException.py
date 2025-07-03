from TicTacToe.src.customExceptions.gameException import GameException


class InvalidInputException(GameException):
    """Raised for invalid user input."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidInputException: {self.message}"