import pytest
import random
import string
from time_it import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext

README_CONTENT_CHECK_FOR = [
    'keyword',
    'positional',
    'tuple',
    'time_it',
    'myprint',
    'squared_power_list',
    'create_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'absolute zero',
    'negative',
    'positive'
]

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(time_it) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 40

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(time_it)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_print():
    assert print( 1, 2, 3,sep='-',end= ' ***\n') == time_it(myprint, 1, 2, 3,sep='-',end= ' ***\n', repititions=5)[0], "You just had to print it man..Sheeeh!!!!!"

def test_create_list_end_gt_start():
    r1 = random.randint(0,500)
    r2 = random.randint(500,1000)
    assert list(range(r1, r2+1))  == create_list(r1,r2), "You are not creating list properly, no point of checking anything further"

def test_create_list_end_lt_start():
    r2 = random.randint(0,500)
    r1 = random.randint(500,1000)
    with pytest.raises(ValueError, match=r".* greater than .*"):
        create_list(r1,r2), "You are not creating list properly, no point of checking anything further"

def test_create_list_end_eq_start():
    r1 = random.randint(0,1000)
    r2 = r1
    assert list(range(r1, r2+1))  == create_list(r1,r2), "You are not creating list properly, no point of checking anything further"

def test_square_power_list_for_positives_for_end_gt_start():
    r1 = random.randint(0,500)
    r2 = random.randint(500,1000)
    pow_no = random.randint(1,10)
    my_list = list(range(r1, r2+1))
    assert [ x**pow_no for x in my_list ] == time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_square_power_list_for_positives_for_end_eq_start():
    r1 = random.randint(0,1000)
    r2 =r1
    pow_no = random.randint(1,10)
    my_list = list(range(r1, r2+1))
    assert [ x**pow_no for x in my_list ] == time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_square_power_list_for_positives_for_end_lt_start():
    r2 = random.randint(0,500)
    r1 = random.randint(500,1000)
    pow_no = random.randint(1,10)
    with pytest.raises(ValueError, match=r".* greater than .*"):
        time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_square_power_list_for_megatives_for_end_gt_start():
    r2 = random.randint(-500,-1)
    r1 = random.randint(-1000,-500)
    pow_no = random.randint(1,10)
    my_list = list(range(r1, r2+1))
    assert [ x**pow_no for x in my_list ] == time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_square_power_list_for_negatives_for_end_eq_start():
    r1 = random.randint(-1000,-1)
    r2 =r1
    pow_no = random.randint(1,10)
    my_list = list(range(r1, r2+1))
    assert [ x**pow_no for x in my_list ] == time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_square_power_list_for_negatives_for_end_lt_start():
    r1 = random.randint(-500,-1)
    r2 = random.randint(-1000,-500)
    pow_no = random.randint(1,10)
    with pytest.raises(ValueError, match=r".* greater than .*"):
        time_it(squared_power_list, pow_no, start=r1, end=r2, repititions=5)[0], "You are not able to square it properly"

def test_polygon_area_for_length_negative():
    length = random.randint(-1000,-1)
    sides = random.randint(3,7)
    with pytest.raises(ValueError, match=r".* negative .*"):
        time_it(polygon_area, length, sides = sides, repititions=5)[0]

def test_polygon_area_for_length_zero():
    length = 0
    sides = random.randint(3,7)
    with pytest.raises(ValueError, match=r".* zero.*"):
        time_it(polygon_area, length, sides = sides, repititions=5)[0]


def test_polygon_area_for_sides_lt_3():
    length = random.randint(1,1000)
    sides = random.randint(-1000,3)
    with pytest.raises(ValueError, match=r".* greater .*"):
        time_it(polygon_area, length, sides = sides, repititions=5)
    
def test_polygon_area_for_sides_gt_7():
    length = random.randint(1,1000)
    sides = random.randint(7,1000)
    with pytest.raises(ValueError, match=r".* less .*"):
        time_it(polygon_area, length, sides = sides, repititions=5)

def test_polygon_area_for_3_sides():
    length = random.randint(1,1000)
    sides = 3
    assert math.isclose(time_it(polygon_area, length, sides = sides, repititions=5)[0],(math.sqrt(3)/4)*math.pow(length,2))==True, 'area calculated in incorrect'

def test_polygon_area_for_4_sides():
    length = random.randint(1,1000)
    sides = 4
    assert math.isclose(time_it(polygon_area, length, sides = sides, repititions=5)[0],math.pow(length,2)) == True,  'area calculated in incorrect'

def test_polygon_area_for_5_sides():
    length = random.randint(1,1000)
    sides = 5
    assert math.isclose(time_it(polygon_area, length, sides = sides, repititions=5)[0],((0.25)*math.sqrt(5 * (5+2*math.sqrt(5))) * math.pow(length,2))) == True,  'area calculated in incorrect'

def test_polygon_area_for_6_sides():
    length = random.randint(1,1000)
    sides = 6
    assert math.isclose(time_it(polygon_area, length, sides = sides, repititions=5)[0],((0.5)*(3*math.sqrt(3))*math.pow(length,2))) == True,  'area calculated in incorrect'

def test_temp_converter_lt_absolute_zero_for_f():
    temp = random.uniform(-1000,-459.67,)
    with pytest.raises(ValueError, match=r".* absolute zero.*"):
        time_it(temp_converter, temp, temp_given_in = 'f', repititions=100)

def test_temp_converter_lt_absolute_zero_for_c():
    temp = random.uniform(-1000,-273.15)
    with pytest.raises(ValueError, match=r".* absolute zero.*"):
        time_it(temp_converter, temp, temp_given_in = 'c', repititions=100)

def test_temp_converter_f_to_c():
    temp = random.uniform(-459.66,1000)
    assert math.isclose(time_it(temp_converter, temp, temp_given_in = 'f', repititions=100)[0], ((temp - 32) / 1.8))==True, "Temperature Conversion from Fahrenheit to Celcius is not working"

def test_temp_converter_c_to_f():
    temp = random.uniform(-273.14,1000)
    assert math.isclose(time_it(temp_converter, temp, temp_given_in = 'c', repititions=100)[0],( (temp * 1.8) + 32))==True, "Temperature Conversion from Fahrenheit to Celcius is not working"

def test_speed_conversion_negative_speed_test():
    speed = random.uniform(-1000,0)
    with pytest.raises(ValueError, match=r".* greater than .*"):
        time_it(speed_converter, speed, dist='km', time='m', repititions=200)
    
def test_speed_converion_km_per_hr():
    speed = random.uniform(0,1000)
    assert time_it(speed_converter, speed, dist='km', time='hr', repititions=200)[0] == speed, "the input was in km/hr, you literally just had to return it back and you screwed it.. "

def test_speed_converion_km_per_day():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='km', time='day', repititions=200)[0],speed/24)==True, "the input was in km/hr, you literally just had to divide by 24 and you screwed it.. "

def test_speed_converion_km_per_min():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='km', time='m', repititions=200)[0],speed*60)==True, "the input was in km/hr, you literally just had to multiply it by 60 and you screwed it.. "

def test_speed_converion_km_per_second():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='km', time='s', repititions=200)[0], speed*3600)==True, "the input was in km/hr, you literally just had to multiply it by 3600 and you screwed it.. "

def test_speed_converion_km_per_micro_seconds():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='km', time='ms', repititions=200)[0],speed*3600000)==True, "the input was in km/hr, you literally just had to multiply it by 3600000 and you screwed it.. "

def test_speed_converion_m_per_hr():
    speed = random.uniform(0,1000)
    assert time_it(speed_converter, speed, dist='m', time='hr', repititions=200)[0] == speed*1000, "the input was in km/hr, you literally just had to multiply it by 1000 and you screwed it.. "

def test_speed_converion_m_per_day():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='m', time='day', repititions=200)[0],speed/24*1000)==True, "the input was in km/hr, you literally just had to divide by 24 and multiply it by 1000 and you screwed it.. "

def test_speed_converion_m_per_min():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='m', time='m', repititions=200)[0],speed*60000)==True, "the input was in km/hr, you literally just had to multiply it by 60000 and you screwed it.. "

def test_speed_converion_m_per_second():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='m', time='s', repititions=200)[0], speed*3600000)==True, "the input was in km/hr, you literally just had to multiply it by 3600000 and you screwed it.. "

def test_speed_converion_m_per_micro_seconds():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='m', time='ms', repititions=200)[0],speed*3600000000)==True, "the input was in km/hr, you literally just had to multiply it by 3600000000 and you screwed it.. "

def test_speed_converion_yrd_per_hr():
    speed = random.uniform(0,1000)
    assert time_it(speed_converter, speed, dist='yrd', time='hr', repititions=200)[0] == speed*1093.61, "the input was in km/hr, you literally just had to multiply it by 1093.61 and you screwed it.. "

def test_speed_converion_yrd_per_day():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='yrd', time='day', repititions=200)[0], speed/24*1093.61)==True, "the input was in km/hr, you literally just had to divide by 24 and multiply it by 1093.61 and you screwed it.. "

def test_speed_converion_yrd_per_min():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='yrd', time='m', repititions=200)[0],speed*60*1093.61)==True, "the input was in km/hr, you literally just had to multiply it by 60*1093.61 and you screwed it.. "

def test_speed_converion_yrd_per_second():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='yrd', time='s', repititions=200)[0], speed*3600*1093.61)==True, "the input was in km/hr, you literally just had to multiply it by 36000*1093.61 and you screwed it.. "

def test_speed_converion_yrd_per_micro_seconds():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='yrd', time='ms', repititions=200)[0],speed*3600000*1093.61)==True, "the input was in km/hr, you literally just had to multiply it by 3600000*1093.61 and you screwed it.. "

def test_speed_converion_ft_per_hr():
    speed = random.uniform(0,1000)
    assert time_it(speed_converter, speed, dist='ft', time='hr', repititions=200)[0] == speed*3280.84, "the input was in km/hr, you literally just had to multiply it by 3280.84 and you screwed it.. "

def test_speed_converion_ft_per_day():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='ft', time='day', repititions=200)[0], speed/24*3280.84)==True, "the input was in km/hr, you literally just had to divide by 24 and multiply it by3280.84 and you screwed it.. "

def test_speed_converion_ft_per_min():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='ft', time='m', repititions=200)[0],speed*60*3280.84)==True, "the input was in km/hr, you literally just had to multiply it by 60*3280.84 and you screwed it.. "

def test_speed_converion_ft_per_second():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='ft', time='s', repititions=200)[0], speed*3600*3280.84)==True, "the input was in km/hr, you literally just had to multiply it by 36000*3280.84 and you screwed it.. "

def test_speed_converion_ft_per_micro_seconds():
    speed = random.uniform(0,1000)
    assert math.isclose(time_it(speed_converter, speed, dist='ft', time='ms', repititions=200)[0],speed*3600000*3280.84)==True, "the input was in km/hr, you literally just had to multiply it by 3600000*3280.84 and you screwed it.. "
    