import os,inspect,re,random
import decorators as dc
import pytest
from datetime import datetime

README_CONTENT_CHECK_FOR = [
    'generate_my_next_number',
    'min_count',
    'docstring',
    'fibonacci',
    'called',
    'closure',
    'global',
    'count',
    'dictioanry',
    'variable'
]
def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(dc, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
# def test_readme_contents():
#     readme_words=[word for line in open('README.md', 'r') for word in line.split()]
#     assert len(readme_words) >= 550, "Make your README.md file interesting! Add atleast 500 words"

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



def test_dec_factory_1():
    time = datetime.utcnow()

    @dc.dec_factory_1(time)
    def add(a,b):
        return a+b
    
    if time.second %2 == 0:
        assert add(1,3) == "Abhi Shubh Muhurat nahi h.. samay dekho"+str(time)
    else:
        assert add(1,3) == 4

def test_info():
    ipl = dc.IPL(1,'MI','CSK','Ambati Rayudu','CSK')
    check = ['Class: IPL', 'docs: \n    This is IPL class representing each match\n    \n    Function:\n        __init__:\n            This function takes in arguments like match_no, team_1, team_2,mom and winner of the \n            match as input and assigns those values to it.\n    ', 'match_no: 1', 'team_1: MI', 'team_2: CSK', 'mom: Ambati Rayudu', 'winner: CSK']
    assert check == ipl.debug(), "You are not able to generate proper info, just print what you class does.. thats it.."

def test_authenticate():

    userpass = "explode"
    @dc.authenticate(userpass)
    def plant_bomb():
        return "bomb planted"
    assert plant_bomb() == "bomb planted"
    userpass = "dont explode"

    with pytest.raises(ValueError):
        @dc.authenticate(userpass)
        def plant_bomb():
            return "bomb planted"

def test_dec_factory_2():
    @dc.dec_factory_2(5)
    def mul(a,b):
        return a*b
    assert mul(1,3) == 3, "Multiplication is not that tough"





    
