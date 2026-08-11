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

# get pieces
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

def square_to_index(square):
    if len(square) != 2:
        raise ValueError("Invalid square")

    file = square[0]
    rank = square[1]

    if file not in "abcdefgh" or rank not in "12345678":
        raise ValueError("Invalid square")

    column = ord(file) - ord("a")
    row = 8 - int(rank)
    return row * 8 + column


def index_to_square(index):
    if index < 0 or index > 63:
        raise ValueError("Invalid index")
    rank = 8 - (index // 8)
    file = index % 8 + 1
    letter = chr(file + ord("a") - 1)
    return letter + str(rank)


def board_printer():
    for row in range(8):
        rank = 8 - row
        start = row * 8
        pieces_in_row = board[start:start + 8]
        print(rank, " ".join(pieces_in_row))
    print("  a b c d e f g h")


def make_move(start,end):
    start_index = square_to_index(start)
    end_index = square_to_index(end)
    piece = get_piece_type(board[start_index])
    if piece is None:
        raise ValueError("No piece to move.")
    if get_piece_type(board[end_index]) is None:
        board[end_index] = board[start_index]
        board[start_index] = "."
        print("Success")
    
print(square_to_index("c6"))
print(index_to_square(18))
board_printer()
make_move("e2","e4")
board_printer()

