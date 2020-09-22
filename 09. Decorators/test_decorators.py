import os,inspect,re,random
import decorators as dc
import pytest
from datetime import datetime
from decimal import Decimal
from html import escape

README_CONTENT_CHECK_FOR = [
    'authenticate',
    'password',
    'function',
    'log',
    'timed',
    'privilege',
    'htmlize',
    'singledispatch',
    'dec_factory',
    'info'
]
def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(dc, inspect.isfunction)
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
    assert content.count("#") >= 25, 'You are not writing proper heading'

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


def test_access_levels():
    @dc.access_level(4)
    def no():
        return "lowest level"
    assert no() == "lowest level","clearance nahi h bro usko"
    with pytest.raises(ValueError):
        @dc.access_level(3)
        def high(a,b):
            return "highest level"

    @dc.access_level(1)
    def high():
        return "Highest level"
    assert high() == "Highest level","clearance nahi h bro usko"

def test_htmlize_dispatch():
    html_func = dc.htmlize
    assert 'htmlize' in str(html_func.dispatch(object)), "htmlize dispatch failed...."
    assert 'html_int' in str(html_func.dispatch(int)), "htmlize dispatch failed...."
    assert 'html_real' in str(html_func.dispatch(Decimal)), "htmlize dispatch failed...."
    assert 'html_real' in str(html_func.dispatch(float)), "htmlize dispatch failed...."
    assert 'html_str' in str(html_func.dispatch(str)), "htmlize dispatch failed...."
    assert 'html_sequence' in str(html_func.dispatch(list)), "htmlize dispatch failed...."
    assert 'html_sequence' in str(html_func.dispatch(tuple)), "htmlize dispatch failed...."
    assert 'html_sequence' in str(html_func.dispatch(set)), "htmlize dispatch failed...."
    assert 'html_sequence' in str(html_func.dispatch(frozenset)), "htmlize dispatch failed...."
    assert 'html_dict' in str(html_func.dispatch(dict)), "htmlize dispatch failed...."

def test_singledispatch_html():
    assert dc.htmlize(100) == '100(<i>0x64</i>)'
    assert dc.htmlize([1, 2]) == '<ul>\n<li>1</li>\n<li>2</li>\n</ul>'
    assert dc.htmlize(((1, 2), (2, 3))) == '<ul>\n<li>(1, 2)</li>\n<li>(2, 3)</li>\n</ul>'
    assert dc.htmlize({'a': 1, 'b': 2}) == '<ul>\n<li>a=1</li>\n<li>b=2</li>\n</ul>'
    assert dc.htmlize('1 < 200') == '1 &lt; 200'
    assert dc.htmlize('hello, world\n') == 'hello, world<br/>\n'
    assert dc.htmlize(1.1232112) == '1.12'
    assert dc.htmlize(Decimal(2.3445)) == '2.34'
    assert dc.htmlize({1,2}) == '<ul>\n<li>1</li>\n<li>2</li>\n</ul>'
    assert dc.htmlize(frozenset((1,2))) == '<ul>\n<li>1</li>\n<li>2</li>\n</ul>'

def test_docs():
    assert bool(dc.dec_factory_1.__doc__),"doc string missing"
    assert bool(dc.info.__doc__),"doc string missing"
    assert bool(dc.debug_info.__doc__),"doc string missing"
    assert bool(dc.authenticate.__doc__),"doc string missing"
    assert bool(dc.dec_factory_2.__doc__),"doc string missing"
    assert bool(dc.access_level.__doc__),"doc string missing"

def test_annot():
    assert bool(dc.dec_factory_1.__annotations__),"annotation missing"
    assert bool(dc.info.__annotations__),"annotation missing"
    assert bool(dc.debug_info.__annotations__),"annotation missing"
    assert bool(dc.authenticate.__annotations__),"annotation missing"
    assert bool(dc.dec_factory_2.__annotations__),"annotation missing"
    assert bool(dc.access_level.__annotations__),"annotation missing"