import random

# DOC String Check
def docstring_check(fn):
    """
    This function is used to check the docstring count for each function, it checks if 
    the doc string is of minimum 50 characters

    # Closure:
        mycount:
            This function uses two free varibales i.e. min_count and mydoc. It then checks if mydoc is not 
            empty and then checks its lenght, 
            if the condition is satisfied it returns a bool
    """
    min_count = 50
    
    def mycount()->bool:
        """
        This function returns True, if the docstring has minimum 
        50 characters else it returns false.
        """
        nonlocal min_count
        mydoc = fn.__doc__
        if mydoc and len(mydoc) >= min_count:
            return True
        else:
            return False
    return mycount

# Next Fibonacci -
def myfibonacci():
    """
    Function to generate next fibonacci numbeer
    
    # Closure:
        generate_my_next_number:
            This function takes in two nonlocal variables i.e. first and second and uses thhem 
            to generate next number and returns that

    """
    first = 0
    second = 1
    def generate_my_next_number()-> int:
        """
        This function sums the previous two numbers and returns the generated sum, it also updates the previous
        two numbers with the new value
        """
        nonlocal first,second
        temp = second
        second = first + second
        first = temp
        return second
    return generate_my_next_number

# Function call counter
def add(a:int, b:int)->float:
    """
        This function is used to add two numbers

        # params

            a: int , Number 1
            
            b: int , Number 2

    """
    return a + b

def sub(a:int, b:int)->float:
    """
        This function is used to substract two numbers

        # params

            a: int , Number 1
            
            b: int , Number 2

    """
    return a - b

def mul(a:int, b:int)->int:
    """
        This function is used to multiply two numbers

        # params

            a: int , Number 1
            
            b: int , Number 2

    """
    return a*b

def div(a:int, b:int)->float:
    """
        This function is used to multiply two numbers

        # params

            a: int , Number 1
            
            b: int , Number 2

    """
    if b == 0:
        raise ValueError("Zero se divide karega.. bhagwan h??")
    return a/b


def mycounter(fn):
    """
        This function is used to calculate the number of times a function is being called.

        # params:

            fn: Function whose call will be counted

    """
    count = 0
    def inner(*args,**kwargs)->int:
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        count += 1
        return count
    return inner

mydict = {'add':0,'mul':0,'div':0,'sub':0}


def mycounter_with_global_dict(fn):
    """
        This function is used to calculate the number of times a function is being called.

        # params:

            fn: Function whose call will be counted

    """
    count = mydict[fn.__name__]
    def inner(a:int,b:int)->int:
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        print(fn(a,b))
        count += 1
        mydict[fn.__name__] = count
        return count
    return inner

def mycounter_with_global_dict_2(fn, mydict:dict):
    """
        This function is used to calculate the number of times a function is being called and update the dictionary
        which is passed as a parameter.

        # params:

            fn: Function whose call will be counted

            mydict: Dictionary whose value we need to update

    """
    count = mydict[fn.__name__]
    def inner(a:int,b:int)->int:
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        print(fn(a,b))
        count += 1
        mydict[fn.__name__] = count
        return count
    return inner
