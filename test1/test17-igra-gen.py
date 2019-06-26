import random

numbers = ['1', '2', '3']
symbols = ["DIAMOND", "SQUIGGLE", "OVAL"]
shadings = ["STRIPPED", "SOLID", "OPEN"]
colors = ["RED", "GREEN", "PURPLE"]


namber_n = []
namber_s = []
namber_sh =[]
namber_c = []

def check_set(cards):
    for card in cards:
        if card[0] not in namber_n:
            namber_n.append(card[0])
        if card[1] not in namber_s:
            namber_s.append(card[1])
        if card[2] not in namber_sh:
            namber_sh.append(card[2])
        if card[3] not in namber_sh:
            namber_c.append(card[3])
    print(namber_n)
    print(namber_s)
    print(namber_sh)
    print(namber_c)
    if (len(namber_n) or len(namber_s) or len(namber_sh) or len(namber_c)) == 1 \
            or (len(namber_n)==3 and len(namber_s)==3 and len(namber_sh)==3 and len(namber_c) == 3):
        return True
    else:
        return False

y = []
i = 0
while i <3:
    i += 1

    index1 = random.randrange(0,len(numbers))
    number = numbers[index1]

    index2 = random.randrange(0, len(symbols))
    symbol = symbols[index2]

    index3 = random.randrange(0, len(shadings))
    shading = shadings[index3]

    index4 = random.randrange(0, len(colors))
    color = colors[index4]

    y.append(str(number) + ' ' + str(symbol) + ' ' + str(shading) + ' ' + str(color) + ' ')

for a in y:
    print(a)
print(check_set(list(y)))