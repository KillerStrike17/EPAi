import inspect
import re
import Session7 as pxt
import os
import pytest
import random
README_CONTENT_CHECK_FOR = [
    'Fibonacci',
    'vowels',
    'list',
    'lambda',
    'zip',
    'tuple',
    'detox',
    'reduce',
    'sigmoid',
    'Cipher',
    'number plate',
    'ReLU'
]

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(pxt, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

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
    assert content.count("#") >= 10, 'You are not writing proper heading'

def test_fibonacci():
    assert [0, 1, 1, 2, 3, 5, 8, 13] == pxt.fibonacci(8), 'You are not able to generate a fabonacci series, time to visit childhood again'
    assert [0, 1, 1, 2] == pxt.fibonacci(4), 'You are not able to generate a fabonacci series, time to visit childhood again'

def test_check_result():
    assert [0, 1, 1, 2, 3, 5, 8, 13] == pxt.check_result([0,5,6,9,4,7,8,2,1,3,6,1,13,50,600]), 'Fibonacci matching is getting failed'
    assert [0, 1, 1, 2] == pxt.check_result([0,6,9,4,7,2,1,6,1,50,600]), 'You are not able to generate a fabonacci series, time to visit childhood again'

def test_add():
    a = [1,3,5,7,9]
    b = [2,4,6,8,10]
    assert pxt.my_add(a,b) == [], 'you just had to check odd and even and perform addition, and you FAILED..!!'
    b = [1,3,5,7,9]
    a = [2,4,6,8,10]
    assert pxt.my_add(a,b) == [3,7,11,15,19], 'you just had to check odd and even and perform addition, and you FAILED..!!'

def test_string():
    mystring = "tsai"
    assert pxt.my_alphabet(mystring) == "ts" ,'You ust need to remove a,e,i, o, u, You are awesome, you can do it.'

def test_my_relu():
    mylist = [-1,-2,-3,-4,-5,5,4,3,1,0,9,-10,-17,5,2]
    assert pxt.my_relu(mylist) == [0,0,0,0,0,5,4,3,1,0,9,0,0,5,2],"Remove all the negativity"

def test_sigmoid():
    x = 0
    assert pxt.sigmoid(x) == 0.5, 'it is simple sigmoid, check google for equation'
    x = 4
    assert pxt.sigmoid(x) == 0.9820137900379085, 'it is simple sigmoid, check google for equation'
    x = -4
    assert pxt.sigmoid(x) == 0.01798620996209156, 'it is simple sigmoid, check google for equation'

def test_mysigmoid():
    mylist = [0,4,-4]
    assert pxt.mysigmoid(mylist) == [0.5,0.9820137900379085,0.01798620996209156], 'do the same thing that you did above, but it is a list this time'

def test_mycipher():
    mystring = "zyxwvutsai"
    assert pxt.mycipher(mystring) =="edcbazyxfn","Alphabetical ciphers are very simple,you messed it up but you can do it"

def test_detox():
    mypara = "ola Amigo"
    with pytest.raises(ValueError, match=r".* length .*"):
        pxt.detox(mypara), "That is not a paragraph"
    
    mypara = '''
            reverting for no reason i spent quite some time improving an article that 
            was in a poor state now two people have undone all my work with a click 
            of a button you did not have the courtesy to explain why you reverted it 
            but you still had the fucking cheek to accuse me of leaving an inaccurate 
            edit summary noone is that stupid so you were plainly just out to provoke me 
            well fucking well done consider me fucking provoked i guess you did not even bother 
            to look at the changes before you put all that shit back selfarrest refers to various maneuvers 
            employed in mountaineering it does not refer to that it is that you want to say paris refers to the capital 
            city of france or nile refers to a river that flows into the mediterranean sliding down a snow or ice covered slope 
            arrests stops the slide you think readers are too stupid to understand what arrests means in this 
            context himself or herself you think the single word themselves is some how better expressed in three words andor 
            ice axe you never bothered to read wpslash these potentially lifesaving techniques must be practiced 
            frequently in order to maintain proficiency this website is called wikipedia not wikimanual but you never bothered 
            to read wpnot did you that is just the first five i made many more i left the article looking considerably 
            better and more encyclopaedic but then you came along and fucked it all back up again do you feel 
            proud still waiting for you to justify your risible claim of or also stop stalking and harassing
            '''
    assert pxt.detox(mypara) == True,"One should not ignore bad words, they should teach people not to say it as it may hurt someone"

    mypara = '''
            reverting for no reason i spent quite some time improving an article that 
            was in a poor state now two people have undone all my work with a click 
            of a button you did not have the courtesy to explain why you reverted it 
            but you still had the cheek to accuse me of leaving an inaccurate 
            edit summary noone is that stupid so you were plainly just out to provoke me 
            well well done consider me provoked i guess you did not even bother 
            to look at the changes before you put all that back selfarrest refers to various maneuvers 
            employed in mountaineering it does not refer to that it is that you want to say paris refers to the capital 
            city of france or nile refers to a river that flows into the mediterranean sliding down a snow or ice covered slope 
            arrests stops the slide you think readers are too stupid to understand what arrests means in this 
            context himself or herself you think the single word themselves is some how better expressed in three words andor 
            ice axe you never bothered to read wpslash these potentially lifesaving techniques must be practiced 
            frequently in order to maintain proficiency this website is called wikipedia not wikimanual but you never bothered 
            to read wpnot did you that is just the first five i made many more i left the article looking considerably 
            better and more encyclopaedic but then you came along and it all back up again do you feel 
            proud still waiting for you to justify your risible claim of or also stop stalking and harassing
            '''
    assert pxt.detox(mypara) == False,"One should not classify something good as bad"

def test_myadd():
    mynumbers = [1,2,3,4,5,6,7,8,9,10]
    assert pxt.myadd(mynumbers) == 2+4+6+8+10,'just check if they are even then add them. Simple.'

def test_mymaxchar():
    mystring = "SHUBHAM AGNIHOTRI"
    assert pxt.mymaxchar(mystring) == 'U','Need to find the max character, it is not working as expected'
    mystring = "shubham agnihotri"
    assert pxt.mymaxchar(mystring) =='u','Need to find the max character, it is not working as expected'

def test_my_atrangi_addition():
    mynumbers = [1,2,3,4,5,6,7,8,9,10]
    assert pxt.my_atrangi_addition(mynumbers) == 3+6+9,'just select evert 3rd element and add it. Simple.'

def test_get_numberplate():
    mynumbers = [random.randint(1000,10000) for x in range(25)]
    mynumberplates = pxt.get_numberplate(mynumbers)
    for i in range(len(mynumberplates)):
        assert mynumberplates[i][-4:] == str(mynumbers[i]),'Custom Number plates not getting assigned'


def test_ny_number_plate():
    state_code="KA"
    numberplate = 1224
    assert pxt.my_number_plate(state_code,numberplate)[:2] == state_code,'Number plate is not getting generated properly'
    assert pxt.my_number_plate(state_code,numberplate)[-4:] == str(numberplate),'Number plate is not getting generated properly'

def test_custom_numberplate():
    state_code="KA"
    assert pxt.custom_numberplate(pxt.my_number_plate,state_code)()[:2] == state_code,'Number plate is not getting generated properly'

def test_fibonacci_doc():
    assert bool(pxt.fibonacci.__doc__),'No DocString for fibonacci'
def test_check_result_docs():
    assert bool(pxt.check_result.__doc__),'No DocString for check_result'
def test_my_add_docs():
    assert bool(pxt.my_add.__doc__),'No DocString for my_add'

def test_my_alphabet_docs():
    assert bool(pxt.my_alphabet.__doc__),'No DocString for my_alphabet'

def test_my_relu_docs():
    assert bool(pxt.my_relu.__doc__),'No DocString for my_relu'
def test_sigmoid_docs():
    assert bool(pxt.sigmoid.__doc__),'No DocString for sigmoid'
def test_mysigmoid_docs():
    assert bool(pxt.mysigmoid.__doc__),'No DocString for mysigmoid'
def test_mycipher_docs():
    assert bool(pxt.mycipher.__doc__),'No DocString for mycipher'
def test_detox_docs():
    assert bool(pxt.detox.__doc__),'No DocString for detox'
def test_myadd_docs():
    assert bool(pxt.myadd.__doc__),'No DocString for myadd'
def test_mymaxchar_docs():
    assert bool(pxt.mymaxchar.__doc__),'No DocString for mymaxchar'
def test_my_atrangi_addition_docs():
    assert bool(pxt.my_atrangi_addition.__doc__),'No DocString for my_atrangi_addition'
def test_mynumberplate_docs():
    assert bool(pxt.mynumberplate.__doc__),'No DocString for mynumberplate'
def test_get_numberplate_docs():
    assert bool(pxt.get_numberplate.__doc__),'No DocString for get_numberplate'
def test_my_number_plate_docs():
    assert bool(pxt.my_number_plate.__doc__),'No DocString for my_number_plate'

def test_custom_numberplate_docs():
    assert bool(pxt.custom_numberplate.__doc__),'No DocString for custom_numberplate'

def test_fibonacci_annot():
    assert bool(pxt.fibonacci.__annotations__),'No Annotation for fibonacci'
def test_check_result_annot():
    assert bool(pxt.check_result.__annotations__),'No Annotation for check_result'

def test_my_add_annot():
    assert bool(pxt.my_add.__annotations__),'No Annotation for my_add'

def test_my_alphabet_annot():
    assert bool(pxt.my_alphabet.__annotations__),'No Annotation for my_alphabet'
def test_my_relu_annot():
    assert bool(pxt.my_relu.__annotations__),'No Annotation for my_relu'
def test_sigmoid_annot():
    assert bool(pxt.sigmoid.__annotations__),'No Annotation for sigmoid'

def test_mysigmoid_annot():
    assert bool(pxt.mysigmoid.__annotations__),'No Annotation for mysigmoid'

def test_mycipher_annot():
    assert bool(pxt.mycipher.__annotations__),'No Annotation for mycipher'

def test_detox_annot():
    assert bool(pxt.detox.__annotations__),'No Annotation for detox'

def test_myadd_annot():
    assert bool(pxt.myadd.__annotations__),'No Annotation for myadd'

def test_mymaxchar_annot():
    assert bool(pxt.mymaxchar.__annotations__),'No Annotation for mymaxchar'

def test_my_atrangi_addition_annot():
    assert bool(pxt.my_atrangi_addition.__annotations__),'No Annotation for my_atrangi_addition'

def test_mynumberplate_annot():
    assert bool(pxt.mynumberplate.__annotations__),'No Annotation for mynumberplate'

def test_get_numberplate_annot():
    assert bool(pxt.get_numberplate.__annotations__),'No Annotation for get_numberplate'
def test_my_number_plate_annot():
    assert bool(pxt.my_number_plate.__annotations__),'No Annotation for my_number_plate'
def test_custom_numberplate_annot():
    assert bool(pxt.custom_numberplate.__annotations__),'No Annotation for custom_numberplate'
