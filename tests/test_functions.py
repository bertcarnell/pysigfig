import pytest
import numpy as np
import src.pysigfig.functions as func
from src.pysigfig.number import Float


def test_log():
    with pytest.raises(TypeError):
        func.log("a")
    with pytest.raises(TypeError):
        func.log(10.0)

    assert func.log(Float("10.0")).str == "2.30E+00"


def test_ln():
    with pytest.raises(TypeError):
        func.ln("a")
    with pytest.raises(TypeError):
        func.ln(10.0)

    assert func.ln(Float("10.0")).str == "2.30E+00"


def test_log10():
    with pytest.raises(TypeError):
        func.log10("a")
    with pytest.raises(TypeError):
        func.log10(10.0)

    # examples of the rule that log10 of 3 sig figs == number with 3 sig places after the decimal
    assert func.log10(Float("4.85E-6"), basic_rule=True).str == "-5.314E+00"
    assert func.log10(Float("4.85E-6"), basic_rule=False).str == "-5.314E+00"
    assert func.log10(Float("2.73E-05"), basic_rule=True) == Float("-4.564")
    assert func.log10(Float("2.73E-05"), basic_rule=False) == Float("-4.564")
    assert func.log10(Float("9.1E6"), basic_rule=True) == Float("6.96")
    assert func.log10(Float("9.1E6"), basic_rule=False) == Float("6.96")
    # example of breaking the basic rule
    assert func.log10(Float("1E-12"), basic_rule=True) == Float("-12.0")
    assert func.log10(Float("1E-12"), basic_rule=False) == Float("-12")


def test_log2():
    with pytest.raises(TypeError):
        func.log2("a")
    with pytest.raises(TypeError):
        func.log2(10.0)
    assert func.log2(Float("10.0")).str == "3.32E+00"


def test_log1p():
    with pytest.raises(TypeError):
        func.log1p("a")
    with pytest.raises(TypeError):
        func.log1p(10.0)
    assert func.log1p(Float("10.0")).str == "2.40E+00"


def test_exp():
    with pytest.raises(TypeError):
        func.exp("a")
    with pytest.raises(TypeError):
        func.exp(10.0)
    assert func.exp(Float("1.234")).str == "3.43E+00"


def test_exp2():
    with pytest.raises(TypeError):
        func.exp2("a")
    with pytest.raises(TypeError):
        func.exp2(10.0)
    assert func.exp2(Float("1.234")).str == "2.352E+00"
    # TODO:  why does this fail?
    # assert func.exp2(func.log2(Float("1.234"))) == Float("1.234")


def test_exp10():
    with pytest.raises(TypeError):
        func.exp10("a")
    with pytest.raises(TypeError):
        func.exp10(10.0)
    assert func.exp10(Float("1.234")).str == "1.71E+01"

def test_sin():
    with pytest.raises(TypeError):
        func.sin("a")
    with pytest.raises(TypeError):
        func.sin(10.0)

    assert func.sin(Float(0, 3)) == Float("0.00E+00")
    assert func.sin(Float(np.pi/2.0, 2)).v == 1.0
    assert func.sin(Float(np.pi/2.0, 2)).sf == 18
    assert func.sin(Float(np.pi/2.0, 5)).sf == 21

    print("\n")
    # TODO:  Don't like this.  These should all return the same sig figs
    print("sin(pi/2) {0}".format(func.sin(Float(np.pi/2.0 - 0.01, 3))))
    print("sin(pi/2) {0}".format(func.sin(Float(np.pi/2.0 - 0.0001, 3))))
    print("sin(pi/2) {0}".format(func.sin(Float(np.pi/2.0, 3))))
    print("sin(pi/2) {0}".format(func.sin(Float(np.pi/2.0 + 0.0001, 3))))
    print("sin(pi/2) {0}".format(func.sin(Float(np.pi/2.0 + 0.01, 3))))
    print("\n")
    print("sin(pi) {0}".format(func.sin(Float(np.pi - 0.000000000001, 3))))
    print("sin(pi) {0}".format(func.sin(Float(np.pi, 3))))
    print("sin(pi) {0}".format(func.sin(Float(np.pi + 0.000000000001, 3))))
    print("\n")
    print("sin(3 pi / 2) {0}".format(func.sin(Float(3.0*np.pi/2.0, 3))))
    print("sin(2 pi) {0}".format(func.sin(Float(2.0*np.pi, 3))))
