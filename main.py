
piece_values = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
}

white_pieces = ["Q", "P", "P"]
black_pieces = ["r", "p", "p", "p"]

white_score = 0

for piece in white_pieces:
    white_score += piece_values[piece]

black_score = 0

for piece in black_pieces:
    black_score += piece_values[piece.upper()]

material_score = white_score - black_score

print("White score:", white_score)
print("Black score:", black_score)
print("Material score:", material_score)
