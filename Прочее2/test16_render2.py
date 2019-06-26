# coding: utf-8


def generate_board(board):
    board = "<table ><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>"
    return "<body>" + board + "</body>"


def render_board(board):
    fp = open('games.html', "w")
    page = generate_page(
        head=generate_head('Game'),
        board=generate_board(board),
    )
    fp.write(page)
    fp.close()
    fp = open('games.html', 'r')
    result = fp.read()
    print(str(result))


render_board(
    board=generate_board(""" """)
)