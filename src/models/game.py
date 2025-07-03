from TicTacToe.src.models.board import Board
from TicTacToe.src.models.gameStatus import GameStatus
from TicTacToe.src.helper.builder.gameBuilder import GameBuilder

class Game:
    def __init__(self, dimension, players, winning_strategy):
        self.Board = Board(dimension)
        self.players = players
        self.winning_strategy = winning_strategy
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.IN_PROGRESS

    @staticmethod
    def gameBuilder():
        return GameBuilder()