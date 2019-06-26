
import json

board = "<table><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>"

filename = 'board.json'
with open(filename,'w') as f_obj:
    json.dump(board, f_obj)



def render_board(board):
    with open("board.html", "w") as file:
        for line in board:
            file.write(str(line))
    return str("board.html")

render_board(board)

with open("board.html", "r") as file:
    for line in file:
        print(str(line))