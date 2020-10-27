import math
from ..util import f_string_print

@f_string_print
def log(x:int)->float:
    """
    This function takes in input as integers and returns the
    computed logirithm value
    """
    return math.log(x)

@f_string_print
def log_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of log which is 1/x
    """
    return 1/x