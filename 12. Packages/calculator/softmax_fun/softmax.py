import numpy as np

class Softmax:

    def __init__(x):
        self.input_value = x
    
    def __repr__(self):
        e = exp(self.input_value)
	    value = e / e.sum()
        return f'Softmax value of {self.input_value} is: {value}'