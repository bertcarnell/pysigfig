import numpy as np

import pysigfig.Float


class Const:
    # Data Elements
    v = 0.0

    def __init__(self, value):
        self.v = float(value)

    def __str__(self):
        return str("%g \t (constant)\n" % (self.v))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.v})"

    def __add__(self, other):
        # Const + Float = Float + Const
        return other + self

    def __neg__(self):
        return Const(-1.0 * self.v)

    def __abs__(self):
        return Const(np.abs(self.v))

    def __sub__(self, other):
        # Const - Float = -Float + Const
        return (-other) + self

    def __mul__(self, other):
        # Const * Float = Float * Const
        return other * self

    def __invert__(self):
        return Const(1.0 / self.v)

    def __truediv__(self, other):
        # Const / Float = (1/Float) * Const
        return (~other) * other

    @staticmethod
    def __check_type_comparison(x):
        if not isinstance(x, Const):
            raise TypeError('only Const can be compared using comparison operators in pysigfig')

    def __eq__(self, other):
        Const.__check_type_comparison(other)
        return self.v == other.v

    def __ne__(self, other):
        Const.__check_type_comparison(other)
        return self.v != other.v

    def __lt__(self, other):
        Const.__check_type_comparison(other)
        return self.v < other.v

    def __gt__(self, other):
        Const.__check_type_comparison(other)
        return self.v > other.v

    def __le__(self, other):
        Const.__check_type_comparison(other)
        return self.v <= other.v

    def __ge__(self, other):
        Const.__check_type_comparison(other)
        return self.v >= other.v

    def __pow__(self, other):
        if isinstance(other, Const):
            return Const(self.v**other.v)
        elif isinstance(other, int):
            return Const(self.v**other)
        elif isinstance(other, pysigfig.Float.Float):
            # for base 10 the sig figs of the result are equal to the number of significant decimal places in the exponent
            if self.v == 10.0:
                if other.lsd < 0:
                    return pysigfig.Float.Float(10.0**other.v, int(np.abs(other.lsd)))
                elif other.lsd <= 0:
                    raise pysigfig.Float.Float(10.0**other.v, 1)
            else:
                # for other bases, use the fact that the derivative of x^y is ln(x)*x^y
                # therefore a change of z yields a change in result of z * ln(x)*x^y
                deriv = np.log(self.v) * self.v ** other.v
                new_sf = int(np.floor(other.v - np.log10(deriv * 10**other.lsd))) + 1
                return pysigfig.Float.Float(self.v**other.v, new_sf)
        else:
            raise TypeError('only Float, Const, and int are accepted as exponents of Const')

    def __int__(self):
        return int(self.v)

    def __float__(self):
        return self.v

    def __iadd__(self, other):
        new_float = self + other
        self.__init__(new_float.v)

    def __imul__(self, other):
        new_float = self * other
        self.__init__(new_float.v)

    def __itruediv__(self, other):
        new_float = self / other
        self.__init__(new_float.v)

    def __isub__(self, other):
        new_float = self - other
        self.__init__(new_float.v)
