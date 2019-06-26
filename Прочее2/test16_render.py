board = "<table><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>"
def render_board(board):
    with open("board.html", "w") as file:
        for line in board:
            file.write(line)
    return "board.html"
render_board(board)

with open("board.html", "r") as file:
    for line in file:
        print(line)