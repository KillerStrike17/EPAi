import pytest
import calculator as c
from calculator import derivatives as d
import os
import inspect
import re
import random
import math

README_CONTENT_CHECK_FOR = [
]

def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(c, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    functions = inspect.getmembers(d, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# def test_readme_contents():
#     readme_words=[word for line in open('README.md', 'r') for word in line.split()]
#     assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

# def test_readme_proper_description():
#     READMELOOKSGOOD = True
#     f = open("README.md", "r")
#     content = f.read()
#     f.close()
#     for c in README_CONTENT_CHECK_FOR:
#         if c not in content:
#             READMELOOKSGOOD = False
#             pass
#     assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

# def test_readme_file_for_formatting():
#     f = open("README.md", "r")
#     content = f.read()
#     f.close()
#     assert content.count("#") >= 25, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_function_has_annotations():
    functions = inspect.getmembers(c, inspect.isfunction)
    for _,function in functions:
        print(_,function)
        assert (function.__annotations__ is not {}), "Annotations are missing"
    functions = inspect.getmembers(d, inspect.isfunction)
    for _,function in functions:
        print(_,function)
        assert (function.__annotations__ is not {}), "Annotations are missing"

def test_function_has_docstring():
    functions = inspect.getmembers(c, inspect.isfunction)
    for _,function in functions:
        print(_,function)
        assert (function.__doc__ is not {}), "Doc Strings are missing"
    functions = inspect.getmembers(d, inspect.isfunction)
    for _,function in functions:
        print(_,function)
        assert (function.__doc__ is not {}), "Doc Strings are missing"

def test_functions():
    value = random.randint(-100,100)
    assert round(c.sin(value))== round(math.sin(value)),"Sin function is not working, you studied this in 10.."
    assert round(c.cos(value)) == round(math.cos(value)),"Cos function is not working, you studied this in 10.."
    assert round(c.tan(value)) == round(math.tan(value)),"Tan function is not working, you studied this in 10.."
    assert round(c.tanh(value)) == round(math.tanh(value)),"Tanh function is not working, you studied this in 10.."
    assert round(c.sigmoid(value)) == round((1 / (1 + math.exp(-value)))),"Sigmoid function is not working, this is the basic of DNN.."
    assert round(c.relu(value)) == round(max(0,value)),"Relu function is not working, this is the basic of DNN,,"
    assert round(c.log(value)) == round(math.log(value)),"Log function is not working, you studied this in 10.."
    assert round(c.e(value))== round(math.exp(value)),"Exp function is not working, you studied this in 10.."

def test_functions_derivatives():
    value = random.randint(-100,100)
    assert round(d.sin_d(value)) == round(math.cos(value)),"Having issues is calculating sin derivative?"
    assert round(d.cos_d(value)) == round(-math.sin(value)),"Having issues is calculating cos derivative?"
    assert round(d.tan_d(value)) == round(1/(math.cos(value)**2)),"Having issues is calculating tan derivative?"
    assert round(d.tanh_d(value)) == round(1-(math.tanh(value)**2)),"Having issues is calculating tan derivative?"
    assert round(d.sigmoid_d(value)) ==round( ((1 / (1 + math.exp(-value)))*(1-(1 / (1 + math.exp(-value)))))),"Having issues is calculating Sigmoid derivative?"
    assert round(d.relu_d(value)) == round(1 if value > 0 else 0),"Having issues is calculating relu derivative?"
    assert round(d.log_d(value)) == round(1/value),"Having issues is calculating log derivative?"
    assert round(d.e_d(value)) == round(math.exp(value)),"Having issues is calculating exp derivative?"