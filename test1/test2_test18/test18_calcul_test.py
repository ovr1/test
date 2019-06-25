import mycalc


def test_add():
    assert mycalc.add(1, 2) == 3
    if mycalc.add(1, 2) == 3:
        print("add(a, b) OK")
    else:
        print("add(a, b) NOT OK")


def test_mul():
    if mycalc.mul(2, 5) == 10:
        print("mul(a, b) OK")
    else:
        print("mul(a, b) NOT OK")


def test_sub():
    if mycalc.sub(4, 2) == 2:
        print("sub(a, b) OK")
    else:
        print("sub(a, b) NOT OK")


def test_div():
    if mycalc.div(8, 4) == 2:
        print("div(a, b) OK")
    else:
        print("div(a, b) NOT OK")


def test_sqrt():
    if (mycalc.sqrt(9) - 3) < 0.000000001:
        print("sqrt(a, b) OK")
    else:
        print("sqrt(a, b) NOT OK")


try:
    test_add()
except AssertionError:
    print("test_add(a, b) NOT OK")

test_add()
test_mul()
test_sub()
test_div()
test_sqrt()