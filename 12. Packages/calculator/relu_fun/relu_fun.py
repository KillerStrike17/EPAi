from ..util import f_string_print

@f_string_print
def relu(x:float)->float:
    """
    This function takes in input as integers and returns the
    computed relu value
    """
    return max(0,x)

@f_string_print
def relu_d(x:float)->float:
    """
    This function takes in input in int and returns the
    computed derivaive of relu which is 1 for x > 0
    """
    if x > 0:
        return 1
    return 0