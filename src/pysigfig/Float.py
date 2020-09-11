import re

import numpy as np

import pysigfig.functions as func
import pysigfig.Const


class Float:
    # Data Elements
    v = 0.0
    sf = int(2)
    # least significant digit is defined as the exponent of the 10 that places a 1 in the same place as the least significant digit
    lsd = -1
    sv = ""

    @staticmethod
    def __find_largest_lsd(x, y):
        if x.lsd > y.lsd:
            new_lsd = x.lsd
        else:
            new_lsd = y.lsd
        return new_lsd

    @staticmethod
    def __find_smallest_sf(x, y):
        if x.sf > y.sf:
            new_sf = y.sf
        else:
            new_sf = x.sf
        return new_sf

    def __init__(self, value, num_sig_figs=None):
        if isinstance(value, str):
            # if exponential 2.3450E1223
            m = re.match("[-0-9.]*[Ee][0-9+-]*", value)
            if m:
                new_str = (value.split("E"))[0].replace("-", "").replace(".", "")
            else:
                new_str = re.sub("^[0.]*", "", value).replace(".", "")
            self.v = float(value)
            self.sf = len(new_str)
            self.lsd = func._calc_lsd(self.v, self.sf)
            rounded_value = np.around(self.v, decimals=-self.lsd)
            self.sv = "{0:.{1:d}E}".format(float(rounded_value), (self.sf - 1))
        else:
            # convert to float so that the initialization can handle ints or floats
            self.v = float(value)
            self.sf = int(num_sig_figs)
            self.lsd = func._calc_lsd(self.v, self.sf)
            rounded_value = np.around(self.v, decimals=-self.lsd)
            self.sv = "{0:.{1:d}E}".format(float(rounded_value), (self.sf - 1))

    def __str__(self):
        return str("%s \t (significant figures = %i) (least significant digit = %g)\n" % (self.sv, self.sf, (10.0 ** self.lsd)))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.v}, {self.sf})"

    def __add__(self, other):
        if isinstance(other, Float):
            value = self.v + other.v
            new_lsd = Float.__find_largest_lsd(self, other)
            new_sf = func._calc_sf(value, new_lsd)
            return Float(value, new_sf)
        elif isinstance(other, pysigfig.Const):
            value = self.v + other.v
            new_lsd = func._calc_lsd(value, self.sf)
            new_sf = func._calc_sf(value, new_lsd)
            return Float(value, new_sf)
        else:
            raise TypeError('only Floats and Const can be added or subtracted in pysigfig')

    def __neg__(self):
        value = -1.0 * self.v
        return Float(value, self.sf)

    def __abs__(self):
        value = np.abs(self.v)
        return Float(value, self.sf)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Float):
            value = self.v * other.v
            new_sf = Float.__find_smallest_sf(self, other)
            return Float(value, new_sf)
        elif isinstance(other, pysigfig.Const):
            value = self.v * other.v
            return Float(value, self.sf)
        else:
            raise TypeError('only Floats and Const can be multiplied or divided in pysigfig')

    def __invert__(self):
        value = 1.0 / self.v
        return Float(value, self.sf)

    def __truediv__(self, other):
        return self * (~other)

    @staticmethod
    def __check_type_comparison(x):
        if not isinstance(x, Float):
            raise TypeError('only Floats can be compared using comparison operators in pysigfig')

    def __eq__(self, other):
        Float.__check_type_comparison(other)
        '''Two numbers are the same if their significant digit representations are the same'''
        return self.sv == other.sv

    def __ne__(self, other):
        Float.__check_type_comparison(other)
        return self.sv != other.sv

    def __lt__(self, other):
        Float.__check_type_comparison(other)
        return (self.v < other.v) & (self.sv != other.sv)

    def __gt__(self, other):
        Float.__check_type_comparison(other)
        return (self.v > other.v) & (self.sv != other.sv)

    def __le__(self, other):
        Float.__check_type_comparison(other)
        return (self.v < other.v) | (self.sv == other.sv)

    def __ge__(self, other):
        Float.__check_type_comparison(other)
        return (self.v > other.v) | (self.sv == other.sv)

    def __pow__(self, other):
        if isinstance(other, pysigfig.Const):
            value = self.v**other.v
            return Float(value, self.sf)
        elif isinstance(other, int):
            value = self.v**other
            return Float(value, self.sv)
        elif isinstance(other, Float):
            # interpretation is that the exponent is the number of times we will multiply the number times iteself
            # even if we are uncertain about the exponent, the sig figs of the base control
            value = self.v**other.v
            return Float(value, self.sf)
        else:
            raise TypeError('only Float, Const, and int are accepted as exponents of Floats')

    def __int__(self):
        return int(self.v)

    def __float__(self):
        return self.v

    def __iadd__(self, other):
        new_float = self + other
        self.__init__(new_float.v, new_float.sf)

    def __imul__(self, other):
        new_float = self * other
        self.__init__(new_float.v, new_float.sf)

    def __itruediv__(self, other):
        new_float = self / other
        self.__init__(new_float.v, new_float.sf)

    def __isub__(self, other):
        new_float = self - other
        self.__init__(new_float.v, new_float.sf)

