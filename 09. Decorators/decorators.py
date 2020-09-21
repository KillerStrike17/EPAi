import random

from functools import wraps
from datetime import datetime

# def odd_second_runner(fn):

#     @wraps(fn)
#     def inner(*args,**kwargs):
#         run_dt = datetime.utcnow()
        
#         print(f'{run_dt}: called {fn.__name__}')
#         print(run_dt.second)
#         if run_dt.second %2 != 0:
#             value = fn(*args,**kwargs)
#             return value
#         else:
#             return f"Abhi Shubh Muhurat nahi h.. samay dekho{run_dt}"
#     return inner


# @odd_second_runner
# def add(a,b):
#     return a+b

# print(add(1,2))

# def info(obj):
#     results = []
#     results.append(f'time:{datetime.utcnow()}')
#     results.append(f'Class: {obj.__class__.__name__}')
#     results.append(f'id: {hex(id(obj))}')
#     results.append(f'docs: {obj.__doc__}')
#     for k, v in vars(obj).items():
#         results.append(f'{k}: {v}')
#     return results

# def debug_info(cls):
#     cls.debug = info
#     return cls

# @debug_info
# class IPL:
#     def __init__(self,match_no, team_1, team_2, mom, winner):
#         self.match_no = match_no
#         self.team_1 = team_1
#         self.team_2 = team_2
#         self.mom = mom
#         self.winner = winner
    
#     def start():
#         return "India;s Biggest Festival"
    
# ipl = IPL(1,'MI','CSK','Ambati Rayudu','CSK')
# print(ipl.debug())

def set_password():
    password = ""
    def inner():
        nonlocal password
        if password == "":
            password = input()
        return password
    return inner

current_password = set_password()

def authenticate(fn, current_password, user_password):
    if user_password ==  current_password():
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        return inner
    else:
        print( " you are not eligible for the Y+ security")
    
def y_plus(name):
    return f"{name} is eligible"

y_plus_check = authenticate(y_plus,current_password,'y+ security')
print(y_plus_check("Deepika"))

