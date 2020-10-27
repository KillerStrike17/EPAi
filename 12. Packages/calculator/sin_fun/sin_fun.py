import math
from ..util import f_string_print

@f_string_print
def sin(x:int)->float:
    """
    This function takes in input as redians and returns the
    computed sin value
    """
    return math.sin(x)

@f_string_print
def sin_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivative of sin which is cos(x)
    """
    return math.cos(x)
