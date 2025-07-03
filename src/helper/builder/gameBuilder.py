from TicTacToe.src.customExceptions.invalidPlayerException import InvalidPlayerException

class GameBuilder:
    def __init__(self):
        self.dimension = None
        self.players = None
        self.winning_strategy = None

    def set_dimension(self, dimension):
        self.dimension = dimension
        return self

    def set_players(self, players):
        self.players = players
        return self

    def set_winning_strategy(self, winning_strategy):
        self.winning_strategy = winning_strategy
        return self

    def validate(self):
        if self.players is None or len(self.players) > self.dimension - 1:
            raise InvalidPlayerException()

    def build(self):
        from TicTacToe.src.models.game import Game
        self.validate()
        return Game(self.dimension, self.players, self.winning_strategy)