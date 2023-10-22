board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]
def flood_fill(input_board, old, new, x, y):
    if (x > 7 or x < 0 or y > 21 or y < 0):
        return
    elif(input_board[x][y] == old):
      input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
      flood_fill(input_board, old, new, x + 1, y)
      flood_fill(input_board, old, new, x - 1, y)
      flood_fill(input_board, old, new, x, y + 1)
      flood_fill(input_board, old, new, x, y - 1)
      return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)