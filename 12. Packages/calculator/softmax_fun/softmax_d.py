from numpy import exp

class Softmax_d:
    
    def __init__(self,x:int)->None:
        self.input_value = x
    
    def __repr__(self)->None:
        return f'Derivative of oftmax value is , hence output of {self.input_value} is: {1-(math.atan(self.input_value)*math.atan(self.input_value))}'