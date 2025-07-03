from TicTacToe.src.customExceptions.customExceptions import GameInterruptedException, InvalidInputException
from TicTacToe.src.controller.gameController import GameController
from TicTacToe.src.helper.strategy.winningStrategy.rowWinningStrategy import RowWinningStrategy
from TicTacToe.src.helper.strategy.winningStrategy.colWinningStrategy import ColWinningStrategy
from TicTacToe.src.helper.strategy.winningStrategy.cornerWinningStrategy import CornerWinningStrategy
from TicTacToe.src.helper.strategy.winningStrategy.diagonalWinningStrategy import DiagonalWinningStrategy
from TicTacToe.src.models.botDifficulty import BotDifficulty
from TicTacToe.src.models.gameStatus import GameStatus
from TicTacToe.src.models.players import Player
from TicTacToe.src.models.bot import Bot
from TicTacToe.src.models.playerType import PlayerType
from TicTacToe.src.models.symbol import Symbol
from TicTacToe.src.services.gameService import GameService


if __name__ == "__main__":
    gs = GameService()
    gc = GameController(gs)

    dimensions = 3

    players = [
        Player("Devesh", 1, PlayerType.HUMAN, Symbol("X")),
        Bot("Karan", 2, Symbol("O"), BotDifficulty.EASY)
    ]

    winning = [
        RowWinningStrategy(),
        ColWinningStrategy(),
        DiagonalWinningStrategy(),
        CornerWinningStrategy(),
    ]

    game = gc.start_game(dimensions, players, winning)

    # display the board
    gc.display_board(game)

    # until game in progress take input
    # while game.gameStatus == GameStatus.IN_PROGRESS:
    #     gc.make_move(game)
    #     gc.display_board(game)
    #     undo_answer = input("Do you want to undo? Press 1 for Yes, 0 for No: ")
    #     if undo_answer == "1":
    #         print("Undoing last move...")
    #         gc.undo_move(game)
    #         gc.display_board(game)

    try:
        while game.gameStatus == GameStatus.IN_PROGRESS:
            try:
                gc.make_move(game)
                gc.display_board(game)

                if game.gameStatus != GameStatus.IN_PROGRESS:
                    break

                undo_answer = input("Do you want to undo? Press 1 for Yes, 0 for No: ")
                if undo_answer == "1":
                    print("Undoing last move...")
                    gc.undo_move(game)
                    gc.display_board(game)

            except InvalidInputException as e:
                print(e)
                continue

    except GameInterruptedException as e:
        print(e)
        game.gameStatus = GameStatus.DRAW # Or some other ended state

    # show end game message
    if game.gameStatus == GameStatus.COMPLETED:
        print(f"Game Over! {game.winner.name} wins!")
    elif game.gameStatus == GameStatus.DRAW:
        print("Game Over! It's a draw!")
    else:
        print("Game is still in progress.")
