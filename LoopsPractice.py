# rows: int = 3
#
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print('*', end='_')
#     print()
# print("\n\r")
from typing import List

white = "*"
black = "_"
size = 3
board: []

# for row in range(size * 2):
#     for col in range(size * 2):
#         if (row // size + col // size) % 2 == 0:
#             print("***", end="")
#         else:
#             print("---", end="")
#     print()

square_symbol = white
for x in range(8):
    for y in range(8):
        for symbol_count in range(size):
            print(square_symbol, end='')
        if square_symbol == white:
            square_symbol = black
        else:
            square_symbol = white
    print()
    if square_symbol == white:
        square_symbol = black
    else:
        square_symbol = white

print("\n\r")

chess = ((((white * 5 + black * 5) * size) + "\n") * 3) + ((((black * 5 + white * 5) * 3) + '\n') * size)

print(chess)

even_row = [(white * 3 + black * 3) * 4]
odd_row = [(black * 3 + white * 3) * 4]

# for i in range(8):
#     if i % 2 != 0:
#     board.append(even_row)
# else:
#     board.append(odd_row)
#
# for board_row in board:
#     print(board_row)
