import pytest

from src.pysigfig.number import Const, Float


def test_initialize():
    x = Const(2)
    assert x.v == 2.0

    with pytest.raises(ValueError):
        Const("abc")


def test_pow():
    ans = Const(10.0) ** (Float("5.484"))
    assert isinstance(ans, Float)
    assert ans.str == "3.05E+05"

    ans = Const(10.0) ** (Float("5.483"))
    assert isinstance(ans, Float)
    assert ans.str == "3.04E+05"

    ans = Const(10.0) ** (Float("5.485"))
    assert isinstance(ans, Float)
    assert ans.str == "3.05E+05"


def test_addition():
    x = Const(1.23478755)
    y = Const(356.1)
    ans = x + y
    assert ans.v == 1.23478755 + 356.1

    ans = Float("10.0") + Float("103")
    assert ans.v == 10.0 + 103

    with pytest.raises(TypeError):
        Const("1.23") + "abc"

    with pytest.raises(TypeError):
        "abc" + Const(1.23)

    with pytest.raises(TypeError):
        Const("1.23") + 5

    with pytest.raises(TypeError):
        5 + Const("1.23")

    with pytest.raises(TypeError):
        Const("1.23") + 5.1

    with pytest.raises(TypeError):
        5.1 + Const("1.23")


def test_subtract():
    x = Const(1.23478755)
    y = Const(356.1)
    ans = x - y
    assert ans.v == 1.23478755 - 356.1

    with pytest.raises(TypeError):
        Const("1.23") - "abc"

    with pytest.raises(TypeError):
        "abc" - Const(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Const("1.23") - 5

    with pytest.raises(TypeError):
        5 - Const("1.23")

    with pytest.raises(TypeError):
        Const("1.23") - 5.1

    with pytest.raises(TypeError):
        5.1 - Const("1.23")


def test_multiply():
    x = Const(1.23478755)
    y = Const(356.1)
    ans = x * y
    assert ans.v == 1.23478755 * 356.1

    with pytest.raises(TypeError):
        Const("1.23") * "abc"

    with pytest.raises(TypeError):
        "abc" * Const(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Const("1.23") * 5

    with pytest.raises(TypeError):
        5 * Const("1.23")

    with pytest.raises(TypeError):
        Const("1.23") * 5.1

    with pytest.raises(TypeError):
        5.1 * Const("1.23")


def test_divide():
    x = Const(1.23478755)
    y = Const(356.1)
    ans = x / y
    assert ans.v == 1.23478755 / 356.1

    with pytest.raises(TypeError):
        Const("1.23") / "abc"

    with pytest.raises(TypeError):
        "abc" / Const(1.23, num_sig_figs=3)

    with pytest.raises(TypeError):
        Const("1.23") / 5

    with pytest.raises(TypeError):
        5 / Const("1.23")

    with pytest.raises(TypeError):
        Const("1.23") / 5.1

    with pytest.raises(TypeError):
        5.1 / Const("1.23")
