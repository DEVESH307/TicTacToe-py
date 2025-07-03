from abc import ABC, abstractmethod

class BotFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_bot(difficulty):
        """
        Abstract method to create a bot instance.
        This method should be implemented by subclasses to define how to create a bot.
        """
        pass
