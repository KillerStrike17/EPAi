import random
from functools import wraps
from datetime import datetime
from functools import singledispatch
from decimal import Decimal
from html import escape

## 1.1 Odd Seconds Run

def dec_factory_1(time:datetime)->'Function':
    """
    This is a decorator factory which takes a parameter
    # param:
        time: This variable contains the current time
    """
    def odd_second_runner(fn: 'function'):
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
# Defining Decorator
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

def info(obj)->list:
    """
    This function takes in object as an input, information is extracted
    from this class object and stored in list, the list is returned
    """
    results = []
    results.append(f'Class: {obj.__class__.__name__}')
    results.append(f'docs: {obj.__doc__}')
    for k, v in vars(obj).items():
        results.append(f'{k}: {v}')
    return results

def debug_info(cls:'class'):
    """
    This function takes in class and calls info function
    """
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

def authenticate(user_password:str):
    """
    This function takes in user password and checks with the one 
    stored in the database and if it matches it executes the function 
    else raises error
    """
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

def dec_factory_2(reps:int):
    """
    This function takes in integer as an input and runs the function 
    reps number of time
    """
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

# print(mul(10,20))

## Previlege access

def access_level(level:int):
    """
    This function takes in integer which defines the access level
    and then checks if the function belongs to that level, if it does
    then runs it else raises an error
    """
    levels = {1:('high','mid','low','no'),2:('mid','low','no'),3:('low','no'),4:('no')}
    def access_func(fn):
        func_list = levels.get(level)
        if fn.__name__ in func_list:
            @wraps(fn)
            def inner(*args,**kwargs):
                return fn(*args,**kwargs)
            return inner

        else:
            raise ValueError("Pehle Clearance Lao")
    return access_func

@singledispatch
def htmlize(input: 'input argument') -> str :
    '''
    function to htmlize the input based on the type of input.
    this is a default initializer.
    '''
    return escape(str(input))

@htmlize.register(int)
def html_int(input: int) -> str:
    '''
    converts int in html formats
    '''
    return f'{input}(<i>{str(hex(input))}</i>)'

@htmlize.register(Decimal)
@htmlize.register(float)
def html_real(input: float) -> str:
    '''
    converts reals to html function
    '''
    return f'{round(input, 2)}'

@htmlize.register(str)
def html_str(input: str) -> str:
    '''
    fconvert string to html format
    '''
    return escape(input).replace('\n', '<br/>\n')

@htmlize.register(tuple)
@htmlize.register(list)
@htmlize.register(set)
@htmlize.register(frozenset)
def html_sequence(input) ->str:
    '''
    converts a sequence in html format
    '''
    items = (f'<li>{escape(str(item))}</li>' for item in input)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(input: dict) -> str:
    '''
    converts dictionary in html format
    '''
    items = (f'<li>{k}={v}</li>' for k, v in input.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
