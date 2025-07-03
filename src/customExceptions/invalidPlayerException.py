from TicTacToe.src.customExceptions.gameException import GameException

class InvalidPlayerException(GameException):
    def __init__(self, message="Invalid player configuration."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidPlayerException: {self.message}"