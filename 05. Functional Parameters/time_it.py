import timeit
import math

def time_it(fn, *args,repititions = 1,**kwargs):
    start = timeit.timeit()
    for _ in range(0,repititions):
        value = fn(*args,**kwargs)
    end = timeit.timeit()
    print("Total Time:", end - start)
    speed = end - start
    return value,speed

def myprint(*args,**kwargs):
    print(*args,**kwargs)

def squared_power_list(no, start = 0, end = 1):
    my_list = create_list(start, end)
    squared_list = [i**no for i in my_list]
    return squared_list

def create_list(start = 0, end = 1): 
    if end < start:
        raise ValueError("End cannot be greater than start value, please swap the numbers")
    else:
        return [item for item in range(start, end+1)] 

def polygon_area(length, sides = 3):
    if (sides > 2 and sides < 7) and (length>0):
        area = sides * (length ** 2) / (4 * math.tan(math.pi / sides))
        return area
    else:
        raise ValueError("Sides haves to be greater than 2 or less than 7 and length shouldnt be negative or zero, it should be positive")

def temp_converter(temperature,temp_given_in = 'f'):
    if temp_given_in == 'f':
        if temperature > -459.67:
            celcius_temp = ((temperature - 32)*5)/9
            return celcius_temp
        else:
            raise ValueError("Cant go below absolute zero")
    elif temp_given_in == 'c':
        if temperature>-273.15:
            fahrenheit_temp = (temperature*9)/5 + 32
            return fahrenheit_temp
        else:
            raise ValueError("Cant go below absolute zero")

def speed_converter(speed,dist = 'km',time = 'hr'):
    if speed > 0: 
        if dist == 'km':
            speed = speed
        elif dist == 'm':
            speed = speed * 1000
        elif dist == 'ft':
            speed = speed * 3280.84
        elif dist == 'yrd':
            speed = speed * 1093.61
        if time == 'hr':
            speed = speed
        elif time == 'day':
            speed = speed / 24
        elif time == 'm':
            speed = speed * 60
        elif time == 's':
            speed = speed * 60 * 60
        elif time == 'ms':
            speed = speed * 60 * 60 * 1000
        return speed
    else:
        raise ValueError("Speed has to be greater than zero")

