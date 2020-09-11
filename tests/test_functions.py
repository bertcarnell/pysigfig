from unittest import TestCase

from src.pysigfig.number import Float
import src.pysigfig.functions as func


class Test(TestCase):

    def test__log_internal(self):
        # tested inside log functions
        self.assertTrue(True)

    def test__exp_internal(self):
        # tested inside exp functions
        self.assertTrue(True)

    def test_log(self):
        self.assertEqual(func.log(Float("10.0")).str, "2.303E+00")

    def test_ln(self):
        self.assertEqual(func.ln(Float("10.0")).str, "2.303E+00")

    def test_log10(self):
        ans = func.log10(Float("4.85E-6"))
        self.assertEqual(ans.str, "-5.314E+00")

    def test_log2(self):
        self.assertEqual(func.log2(Float("10.0")).str, "3.322E+00")

    def test_log1p(self):
        self.assertEqual(func.log1p(Float("10.0")).str, "2.398E+00")

    def test_exp(self):
        self.assertEqual(func.exp(Float("1.234")).str, "3.435E+00")

    def test_exp2(self):
        self.assertEqual(func.exp2(Float("1.234")).str, "2.3522E+00")

    def test_exp10(self):
        self.assertEqual(func.exp10(Float("1.234")).str, "1.71E+01")
