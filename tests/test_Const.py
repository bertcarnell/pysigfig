from unittest import TestCase
from pysigfig.Const import Const

class TestConst(TestCase):
    def test_initialize(self):
        x = Const(2)
        self.assertEqual(x.v, 2.0)
