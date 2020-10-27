import pytest
import calculator as c
from calculator import derivatives as d
import os
import inspect
import re

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

# def test_function_has_annotations():
#     functions = inspect.getmembers(c, inspect.isfunction)
#     for function in functions:
#         assert (function.__annotations__ is not {}), "Annotations are missing"

# test_function_has_annotations()