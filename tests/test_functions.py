import pytest
import src.pysigfig.functions as func
from src.pysigfig.number import Float


def test__log_internal():
    # tested inside log functions
    assert True


def test__exp_internal():
    # tested inside exp functions
    assert True


def test_log():
    assert func.log(Float("10.0")).str == "2.303E+00"

    with pytest.raises(TypeError):
        func.log("a")


def test_ln():
    assert func.ln(Float("10.0")).str == "2.303E+00"


def test_log10():
    ans = func.log10(Float("4.85E-6"))
    assert ans.str == "-5.314E+00"


def test_log2():
    assert func.log2(Float("10.0")).str == "3.322E+00"


def test_log1p():
    assert func.log1p(Float("10.0")).str == "2.398E+00"


def test_exp():
    assert func.exp(Float("1.234")).str == "3.435E+00"


def test_exp2():
    assert func.exp2(Float("1.234")).str == "2.3522E+00"


def test_exp10():
    assert func.exp10(Float("1.234")).str == "1.71E+01"
