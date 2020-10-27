import math
from ..util import f_string_print

@f_string_print
def tan(x:int)->float:
    """
    This function takes in input as integers and returns the
    computed tan value
    """
    return math.tan(x)

@f_string_print
def tan_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of tan which is sec^2(x)
    """
    return 1/(math.cos(x)*math.cos(x))