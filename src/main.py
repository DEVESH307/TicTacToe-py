from src.controller.GameController import GameController
from src.models.Bot import Bot
from src.models.BotDificulty import BotDificulty
from src.models.PlayerType import PlayerType
from src.models.Symbol import Symbol
from src.models.players import *
if __name__ == '__main__':
    gc = GameController()

    dimensions = 3

    players =  [
        Player("karan", 1, PlayerType.HUMAN, Symbol("x")),
        Bot("Mohit", 2, PlayerType.BOT, Symbol("y"), BotDificulty.EAZy),
    ]

    winning =[]

    gc.start_game(dimensions, players, winning)