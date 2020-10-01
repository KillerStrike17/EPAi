import os,inspect,re,random
import named_tuples as nt
import pytest
from datetime import datetime
from decimal import Decimal
from html import escape

README_CONTENT_CHECK_FOR = [
    'Blood',
    'Location',
    'Age',
    'Person',
    'random',
    'lambda',
    'fake',
    'profile',
    'namedtuple',
    'tuple'
]
input_1 = None
input_2 = None
def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(nt, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"

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
    assert content.count("#") >= 18, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_init_task1():
    global input1
    input1 = nt.init_task1()
    assert 20000 == len(input1),"you need to create 20000 entries"

def test_init_task2():
    global input2
    input2 = nt.init_task2()
    assert 20000 == len(input2),"you need to create 20000 entries"

def test_oldest_person_time_check():
    assert nt.oldest_person_nt(input1)[0] <= nt.oldest_person_dc(input2)[0], "Dictionarys are slow.. how did you made them rabbit instead of tortoise..! Ghodo ki race m ab ghade bhi dondengay"

def test_average_age_time_check():
    assert nt.average_age_nt(input1)[0] <= nt.average_age_dc(input2)[0], "Dictionarys are slow.. how did you made them rabbit instead of tortoise..!Ghodo ki race m ab ghade bhi dondengay"

def test_average_coords_time_check():
    assert nt.average_coords_nt(input1)[0] <= nt.average_coords_dc(input2)[0], "Dictionarys are slow.. how did you made them rabbit instead of tortoise..!Ghodo ki race m ab ghade bhi dondengay"

def test_bloodgroup_test():
    assert nt.average_bloodgroup_nt(input1)[0] <= nt.average_bloodgroup_dc(input2)[0], "Dictionarys are slow.. how did you made them rabbit instead of tortoise..!Ghodo ki race m ab ghade bhi dondengay"

def test_init_task3():
    global input3
    x,y = nt.init_task3()
    input3 = nt.stock_market(x,y)
    assert 100 == len(input3),"you need to create 100 entries"

def test_annot():
    assert bool(nt.init_task1.__annotations__),"annotation missing"
    assert bool(nt.oldest_person_nt.__annotations__),"annotation missing"
    assert bool(nt.average_age_nt.__annotations__),"annotation missing"
    assert bool(nt.average_coords_nt.__annotations__),"annotation missing"
    assert bool(nt.average_bloodgroup_nt.__annotations__),"annotation missing"
    assert bool(nt.init_task2.__annotations__),"annotation missing"
    assert bool(nt.oldest_person_dc.__annotations__),"annotation missing"
    assert bool(nt.average_age_dc.__annotations__),"annotation missing"
    assert bool(nt.average_coords_dc.__annotations__),"annotation missing"
    assert bool(nt.average_bloodgroup_dc.__annotations__),"annotation missing"
    assert bool(nt.init_task3.__annotations__),"annotation missing"

def test_docs():
    assert bool(nt.init_task1.__doc__),"doc string missing"
    assert bool(nt.oldest_person_nt.__doc__),"doc string missing"
    assert bool(nt.average_age_nt.__doc__),"doc string missing"
    assert bool(nt.average_coords_nt.__doc__),"doc string missing"
    assert bool(nt.average_bloodgroup_nt.__doc__),"doc string missing"
    assert bool(nt.init_task2.__doc__),"doc string missing"
    assert bool(nt.oldest_person_dc.__doc__),"doc string missing"
    assert bool(nt.average_age_dc.__doc__),"doc string missing"
    assert bool(nt.average_coords_dc.__doc__),"doc string missing"
    assert bool(nt.average_bloodgroup_dc.__doc__),"doc string missing"
    assert bool(nt.init_task3.__doc__),"doc string missing"
    assert bool(nt.stock_market.__doc__),"doc string missing"