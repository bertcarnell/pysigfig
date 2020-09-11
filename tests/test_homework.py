from unittest import TestCase

from pysigfig.Float import Float


class TestConst(TestCase):
    def test_homework1(self):
        # https://www.saddleback.edu/faculty/jzoval/worksheets_tutorials/ch1worksheets/worksheet_Sig_Fig_9_11_08.pdf
        self.assertEqual(Float("246.32").sf, 5)
        self.assertEqual(Float("107.854").sf, 6)
        self.assertEqual(Float("100.3").sf, 4)
        self.assertEqual(Float("0.678").sf, 3)
        self.assertEqual(Float("1.008").sf, 4)
        self.assertEqual(Float("0.00340").sf, 3)
        self.assertEqual(Float("14.600").sf, 5)
        self.assertEqual(Float("0.0001").sf, 1)
        self.assertEqual(Float("700000").sf, 6) # package not capable
        self.assertEqual(Float("7E+05").sf, 1)
        self.assertEqual(Float("350.670").sf, 6)
        self.assertEqual(Float("1.0000").sf, 5)
        self.assertEqual(Float("320001").sf, 6)

        self.assertEqual(Float("32.567") + Float("135.0") + Float("1.4567"), Float("169.0"))
        self.assertEqual(Float("246.24") + Float("238.278") + Float("98.3"), Float("582.8"))
        self.assertEqual(Float("658.0") + Float("23.5478") + Float("1345.29"), Float("2026.8"))

        self.assertEqual(Float("23.7") * Float("3.8"), Float("90."))
        self.assertEqual(Float("45.76") * Float("0.25"), Float("11"))
        self.assertEqual(Float("81.04") * Float("0.010"), Float("0.81"))
        self.assertEqual(Float("6.47") * Float("64.5"), Float("417"))
        self.assertEqual(Float("43.678") * Float("64.1"), Float("2.80E+03"))
        self.assertEqual(Float("1.678") / Float("0.42"), Float("4.0"))
        self.assertEqual(Float("28.367") / Float("3.74"), Float("7.58"))
        self.assertEqual(Float("4278") / Float("1.006"), Float("4252"))

    def test_homework2(self):
        # http://www.chemistry.wustl.edu/~coursedev/Online%20tutorials/Plink/sigfigkey.htm
        self.assertEqual(Float("34.6209").sf, 6)
        self.assertEqual(Float("0.003408").sf, 4)
        self.assertEqual(Float("5010.0").sf, 5)
        self.assertEqual(Float("4032.090").sf, 7)

        self.assertEqual(Float("34.683") + Float("58.930") + Float("68.35112"), Float("161.964"))
        self.assertEqual(Float("45001") - Float("56.355") - Float("78.44"), Float("44866"))
        self.assertEqual(Float("0.003") + Float("3.5198") + Float("0.0118"), Float("3.535"))
        self.assertEqual(Float("36.01") - Float("0.4") - Float("15"), Float("21"))

        self.assertEqual(Float("98.1") * Float("0.03"), Float("3"))
        self.assertEqual(Float("57") * Float("7.368"), Float("4.2E+02"))
        self.assertEqual(Float("8.578") / Float("4.33821"), Float("1.977"))
        self.assertEqual(Float("6.90") / Float("2.8952"), Float("2.38"))

