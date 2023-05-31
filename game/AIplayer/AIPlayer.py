import random

class AIPlayer:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        valid_moves = []
        for square in board.squares:
            piece = square.occupying_piece
            if piece is not None and piece.color == self.color:
                valid_moves.extend(piece.get_valid_moves(board))
        move = random.choice(valid_moves)
        board.handle_click(move.x * board.tile_width, move.y * board.tile_height)