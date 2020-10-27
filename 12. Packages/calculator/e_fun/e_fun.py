import math
from ..util import f_string_print

@f_string_print
def e(x:int)->float:
    """
    This function takes in input as integers and returns the
    computed exponential value
    """
    return math.exp(x)

@f_string_print
def e_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of exp which is exp
    """
    return math.exp(x)