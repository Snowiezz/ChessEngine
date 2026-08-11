board = [
    "r", "n", "b", "q", "k", "b", "n", "r",
    "p", "p", "p", "p", "p", "p", "p", "p",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    "P", "P", "P", "P", "P", "P", "P", "P",
    "R", "N", "B", "Q", "K", "B", "N", "R",
]
pieces = {
    "r":["Rook"],
    "n":["Knight"],
    "b":["Bishop"],
    "q":["Queen"],
    "k":["King"],
    "p":["Pawn"],
    ".":["Empty"]
}
def get_piece_colour(piece):
    if piece == ".":
        return None
    elif piece.isupper():
        return "White"
    else:
        return "Black"

def get_piece_type(piece):
    if piece == ".":
        return None
    return pieces[piece.lower()][0]


def get_piece(position):
    return get_piece_colour(board[position]),get_piece_type(board[position])

print(get_piece(62))
