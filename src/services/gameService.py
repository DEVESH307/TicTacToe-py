from TicTacToe.src.models.cellStatus import CellStatus
from TicTacToe.src.models.gameStatus import GameStatus


class GameService:
    def start_game(self, size, players, winning_strategy):
        from TicTacToe.src.models.game import Game
        game = Game.gameBuilder().set_dimension(size).set_players(players).set_winning_strategy(winning_strategy).build()
        return game

    def display_board(self, game):
        game.Board.print_board()

    def make_move(self, game):
        current_player = game.players[game.next_turn]
        cell = current_player.decide_cell(game.Board)
        cell.player = current_player
        cell.status = CellStatus.FILLED
        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.gameStatus = GameStatus.COMPLETED
            game.winner = current_player
        # Check if the game is a draw
        elif len(game.moves) == game.Board.board_size ** 2:
            game.gameStatus = GameStatus.DRAW

        # increment the turn to the next player
        game.next_turn = (game.next_turn + 1) % len(game.players)

    def check_winner(self, game, cell):
        return any(ws.check_winner(game.Board, cell) for ws in game.winning_strategy)

    def undo_move(self, game):
        if not game.moves:
            print("No moves to undo")
            return

        # Retrieve the last move
        last_move = game.moves.pop()

        # Undo the winning strategy
        for ws in game.winning_strategy:
            ws.undo_handle(game.Board, last_move)

        # Reset the cell status
        last_move.status = CellStatus.EMPTY
        last_move.player = None

        # Update the next turn to the previous player
        game.next_turn = (game.next_turn - 1) % len(game.players)
        game.status = GameStatus.IN_PROGRESS