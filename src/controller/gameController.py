# from TicTacToe.src.models.game import Game


class GameController:
    def __init__(self, game_service):
        self.game_service = game_service

    def start_game(self, size, players, winning_strategy):
        # validation using builder
        return self.game_service.start_game(size, players, winning_strategy)

    def display_board(self, game):
        self.game_service.display_board(game)

    def make_move(self, game):
        self.game_service.make_move(game)

    def check_winner(self, game):
        return self.game_service.check_winner(game)

    def undo_move(self, game):
        self.game_service.undo_move(game)



# start the game
# status of game in progress
# In the game loop:
    # display the board
    # player makes a move on board
    # offer undo option before confirming move
    # check for winner
    # if no winner or not all cells filled, continue:
        # switch to next player index
        # other player makes a move on board
        # offer undo option before confirming move
    # if winner, display winner and end game