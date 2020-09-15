import pytest
from src.pysigfig.number import Const, Float


def test_initialize():
    x = Float(1.23478755, 3)
    assert x.v == 1.23478755
    assert x.sf == 3
    assert x.lsd == -2
    assert x.str == "1.23E+00"

    x = Float(1.23478755, num_sig_figs=3)
    assert x.v == 1.23478755
    assert x.sf == 3
    assert x.lsd == -2
    assert x.str == "1.23E+00"

    x = Float("1.23478755", num_sig_figs=3)
    assert x.v == 1.23478755
    assert x.sf == 3
    assert x.lsd == -2
    assert x.str == "1.23E+00"

    x = Float(10000, 2)
    assert x.str == "1.0E+04"

    x = Float(10000.0, 2)
    assert x.str == "1.0E+04"

    x = Float("40.1234567")
    assert x.sf == 9
    assert x.str == "4.01234567E+01"

    x = Float("10.0")
    assert x.sf == 3

    x = Float("100")
    assert x.sf == 3

    with pytest.raises(ValueError):
        Float("abc")

    with pytest.raises(OverflowError):
        Float("1E+400")


def test_addition():
    x = Float(1.23478755, 3)
    y = Float(356.1, 4)
    ans = x + y
    assert ans.str == "3.573E+02"

    ans = Float("10.0") + Float("103")
    assert ans.str == "1.13E+02"

    with pytest.raises(TypeError):
        Float("1.23") + "abc"

    with pytest.raises(TypeError):
        "abc" + Float(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Float("1.23") + 5

    with pytest.raises(TypeError):
        5 + Float("1.23")

    with pytest.raises(TypeError):
        Float("1.23") + 5.1

    with pytest.raises(TypeError):
        5.1 + Float("1.23")


def test_subtract():
    x = Float(1.23478755, 3)
    y = Float(356.1, 4)
    ans = x - y
    assert ans.str == "-3.549E+02"

    with pytest.raises(TypeError):
        Float("1.23") - "abc"

    with pytest.raises(TypeError):
        "abc" - Float(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Float("1.23") - 5

    with pytest.raises(TypeError):
        5 - Float("1.23")

    with pytest.raises(TypeError):
        Float("1.23") - 5.1

    with pytest.raises(TypeError):
        5.1 - Float("1.23")


def test_multiply():
    x = Float(1.23478755, 3)
    y = Float(356.1, 4)
    ans = x * y
    assert ans.str == "4.40E+02"

    with pytest.raises(TypeError):
        Float("1.23") * "abc"

    with pytest.raises(TypeError):
        "abc" * Float(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Float("1.23") * 5

    with pytest.raises(TypeError):
        5 * Float("1.23")

    with pytest.raises(TypeError):
        Float("1.23") * 5.1

    with pytest.raises(TypeError):
        5.1 * Float("1.23")


def test_divide():
    x = Float(1.23478755, 3)
    y = Float(356.1, 4)
    ans = x / y
    assert ans.str == "3.47E-03"

    with pytest.raises(TypeError):
        Float("1.23") / "abc"

    with pytest.raises(TypeError):
        "abc" / Float(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Float("1.23") / 5

    with pytest.raises(TypeError):
        5 / Float("1.23")

    with pytest.raises(TypeError):
        Float("1.23") / 5.1

    with pytest.raises(TypeError):
        5.1 / Float("1.23")


def test_negative():
    x = Float(1.23478755, 3)
    ans = -x
    assert ans.str == "-1.23E+00"


def test_invert():
    x = Float(1.23478755, 3)
    ans = ~x
    assert ans.str == "8.10E-01"


def test_combined():
    ans = (Float("1.23145E4") + Float("2.11379E2")) / (Float("1.503E-2") - Float("4.6E-3"))
    assert ans.str == "1.20E+06"


def test_pow():
    x = Float(1.23, 3) ** 3
    assert x.v == 1.23 ** 3
    assert x.sf == 3

    x = Float(1.23, 3) ** Float(3.0, 2)
    assert x.v == 1.23 ** 3.0
    assert x.sf == 3

    x = Float(1.23, 3) ** Const(3.0)
    assert x.v == 1.23 ** 3.0
    assert x.sf == 3

    with pytest.raises(TypeError):
        Float("1.23") ** "abc"

    with pytest.raises(TypeError):
        "abc" ** Float(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Float("1.23") ** 5.1

    with pytest.raises(TypeError):
        5.1 ** Float("1.23")
