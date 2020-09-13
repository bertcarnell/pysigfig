from unittest import TestCase

from src.pysigfig.number import Const, Float


class TestFloat(TestCase):
    def test_initialize(self):
        x = Float(1.23478755, 3)
        self.assertEqual(x.v, 1.23478755)
        self.assertEqual(x.sf, 3)
        self.assertEqual(x.lsd, -2)
        self.assertEqual(x.str, "1.23E+00")

        x = Float(10000, 2)
        self.assertEqual(x.str, "1.0E+04")

        x = Float("40.1234567")
        self.assertEqual(x.sf, 9)
        self.assertEqual(x.str, "4.01234567E+01")

        x = Float("10.0")
        self.assertEqual(x.sf, 3)

        x = Float("100")
        self.assertEqual(x.sf, 3)

    def test_addition(self):
        x = Float(1.23478755, 3)
        y = Float(356.1, 4)
        ans = x + y
        self.assertEqual(ans.str, "3.573E+02")

        ans = Float("10.0") + Float("103")
        self.assertEqual(ans.str, "1.13E+02")

    def test_subtract(self):
        x = Float(1.23478755, 3)
        y = Float(356.1, 4)
        ans = x - y
        self.assertEqual(ans.str, "-3.549E+02")

    def test_multiply(self):
        x = Float(1.23478755, 3)
        y = Float(356.1, 4)
        ans = x * y
        self.assertEqual(ans.str, "4.40E+02")

    def test_divide(self):
        x = Float(1.23478755, 3)
        y = Float(356.1, 4)
        ans = x / y
        self.assertEqual(ans.str, "3.47E-03")

    def test_negative(self):
        x = Float(1.23478755, 3)
        ans = -x
        self.assertEqual(ans.str, "-1.23E+00")

    def test_invert(self):
        x = Float(1.23478755, 3)
        ans = ~x
        self.assertEqual(ans.str, "8.10E-01")

    def test_combined(self):
        ans = (Float("1.23145E4") + Float("2.11379E2")) / (Float("1.503E-2") - Float("4.6E-3"))
        self.assertEqual(ans.str, "1.20E+06")
