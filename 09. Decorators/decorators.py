import random
from functools import wraps
from datetime import datetime

## 1.1 Odd Seconds Run
def dec_factory_1(time:datetime):
    """
    This is a decorator factory which takes a parameter
    # param:
        time: This variable contains the current time
    """
    def odd_second_runner(fn):
        """
        This is a closure function
        # Param:
            fn : This function takes in function as a parameter
        """
        @wraps(fn)
        def inner(*args,**kwargs):
            """
            This function checks if the seconds is odd, then it will run the function
            else will return a message
            """
            run_dt = time
            print(f'{run_dt}: called {fn.__name__}')
            print(run_dt.second)
            if run_dt.second %2 != 0:
                value = fn(*args,**kwargs)
                return value
            else:
                return f"Abhi Shubh Muhurat nahi h.. samay dekho{run_dt}"
        return inner
    return odd_second_runner

time = datetime.utcnow()
@dec_factory_1(time)
def add(a: int,b: int) -> int:
    """
    This function performs simple addition
    # Param:
        a: int First Integer
        b: int Second Integer
    
    # Return: int
    """
    return a+b

## 1.2 logger

def info(obj):
    results = []
    results.append(f'Class: {obj.__class__.__name__}')
    results.append(f'docs: {obj.__doc__}')
    for k, v in vars(obj).items():
        results.append(f'{k}: {v}')
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class IPL:
    """
    This is IPL class representing each match
    
    Function:
        __init__:
            This function takes in arguments like match_no, team_1, team_2,mom and winner of the 
            match as input and assigns those values to it.
    """
    def __init__(self,match_no, team_1, team_2, mom, winner):
        self.match_no = match_no
        self.team_1 = team_1
        self.team_2 = team_2
        self.mom = mom
        self.winner = winner

    
ipl = IPL(1,'MI','CSK','Ambati Rayudu','CSK')

## 1.3 Authenticate

def authenticate(user_password):
    def auth(fn):
        if user_password ==  'explode':
            @wraps(fn)
            def inner(*args, **kwargs):
                return fn(*args, **kwargs)
            return inner
        else:
            raise ValueError("cannot launch nuke.. need correct password")
    return auth


## 1.4 Timed

def dec_factory_2(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0

            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return timed

@dec_factory_2(5)
def mul(a,b):
    return a*b

print(mul(10,20))

## Previlege access

# class user:
#     def __init__(self,name,access):
#         self.name = name
        
#         self.access = access

# class database:
#     def __init__(self,name, phone, email, age):
#         self.name = 'hero'
#         self.phone = "9999999999"
#         self.email = "hero@zero.com"
#         self.age = 20
#     def __call__(self,fn):
#         def inner(*args)

# userA = user("A","Admin")
# userB = user("B","Boss")
# userC = user("C","Employee")
# userD = user("D","Customer")


