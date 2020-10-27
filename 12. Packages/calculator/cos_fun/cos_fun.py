import math
from ..util import f_string_print

@f_string_print
def cos(x:int)->float:
    """
    This function takes in input in radians and returns the
    computed cos value
    """
    return math.cos(x)

@f_string_print
def cos_d(x:int)->float:
    """
    This function takes in input in radians and returns the
    computed derivaive of cos which is -sin.
    """
    return -math.sin(x)