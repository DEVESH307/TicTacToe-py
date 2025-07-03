from TicTacToe.source.src.models.PlayerType import PlayerType
from TicTacToe.src.helper.factory.easyBotFactory import EasyBotFactory
from TicTacToe.src.models.players import Player

class Bot(Player):
    def __init__(self, name: str, player_id: int, symbol, difficulty):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.strategy = EasyBotFactory.create_bot(self.difficulty)

    def decide_cell(self, board):
        return self.strategy.decide_move(board)