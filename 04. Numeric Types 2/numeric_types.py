import random
from decimal import Decimal

class Qualean:

    def __init__(self, user_input: Decimal ):
        self.user_choice = user_input
        self.value = self.number_transformation(self.user_choice)
        # print(self.value)

    def __repr__(self):
        return 'Quanlean: {0}'.format(self.user_choice)

    def number_transformation(self, user_choice):
        return self.user_choice*Decimal.from_float(random.uniform(-1,1)).__round__(10)

    def __str__(self):
        return 'Quanlean: {0}'.format(self.user_choice)

    def __add__(self,value):
        return self.value+value

    def __eq__(self, value):
        return self.value == value

    def __float__(self):
        return float(self.value)

    def __ge__(self, value):
        return self.value >= value

    def __gt__(self, value):
        return self.value > value

    def __invertsign__(self):
        return -self.value

    def __le__(self, value):
        return self.value <= value

    def __lt__(self, value):
        return self.value < value

    def __mul__(self, value):
        return self.value*value
 
    def __bool__(self):
        return self.value != 0

    def __sqrt__(self):
        if self.value >= 0:
            return self.value.sqrt()
        else:
            self.value = self.__invertsign__()
            return 'i' + str(self.value.sqrt())

    def get_item(self):
        return self.value

    def __and__(self,other_object):
        if not bool(self.value):
            return False
        else:
            if isinstance(other_object,Qualean) and other_object.value:
                return bool(self.value and other_object.value)
            else:
                return False

    def __or__(self,other_object):
        if self.value:
            return True
        else:
            if isinstance(other_object,Qualean) and other_object.value:
                return bool(self.value or other_object.value)
            else:
                return False