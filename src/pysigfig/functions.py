import numpy as np
from src.pysigfig.number import Const, Float


def _log_internal(x, value):
    if isinstance(x, Float):
        value = float(value)
        new_sf = Float._calc_sf(value, -x.sf)
        return Float(value, new_sf)
    elif isinstance(x, Const):
        return Const(value)
    else:
        raise TypeError("x must be a Float or Const object")


def _exp_internal(base, expo):
    if isinstance(expo, Float):
        return base ** expo
    else:
        raise TypeError("exponent must be a Float object")


def log(x):
    return _log_internal(x, np.log(x.v))


def ln(x):
    return _log_internal(x, np.log(x.v))


def log10(x):
    return _log_internal(x, np.log10(x.v))


def log2(x):
    return _log_internal(x, np.log2(x.v))


def log1p(x):
    return _log_internal(x, np.log1p(x.v))


def exp(x):
    return _exp_internal(Const(np.exp(1.0)), x)


def exp2(x):
    return _exp_internal(Const(2.0), x)


def exp10(x):
    return _exp_internal(Const(10.0), x)
