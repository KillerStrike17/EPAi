import math
from ..util import f_string_print

@f_string_print
def softmax(x:list)->list:
    """
    This function takes in input in a form of list and returns the
    computed softmax value of the list in the form of list.
    """
    max_value = max(x)
    total = [math.exp(i - max_value) for i in x]
    result = [i/sum(total) for i in total]
    return result

@f_string_print
def softmax_d(x:list)->list:
    """
    This function takes in input in list and returns the
    computed derivaive of softmax in the form of list.
    """
    
    max_list = max(x)
    total = [math.exp(i - max_list) for i in x]
    softmax_out = [i/sum(total) for i in total]

    result = []
    for idx, _ in enumerate(x):
        res_index = []
        for sm_idx, softmax_val in enumerate(softmax_out):
            if idx == sm_idx:
                sm_diff = softmax_val * (1 - softmax_val)
            else:
                sm_diff = -1 * softmax_val * softmax_out[idx]
            res_index.append(sm_diff)
        result.append(res_index)

    return result