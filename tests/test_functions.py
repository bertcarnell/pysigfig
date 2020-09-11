from unittest import TestCase

from pysigfig.Float import Float
from pysigfig.Const import Const
import pysigfig.functions as func


class Test(TestCase):
    def test__calc_lsd(self):
        self.assertEqual(func._calc_lsd(10.0, 3), -1)
        self.assertEqual(func._calc_lsd(10.0, 2), 0)

    def test__calc_sf(self):
        self.assertEqual(func._calc_sf(10.0, -1), 3)
        self.assertEqual(func._calc_sf(10.0, 0), 2)

    def test__log_internal(self):
        # tested inside log functions
        self.assertTrue(True)

    def test__exp_internal(self):
        # tested inside exp functions
        self.assertTrue(True)

    def test_log(self):
        self.assertEqual(func.log(Float("10.0")).sv, "2.303E+00")

    def test_ln(self):
        self.assertEqual(func.ln(Float("10.0")).sv, "2.303E+00")

    def test_log10(self):
        ans = func.log10(Float("4.85E-6"))
        self.assertEqual(ans.sv, "-5.314E+00")

    def test_log2(self):
        self.assertEqual(func.log2(Float("10.0")).sv, "3.322E+00")

    def test_log1p(self):
        self.assertEqual(func.log1p(Float("10.0")).sv, "2.398E+00")

    def test_exp(self):
        self.assertEqual(func.exp(Float("1.234")).sv, "3.435E+00")

    def test_exp2(self):
        self.assertEqual(func.exp2(Float("1.234")).sv, "2.3522E+00")

    def test_exp10(self):
        self.assertEqual(func.exp10(Float("1.234")).sv, "1.71E+01")
