from unittest import TestCase
from pysigfig.Const import Const
from pysigfig.Float import Float


class TestConst(TestCase):
    def test_initialize(self):
        x = Const(2)
        self.assertEqual(x.v, 2.0)

    def test_pow(self):
        ans = Const(10.0)**(Float("5.484"))
        self.assertTrue(ans.sv, "3.05E+05")

        ans = Const(10.0)**(Float("5.483"))
        self.assertTrue(ans.sv, "3.04E+05")

        ans = Const(10.0)**(Float("5.485"))
        self.assertTrue(ans.sv, "3.05E+05")
