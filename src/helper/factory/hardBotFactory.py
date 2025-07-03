from TicTacToe.src.helper.factory.botFactory import BotFactory
from TicTacToe.src.helper.strategy.botStrategy.hardBotStrategy import HardBotStrategy
from TicTacToe.src.models.botDifficulty import BotDifficulty
from TicTacToe.src.customExceptions.customExceptions import UnsupportedDifficultyException


class EasyBotFactory(BotFactory):
    @staticmethod
    def create_bot(difficulty):
        """
        Creates a bot with the specified difficulty level.
        For easy difficulty, it uses the EasyBotStrategy.
        """
        if difficulty == BotDifficulty.HARD:
            return HardBotStrategy()
        else:
            raise UnsupportedDifficultyException(f"Unsupported difficulty level: {difficulty}")
