import pytest
import mycalc
import random
#import sys

#try:
#    import pandas as pd
#except ImportError:
#    pass

#@pytest.mark.skipif(
#    'pandas' not in sys.modules,
#    reason="нужна библиотека Pandas для теста")
#def test_something():
#   ...

#pytest.skip("Не надо проверять калькулятор", allow_module_level=True)

#@pytest.mark.skip("нет никаких сложений, хватит")

def test_add():
    pytest.skip("Нет, спасибо")

@pytest.mark.skipif(random.random() < 0.5,reason="Умножению не повезло")
def test_mul():
    assert mycalc.mul(3, 7) == 21

def test_sub():
    assert mycalc.sub(4, 2) == 2

#def test_div():
#    with pytest.raises(ZeroDivisionError):
#        mycalc.div(1, 0)

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_div():
        mycalc.div(1, 0)

def test_sqrt():
    assert (mycalc.sqrt(9) - 3) < 0.000000001