import pytest
import random
import string
import numeric_types
import os
import inspect
import re
import math
from decimal import Decimal, getcontext

README_CONTENT_CHECK_FOR = [
    '__init__',
    'number_transformation',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__le__',
    '__lt__',
    '__invertsign__',
    '__mul__',
    '__sqrt__',
    '__bool__',
    'test_function_names',
    'test_readme_exits',
    'test_readme_contents',
    'test_readme_proper_discription',
    'test_readme_file_for_formatting',
    'test_indentations',
    'test_qualean_repr',
    'test_qualean_string',
    'test_add_function',
    'test_equal_function_on_random',
    'test_equal_function_on_same_number',
    'test_float_fucntion',
    'test_greater_than_equal_function',
    'test_greater_than_function',
    'test_invert_function',
    'test_less_than_equal_function',
    'test_less_than_function',
    'test_multiply_function',
    'test_true_bool_function',
    'test_false_bool_function',
    'test_check_sqrt',
    'test_get_item',
    'test_hundred_sum',
    'test_million_q_sum',
    'test_million_q_mul',
    'test_and_function_q2_undefined',
    'test_and_function_q1_undefined',
    'test_and_function_both_undefined',
    'test_and_function_both_defined',
    'test_or_function_q2_undefined',
    'test_or_function_q1_undefined',
    'test_or_function_both_undefined',
    'test_or_function_both_defined',
    'test_decimal_upto_ten'
]

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(numeric_types) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2000, "Make your README.md file interesting! Add atleast 500 words"

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
    assert content.count("#") >= 150

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(numeric_types)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_qualean_repr():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    assert r.__repr__() == f'Quanlean: {choice}', 'The representation of the Qualean object does not meet expectations'

def test_qualean_str():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    assert r.__str__() == f'Quanlean: {choice}', 'The print of the Qualean object does not meet expectations'

def test_add_function():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    number= random.randint(0,1000)
    assert r.__add__(number) ==r.value + number, 'This is how you mess up simple addition..'

def test_equal_function_on_random():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    number= round(Decimal(random.uniform(-1,1)),10)
    print(number)
    print(r.value)
    assert r.__eq__(number) == False, 'Equality is a soul of liberty, please maintain it..!!'

def test_equal_function_on_same_number():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    assert r.__eq__(r.value) == True, 'Equality is a soul of liberty, please maintain it..!!'

def test_float_function():
    choice = random.choice([-1,0,1])
    r = numeric_types.Qualean(choice)
    assert type(r.__float__()) == float,'One should be adaptable to change!!'

def test_greater_than_equal_function():
    choice = random.choice([-1,0,1])
    r1 = numeric_types.Qualean(0)
    r2 = numeric_types.Qualean(choice)
    if r2.value < 0:
        assert r1.__ge__(r2.value),'r1 should be greater than equal to r2'
    else:
        assert r2.__ge__(r1.value),'r2 should be greater than equal to r1'

def test_greater_than_function():
    choice = random.choice([-1,1])
    r1 = numeric_types.Qualean(0)
    r2 = numeric_types.Qualean(choice)
    if r2.value < 0:
        assert r1.__gt__(r2.value),'r1 should be greater than r2'
    else:
        assert r2.__gt__(r1.value),'r2 should be greater than r1'
    
def test_invert_function():
    choice = random.choice([-1,0,1])
    r1 = numeric_types.Qualean(choice)
    assert r1.__invertsign__() == -r1.value, 'Its time to show the flip side of yours'

def test_less_than_equal_function():
    choice = random.choice([-1,0,1])
    r1 = numeric_types.Qualean(0)
    r2 = numeric_types.Qualean(choice)
    if r2.value > 0:
        assert r1.__le__(r2.value),'r1 should be less than equal to r2'
    else:
        assert r2.__le__(r1.value),'r2 should be less than equal to r1'

def test_less_than_function():
    choice = random.choice([-1,1])
    r1 = numeric_types.Qualean(0)
    r2 = numeric_types.Qualean(choice)
    if r2.value > 0:
        assert r1.__lt__(r2.value),'r1 should be less than r2'
    else:
        assert r2.__lt__(r1.value),'r2 should be less than r1'

def test_multiply_function():
    choice = random.choice([-1,0,1])
    r1 = numeric_types.Qualean(choice)
    number= random.randint(0,1000)
    assert r1.__mul__(number) == r1.value*number, 'This is how you mess up multiplication'

def test_true_bool_function():
    choice = random.choice([-1,1])
    r1 = numeric_types.Qualean(choice)
    print(r1.value)
    assert r1.__bool__()==True,'Check for trueness' 

def test_false_bool_function():
    choice = random.choice([0])
    r1 = numeric_types.Qualean(choice)
    assert r1.__bool__()==False,'Check for falseness'

def test_check_sqrt():
    choice = random.choice([1,0,-1])
    r1 = numeric_types.Qualean(choice)
    value = r1.get_item()
    if value>=0:
        assert r1.__sqrt__() == Decimal(value).sqrt(), 'Sqrt not working properly'
    else:
        assert r1.__sqrt__() == 'i'+str(Decimal(-value).sqrt()), 'Sqrt not working properly'

def test_get_item():
    choice = random.choice([1,0,-1])
    r1 = numeric_types.Qualean(choice)
    value = r1.get_item()
    assert r1.value == value, 'checking equality'

def test_hundred_sum():
    choice = random.choice([1,0,-1])
    r1 = numeric_types.Qualean(choice)
    sum_res = 0
    for i in range(0,50):
        sum_res+=r1.__add__(r1.value)
    assert sum_res == 100*r1.value, 'It is the right time to visit 5th std.. Need to work on basics of addition..!!'

def test_million_q_sum():
    sum_res = 0
    for _ in range(0,1000000):
        choice = random.choice([1,0,-1])
        r1 = numeric_types.Qualean(choice)
        sum_res +=r1.get_item()
    
    print(sum_res)
    assert math.isclose(sum_res,0) == False, 'Small jodte jao large banate jao..'

def test_million_q_mul():
    sum_res = 0
    for _ in range(0,1000000):
        choice = random.choice([1,0,-1])
        r1 = numeric_types.Qualean(choice)
        sum_res *=r1.get_item()
    
    print(sum_res)
    assert math.isclose(sum_res,0) == True, 'Small smilate jao small banate jao..'

def test_and_function_q2_undefined():
    choice = random.choice([1,-1])
    r2 = 1
    r1 = numeric_types.Qualean(choice)
    assert r1.__and__(r2) == False, 'And Functionality not working'

def test_and_function_q1_undefined():
    choice = random.choice([1,-1])
    r2 = numeric_types.Qualean(choice)
    r1 = numeric_types.Qualean(0)
    assert r1.__and__(r2) == False, 'And Functionality not working'

def test_and_function_both_undefined():
    r2 = numeric_types.Qualean(0)
    r1 = numeric_types.Qualean(0)
    assert r1.__and__(r2) == False, 'And Functionality not working'

def test_and_function_both_defined():
    choice = random.choice([1,-1])
    r2 = numeric_types.Qualean(choice)
    r1 = numeric_types.Qualean(choice)
    assert r1.__and__(r2) == True, 'And Functionality not working'

def test_or_function_q2_undefined():
    choice = random.choice([1,-1])
    r2 = 1
    r1 = numeric_types.Qualean(choice)
    assert r1.__or__(r2) == True, 'Or Functionality not working'

def test_or_function_q1_undefined():
    choice = random.choice([1,-1])
    r2 = numeric_types.Qualean(choice)
    r1 = numeric_types.Qualean(0)
    assert r1.__or__(r2) == True, 'Or Functionality not working'

def test_or_function_both_undefined():
    r2 = numeric_types.Qualean(0)
    r1 = numeric_types.Qualean(0)
    assert r1.__or__(r2) == False, 'Or Functionality not working'

def test_or_function_both_defined():
    choice = random.choice([1,-1])
    r2 = numeric_types.Qualean(choice)
    r1 = numeric_types.Qualean(choice)
    assert r1.__or__(r2) == True, 'Or Functionality not working'

def test_decimal_upto_ten():
    choice = random.choice([-1,1])
    r1 = numeric_types.Qualean(choice)
    if r1.get_item()>0:
        assert len(str(r1.get_item())) == 12, 'Rounding off is not working properly'
    else:
        assert len(str(r1.get_item())) == 13, 'Rounding off is not working properly'

