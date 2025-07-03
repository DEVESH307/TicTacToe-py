# TicTacToe/src/customExceptions/customExceptions.py

class GameException(Exception):
    """Base class for exceptions in this game."""
    pass

class InvalidPlayerException(Exception):
    """Raised when an invalid player is encountered, such as a player with no symbol."""
    pass

class GameInterruptedException(Exception):
    """Raised when the user manually interrupts the game (e.g., Ctrl+C)."""
    pass

class InvalidInputException(Exception):
    """Raised for invalid user input, like non-numeric values for coordinates."""
    pass

class UnsupportedDifficultyException(Exception):
    """Raised when an unsupported bot difficulty level is requested."""
    pass