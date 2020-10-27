import math
from ..util import f_string_print

@f_string_print
def sigmoid(x:int)->float:
    """
    This function takes in input as integers and returns the
    computed sigmoid value
    """
    return 1 / (1 + math.exp(-x))

@f_string_print
def sigmoid_d(x:int)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of Sigmoid which is sigmoid(x)*(1-Sigmoid(x))
    """
    return sigmoid(x)*(1-sigmoid(x))