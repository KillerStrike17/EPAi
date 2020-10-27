import math
from ..util import f_string_print

@f_string_print
def tanh(x:int)->float:
    """
    This function takes in input as integers and returns the
    computed tanh value
    """
    return 1 / (1 + math.exp(-x))

@f_string_print
def tanh_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of tanh which is 1-tanh^2(x)
    """
    return 1 - (tanh(x)**2)