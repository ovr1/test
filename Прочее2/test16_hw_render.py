# coding: utf-8

def generate_page(head, board):
    page = "<html>" + head + board + "</html>"
    return page


def generate_head(title):
    title = 'Board'
    head = "<meta charset='utf-8'>" + "<title>" + title + "</title>" +  """<style type="text/css">
            td {
               width: 150px;
                height: 150px;
                border: 5px solid #1533ad;
                text-align: center;
                font-size: 80pt;
                font-weight: bold;
            }
            table {
                border-collapse: collapse;
                border-style:hidden;
            }
         </style></html>"""
    return "<head>" + head + "</head>"


def generate_board(board):
    board = "<table ><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>"
    return "<body>" + board + "</body>"


def render_board(board):
    fp = open('board.html', "w")
    page = generate_page(
        head=generate_head('Game'),
        board=generate_board(board),
    )
    fp.write(page)
    fp.close()
    fp = open('board.html', 'r')
    result = fp.read()
    print(str(result))
    




render_board(
    board=generate_board(""" """)
)
