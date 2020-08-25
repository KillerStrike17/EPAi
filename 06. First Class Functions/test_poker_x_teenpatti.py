import pytest
import random
import poker_x_teenpatti as pxt
import os
import inspect
import re
value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
README_CONTENT_CHECK_FOR = [
    'hand',
    'process',
    'straight flush',
    'flush',
    'straight',
    'royal flush',
    'full house',
    '4 of a kind',
    '3 of a kind',
    'high card',
    '1 pair',
    '2 pair',
    'list comprehension',
    'generate_deck'
]

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(pxt, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 1200, "Make your README.md file interesting! Add atleast 500 words"

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

def test_generate_deck_using_list_comprehension():
    assert pxt.generate_deck_using_list_comprehension(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'],'deck is not generated properly'

def test_generate_deck():
    assert pxt.generate_deck(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'], 'Deck is not generated properly'

def test_check_for_number_sequence_for_no_sequence():
    my_list = [1,3,2,4,8]
    assert pxt.check_for_number_sequence(my_list) == False, 'This shouldnt be a sequence'

def test_check_for_number_sequence_for_sequence():
    my_list = [1,3,2,4,6,5]
    assert pxt.check_for_number_sequence(my_list) == True, 'This shouldnt be a sequence'

def test_check_for_color_for_same_color():
    my_list = ['diamonds','diamonds','diamonds','diamonds']
    assert pxt.check_for_color(my_list) == True,'The output should say they are all same'

def test_check_for_color_for_different_color():
    my_list = ['diamonds','diamonds','diamonds','hearts']
    assert pxt.check_for_color(my_list) == False,'It is okay to be different, but you are not cathcing that..'

def test_transform_value_list_for_single_occurance_jack():
    my_list = ['1','2','jack']
    assert pxt.transform_value_list(my_list) == [1,2,11],'jack Conversion not working'

def test_transform_value_list_for_single_occurance_queen():
    my_list = ['1','2','queen']
    assert pxt.transform_value_list(my_list) == [1,2,12],'Queen Conversion not working'

def test_transform_value_list_for_single_occurance_king():
    my_list = ['1','2','king']
    assert pxt.transform_value_list(my_list) == [1,2,13],'King Conversion not working'

def test_transform_value_list_for_single_occurance_ace():
    my_list = ['1','2','ace']
    assert pxt.transform_value_list(my_list) == [1,2,14],'Ace Conversion not working'

def test_transform_value_list_for_multiple_occurance_jack_and_queen():
    my_list = ['1','queen','jack']
    assert pxt.transform_value_list(my_list) == [1,12,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_king():
    my_list = ['1','king','jack']
    assert pxt.transform_value_list(my_list) == [1,13,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_jack():
    my_list = ['1','jack','jack']
    assert pxt.transform_value_list(my_list) == [1,11,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_ace():
    my_list = ['1','ace','jack']
    assert pxt.transform_value_list(my_list) == [1,14,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_queen_and_queen():
    my_list = ['1','queen','queen']
    assert pxt.transform_value_list(my_list) == [1,12,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_queen():
    my_list = ['1','king','queen']
    assert pxt.transform_value_list(my_list) == [1,13,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_ace_and_queen():
    my_list = ['1','ace','queen']
    assert pxt.transform_value_list(my_list) == [1,14,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_king():
    my_list = ['1','king','king']
    assert pxt.transform_value_list(my_list) == [1,13,13],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_ace():
    my_list = ['1','ace','king']
    assert pxt.transform_value_list(my_list) == [1,14,13],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_ace_and_ace():
    my_list = ['1','ace','ace']
    assert pxt.transform_value_list(my_list) == [1,14,14],'Multiple Combinations replace not working'

def test_show_for_5_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_4_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_3_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['ace spades', 'king spades', 'queen spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_5_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_4_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_3_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_5_for_1_v_3():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 4 of a kind, royal flush should win"

def test_show_for_4_for_1_v_3():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 4 of a kind, royal flush should win"

def test_show_for_5_for_1_v_4():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs Full House, royal flush should win"

def test_show_for_5_for_1_v_5():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs Flush, royal flush should win"

def test_show_for_4_for_1_v_5():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs Flush, royal flush should win"

def test_show_for_3_for_1_v_5():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['9 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs Flush, royal flush should win"

def test_show_for_5_for_1_v_6():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight, royal flush should win"

def test_show_for_4_for_1_v_6():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight, royal flush should win"

def test_show_for_3_for_1_v_6():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['king diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight, royal flush should win"

def test_show_for_5_for_1_v_7():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 3 of a kind, royal flush should win"

def test_show_for_4_for_1_v_7():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 3 of a kind, royal flush should win"

def test_show_for_3_for_1_v_7():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 3 of a kind, royal flush should win"

def test_show_for_5_for_1_v_8():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 2 pair , royal flush should win"

def test_show_for_4_for_1_v_8():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 2 pair , royal flush should win"

def test_show_for_5_for_1_v_9():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 1 pair , royal flush should win"

def test_show_for_4_for_1_v_9():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 1 pair , royal flush should win"

def test_show_for_3_for_1_v_9():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs 1 pair , royal flush should win"

def test_show_for_5_for_1_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs high card, royal flush should win"

def test_show_for_4_for_1_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['9 spades', 'king diamonds', 'queen spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs high card, royal flush should win"

def test_show_for_3_for_1_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['9 spades', 'king diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs high card, royal flush should win"

def test_show_for_5_for_2_v_1():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush , straight flush should win"

def test_show_for_4_for_2_v_1():
    set1 = ['10 spades', '9 spades', 'queen spades','jack spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush, straight flush should win"

def test_show_for_3_for_2_v_1():
    set1 = ['jack spades', '10 spades', 'queen spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush, straight flush should win"

def test_show_for_5_for_2_v_2():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['9 hearts', '8 hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '0',"straight Flush vs straight Flush should be a draw"

def test_show_for_4_for_2_v_2():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['9 hearts', 'queen hearts','10 hearts','jack hearts']

    assert pxt.show(set1,set2) == '0',"straight Flush vs straight Flush should be a draw"

def test_show_for_3_for_2_v_2():
    set1 = [ 'queen spades','jack spades','10 spades']
    set2 = ['queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '0',"straight Flush vs straight Flush should be a draw"

def test_show_for_5_for_2_v_3():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"straight Flush vs 4 of a kind, straight flush should win"

def test_show_for_4_for_2_v_3():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 4 of a kind, straight flush should win"

def test_show_for_5_for_2_v_4():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['ace diamonds', 'ace hearts', 'ace clubs','king clubs','king diamonds']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs Full House, straight flush should win"

def test_show_for_5_for_2_v_5():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['5 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs Flush, straight flush should win"

def test_show_for_4_for_2_v_5():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['7 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs Flush, straight flush should win"

def test_show_for_3_for_2_v_5():
    set1 = ['queen spades','jack spades','10 spades']
    set2 = ['5 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs Flush, straight flush should win"

def test_show_for_5_for_2_v_6():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['9 clubs', 'king diamonds', 'queen clubs','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs straight, straight flush should win"

def test_show_for_4_for_2_v_6():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king diamonds', 'queen clubs','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs straight, straight flush should win"

def test_show_for_3_for_2_v_6():
    set1 = ['10 spades', 'queen spades','jack spades']
    set2 = ['king diamonds', 'queen clubs','jack clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs straight, straight flush should win"

def test_show_for_5_for_2_v_7():
    set1 = ['9 hearts', '8 clubs', 'queen spades','jack diamonds','10 hearts']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs','jack hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 3 of a kind, straight flush should win"

def test_show_for_4_for_2_v_7():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 3 of a kind, straight flush should win"

def test_show_for_3_for_2_v_7():
    set1 = ['queen spades','jack spades','10 spades']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 3 of a kind, straight flush should win"

def test_show_for_5_for_2_v_8():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king hearts', 'king clubs', 'queen spades','queen hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 2 pair , straight flush should win"

def test_show_for_4_for_2_v_8():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king hearts', 'king spades', 'queen clubs','queen hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 2 pair , straight flush should win"

def test_show_for_5_for_2_v_9():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king clubs', 'king diamonds', 'jack diamonds','queen hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 1 pair , straight flush should win"

def test_show_for_4_for_2_v_9():
    set1 = ['9 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king clubs', 'king diamonds', 'jack diamonds','queen hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 1 pair , straight flush should win"

def test_show_for_3_for_2_v_9():
    set1 = ['queen spades','jack spades','10 spades']
    set2 = ['king clubs', 'king diamonds', 'jack diamonds']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs 1 pair , straight flush should win"

def test_show_for_5_for_2_v_10():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['9 diamonds', 'king diamonds', '5 diamonds','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs high card, straight flush should win"

def test_show_for_4_for_2_v_10():
    set1 = ['9 spades','queen spades','jack spades','10 spades']
    set2 = ['9 diamonds', 'king diamonds', 'queen diamonds','jack clubs']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs high card, straight flush should win"

def test_show_for_3_for_2_v_10():
    set1 = ['queen spades','jack spades','10 spades']
    set2 = ['9 spades', 'king diamonds', 'queen diamonds']
    assert pxt.show(set1,set2) == '1',"Straight Flush vs high card, straight flush should win"

def test_show_for_5_for_3_v_1():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs Royal Flush , 4 of a kind should win"

def test_show_for_4_for_3_v_1():
    set1 = ['10 spades', '9 spades', 'queen spades','jack spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs Royal Flush, 4 of a kind should win"

def test_show_for_5_for_3_v_2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['9 hearts', '8 hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs straight Flush,straight flush should win"

def test_show_for_4_for_3_v_2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['9 hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs straight Flush,straight flush should win"

def test_show_for_5_for_3_v_3_s1gts2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['6 hearts', '6 diamonds', '6 spades','6 hearts','10 diamonds']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 4 of a kind, player 1 should win"

def test_show_for_4_for_3_v_3_s1gts2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['6 hearts', '6 diamonds', '6 spades','6 hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 4 of a kind, player 1 should win"

def test_show_for_5_for_3_v_3_s1lts2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['8 hearts', '8 diamonds', '8 spades','8 hearts','10 diamonds']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs 4 of a kind, player 2 should win"

def test_show_for_4_for_3_v_3_s1lts2():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['8 hearts', '8 diamonds', '8 spades','8 hearts']
    assert pxt.show(set1,set2) == '2',"4 of a kind vs 4 of a kind, player 2 should win"

def test_show_for_5_for_3_v_4():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['ace diamonds', 'ace hearts', 'ace clubs','king clubs','king diamonds']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs Full House, 4 of a kind should win"

def test_show_for_5_for_3_v_5():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['5 spades', '2 spades', '3 spades','4 spades','8 spades']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs Flush, 4 of a kind should win"

def test_show_for_4_for_3_v_5():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['8 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs Flush, 4 of a kind should win"

def test_show_for_5_for_3_v_6():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['9 clubs', 'king diamonds', 'queen clubs','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs straight, 4 of a kind should win"

def test_show_for_4_for_3_v_6():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['king diamonds', 'queen clubs','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs straight, 4 of a kind should win"

def test_show_for_5_for_3_v_7():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs','jack hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 3 of a kind, 4 of a kind should win"

def test_show_for_4_for_3_v_7():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 3 of a kind, 4 of a kind should win"

def test_show_for_5_for_3_v_8():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['king hearts', 'king clubs', 'queen spades','queen hearts','10 diamonds']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 2 pair , 4 of a kind should win"

def test_show_for_4_for_3_v_8():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['king hearts', 'king spades', 'queen clubs','queen hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 2 pair , 4 of a kind should win"

def test_show_for_5_for_3_v_9():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['king clubs', 'king diamonds', 'jack diamonds','queen hearts','10 diamonds']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 1 pair , 4 of a kind should win"

def test_show_for_4_for_3_v_9():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['king clubs', 'king diamonds', 'jack diamonds','queen hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs 1 pair , 4 of a kind should win"

def test_show_for_5_for_3_v_10():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 clubs']
    set2 = ['9 diamonds', 'king diamonds', '5 diamonds','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs high card, 4 of a kind should win"

def test_show_for_4_for_3_v_10():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['9 diamonds', 'king diamonds', 'queen diamonds','jack clubs']
    assert pxt.show(set1,set2) == '1',"4 of a kind vs high card, 4 of a kind should win"

def test_show_for_5_for_4_v_1():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Full House vs Royal Flush, Roual Flush should be a draw"

def test_show_for_5_for_4_v_2():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Full House vs straight Flush, Straight flush should win"

def test_show_for_5_for_4_v_3():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"Full House vs 4 of a kind, 4 of a kind flush should win"

def test_show_for_5_for_4_v_4_s1lts2():
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set1 = ['queen diamonds', 'queen clubs', '8 clubs','8 spades','8 diamonds']
    assert pxt.show(set1,set2) == '2',"Full House vs Full House,player 2 should win"

def test_show_for_5_for_4_v_4_s1gts2():
    set1 = ['ace spades', 'ace hearts', 'king clubs','king spades','king diamonds']
    set2 = ['ace clubs', 'ace diamonds', 'queen clubs','queen spades','queen diamonds']
    assert pxt.show(set1,set2) == '1',"Full House vs Full House, player 1 should win"

def test_show_for_5_for_4_v_5():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '1',"Full House vs Flush, full house should win"

def test_show_for_5_for_4_v_6():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Full House vs straight, full house should win"

def test_show_for_5_for_4_v_7():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Full House vs 3 of a kind, full house should win"

def test_show_for_5_for_4_v_8():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['king hearts', 'king clubs', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Full House vs 2 pair , full house should win"

def test_show_for_5_for_4_v_9():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['king clubs', 'king clubs', 'jack spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Full House vs 1 pair , full house should win"

def test_show_for_5_for_4_v_10():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Full House vs high card, full house should win"

def test_show_for_5_for_5_v_1():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Flush vs Royal Flush, Royal Flush SHould win"

def test_show_for_4_for_5_v_1():
    set1 = ['9 spades', '2 spades','4 spades','7 spades']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"Flush vs Royal Flush, Royal Flush SHould win"

def test_show_for_3_for_5_v_1():
    set1 = ['9 spades', '4 spades','7 spades']
    set2 = ['ace spades', 'king spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"Flush vs Royal Flush, Royal Flush SHould win"

def test_show_for_5_for_5_v_2():
    set1 =['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Flush vs straight Flush, Straight flush should win"

def test_show_for_4_for_5_v_2():
    set1 = ['9 spades', '2 spades', '4 spades','7 spades']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"Flush vs straight Flush, Straight flush should win"

def test_show_for_3_for_5_v_2():
    set1 =['9 spades', '4 spades','7 spades']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"Flush vs straight Flush, Straight flush should win"

def test_show_for_5_for_5_v_3():
    set1 = ['9 spades', '2 spades', '4 spades','7 spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"Flush vs 4 of a kind, 4 of a kind should win"

def test_show_for_4_for_5_v_3():
    set1 =['9 spades', '4 spades','7 spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '2',"Flush vs 4 of a kind,  4 of a kind should win"

def test_show_for_5_for_5_v_4():
    set1 = ['9 spades', '2 spades','4 spades','7 spades']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.show(set1,set2) == '2',"Flush vs Full House, Full House should win"

def test_show_for_5_for_5_v_5_s1gts2():
    set1 = ['10 spades', '2 spades', '3 spades','5 spades','7 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts','4 hearts','7 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs Flush, player 1should win"

def test_show_for_5_for_5_v_5_s2gts1():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['10 hearts', '2 hearts', '3 hearts','5 hearts','7 hearts']
    assert pxt.show(set1,set2) == '2',"Flush vs Flush, player 2 should win"

def test_show_for_5_for_5_v_5_s1eqs2():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts','4 hearts','7 hearts']
    assert pxt.show(set1,set2) == '0',"Flush vs Flush, It should be a draw"

def test_show_for_4_for_5_v_5_s1gts2():
    set1 = ['10 spades', '2 spades', '4 spades','7 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts','4 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs Flush, player 1 should win"

def test_show_for_4_for_5_v_5_s1lts2():
    set1 = ['9 spades', '2 spades', '4 spades','7 spades']
    set2 = ['10 hearts', '2 hearts', '8 hearts','4 hearts']
    assert pxt.show(set1,set2) == '2',"Flush vs Flush, player 2 should win"

def test_show_for_4_for_5_v_5_s1eqs2():
    set1 = ['9 spades', '2 spades', '4 spades','7 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts','4 hearts']
    assert pxt.show(set1,set2) == '0',"Flush vs Flush, It should be a draw"

def test_show_for_3_for_5_v_5_s1gts2():
    set1 = ['9 spades', '2 spades', '3 spades']
    set2 = ['8 hearts', '2 hearts', '3 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs Flush, Player 1 should win"

def test_show_for_3_for_5_v_5_s1lts2():
    set1 = ['8 spades', '2 spades', '3 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts']
    assert pxt.show(set1,set2) == '2',"Flush vs Flush, Player 2 should win"

def test_show_for_3_for_5_v_5_s1eqs2():
    set1 = ['9 spades', '2 spades', '3 spades']
    set2 = ['9 hearts', '2 hearts', '3 hearts']
    assert pxt.show(set1,set2) == '0',"Flush vs Flush, It should be a draw"

def test_show_for_5_for_5_v_6():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs straight,flush should win"

def test_show_for_4_for_5_v_6():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs straight,flush should win"

def test_show_for_3_for_5_v_6():
    set1 = ['9 spades', '2 spades', '3 spades']
    set2 = ['king diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '1',"Flush vs straight,flush should win"

def test_show_for_5_for_5_v_7():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Flush vs 3 of a kind,flush should win"

def test_show_for_4_for_5_v_7():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"Flush vs 3 of a kind,flush should win"

def test_show_for_3_for_5_v_7():
    set1 = ['9 spades', '2 spades', '3 spades']
    set2 = ['queen hearts', 'queen spades', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"Flush vs 3 of a kind,flush should win"

def test_show_for_5_for_5_v_8():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Flush vs 2 pair ,flush should win"

def test_show_for_4_for_5_v_8():
    set1 =['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs 2 pair ,flush should win"

def test_show_for_5_for_5_v_9():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Flush vs 1 pair ,flush should win"

def test_show_for_4_for_5_v_9():
    set1 =['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs 1 pair ,flush should win"

def test_show_for_3_for_5_v_9():
    set1 =['9 spades', '2 spades', '3 spades']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '1',"Flush vs 1 pair ,flush should win"

def test_show_for_5_for_5_v_10():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"Flush vs high card,flush should win"

def test_show_for_4_for_5_v_10():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['9 spades', 'king diamonds', 'queen spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"Flush vs high card,flush should win"

def test_show_for_3_for_5_v_10():
    set1 = ['9 spades', '2 spades', '3 spades']
    set2 = ['9 spades', 'king diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '1',"Flush vs high card,flush should win"

def test_show_for_5_for_6_v_1():
    set1 =['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Royal Flush, Royal Flush wins"

def test_show_for_4_for_6_v_1():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Royal Flush, Royal Flush wins"

def test_show_for_3_for_6_v_1():
    set1 = [ 'queen spades','jack spades','10 hearts']
    set2 = ['ace spades', 'king spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Royal Flush, Royal Flush wins"

def test_show_for_5_for_6_v_2():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs straight Flush, Straight flush should win"

def test_show_for_4_for_6_v_2():
    set1 = ['9 clubs',  'queen spades','jack spades','10 hearts']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"Straight vs straight Flush, Straight flush should win"

def test_show_for_3_for_6_v_2():
    set1 = ['queen spades','jack spades','10 hearts']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"Straight vs straight Flush, Straight flush should win"

def test_show_for_5_for_6_v_3():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs 4 of a kind, 4 of a kind should win"

def test_show_for_4_for_6_v_3():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '2',"Straight vs 4 of a kind, 4 of a kind should win"

def test_show_for_5_for_6_v_4():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.show(set1,set2) == '2',"Straight vs Full House, Full House should win"

def test_show_for_5_for_6_v_5():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Flush, flush should win"

def test_show_for_4_for_6_v_5():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Flush, flush should win"

def test_show_for_3_for_6_v_5():
    set1 = ['queen spades','jack spades','10 hearts']
    set2 = ['9 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs Flush, flush should win"

def test_show_for_5_for_6_v_6_s1gts2():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 clubs', '8 diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '1',"Straight vs straight, player 1 should win"

def test_show_for_5_for_6_v_6_s1lts2():
    set1 = ['9 clubs', '8 diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '2',"Straight vs straight, player 2 should win"

def test_show_for_5_for_6_v_6_s1eqs2():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 hearts', 'king clubs', 'queen diamonds','jack hearts','10 spades']
    assert pxt.show(set1,set2) == '0',"Straight vs straight, It should be a draw"

def test_show_for_4_for_6_v_6_s1gts2():
    set1 = ['king clubs','queen spades','jack hearts','10 hearts']
    set2 = ['9 diamonds', 'queen hearts','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs straight, player 1 should win"

def test_show_for_4_for_6_v_6_s1lts2():
    set2 = ['king clubs','queen spades','jack hearts','10 hearts']
    set1 = ['9 diamonds', 'queen hearts','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"Straight vs straight, player 2 should win"

def test_show_for_4_for_6_v_6_s1eqs2():
    set1 = ['king clubs','queen spades','jack hearts','10 hearts']
    set2 = ['king diamonds', 'queen hearts','jack spades','10 spades']
    assert pxt.show(set1,set2) == '0',"Straight vs straight, It should be draw"

def test_show_for_3_for_6_v_6_s1gts2():
    set1 = [ 'queen clubs','jack diamonds','king hearts']
    set2 = ['10 diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '1',"Straight vs straight, player 1 should win"

def test_show_for_3_for_6_v_6_s1lts2():
    set2 = [ 'queen clubs','jack diamonds','king hearts']
    set1 = ['10 diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"Straight vs straight, player 2 should win"

def test_show_for_3_for_6_v_6_s1eqs2():
    set1 = ['king diamonds', 'queen spades','jack spades']
    set2 = ['king hearts', 'queen diamonds','jack clubs']
    assert pxt.show(set1,set2) == '0',"Straight vs straight, It should be a draw"

def test_show_for_5_for_6_v_7():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs 3 of a kind, straight should win"

def test_show_for_4_for_6_v_7():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs 3 of a kind, straight should win"

def test_show_for_3_for_6_v_7():
    set1 = [ 'queen spades','jack spades','10 hearts']
    set2 = ['queen hearts', 'queen diamonds', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"Straight vs 3 of a kind, straight should win"

def test_show_for_5_for_6_v_8():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['king hearts', 'king spades', 'queen diamonds','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs 2 pair , straight should win"

def test_show_for_4_for_6_v_8():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['king hearts', 'king spades', 'queen diamonds','queen hearts']
    assert pxt.show(set1,set2) == '1',"Straight vs 2 pair , straight should win"

def test_show_for_5_for_6_v_9():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs 1 pair , straight should win"

def test_show_for_4_for_6_v_9():
    set1 = ['9 clubs', 'queen spades','jack spades','10 hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"Straight vs 1 pair , straight should win"

def test_show_for_3_for_6_v_9():
    set1 = [ 'queen spades','jack spades','10 hearts']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '1',"Straight vs 1 pair , straight should win"

def test_show_for_5_for_6_v_10():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['9 spades', 'king clubs', 'queen clubs','5 clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"Straight vs high card, straight should win"

def test_show_for_4_for_6_v_10():
    set1 = ['9 clubs','queen spades','jack spades','10 hearts']
    set2 = ['9 spades', 'king clubs', 'queen clubs','jack clubs']
    assert pxt.show(set1,set2) == '1',"Straight vs high card, straight should win"

def test_show_for_3_for_6_v_10():
    set1 =[ 'queen spades','jack spades','10 hearts']
    set2 = ['9 spades', 'king clubs', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"Straight vs high card, straight should win"

def test_show_for_5_for_7_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['queen diamonds', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs Royal Flush,Royal Flush should be a draw"

def test_show_for_4_for_7_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['queen diamonds', 'queen spades', 'queen clubs','jack spades']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs Royal Flush,Royal Flush should be a draw"

def test_show_for_3_for_7_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['queen diamonds', 'queen spades', 'queen clubs']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs Royal Flush,Royal Flush should be a draw"

def test_show_for_5_for_7_v_2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight Flush, straight flush should win"

def test_show_for_4_for_7_v_2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight Flush, straight flush should win"

def test_show_for_3_for_7_v_2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight Flush, straight flush should win"

def test_show_for_5_for_7_v_3():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs 4 of a kind, 4 of a kind should win"

def test_show_for_4_for_7_v_3():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs 4 of a kind, 4 of a kind should win"

def test_show_for_5_for_7_v_4():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs Full House, Full House should win"

def test_show_for_5_for_7_v_5():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs Flush,  flush should win"

def test_show_for_4_for_7_v_5():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs Flush,  flush should win"

def test_show_for_3_for_7_v_5():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['9 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs Flush,  flush should win"

def test_show_for_5_for_7_v_6():
    set1 = ['queen hearts', 'queen diamonds', 'queen clubs','jack spades','10 spades']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight, straight should win"

def test_show_for_4_for_7_v_6():
    set1 = ['queen hearts', 'queen diamonds', 'queen clubs','jack spades']
    set2 = ['king diamonds', 'queen spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight, straight should win"

def test_show_for_3_for_7_v_6():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['king diamonds', 'queen diamonds','jack clubs']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs straight, straight should win"

def test_show_for_5_for_7_v_7_s1gts2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['8 hearts', '8 spades', '8 clubs','jack clubs','10 clubs']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 3 of a kind, player 1 should win"

def test_show_for_5_for_7_v_7_s1lts2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['king hearts', 'king spades', 'king clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs 3 of a kind, player 2 should win"

def test_show_for_4_for_7_v_7_s1gts2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['8 hearts', '8 spades', '8 clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 3 of a kind, player 1 should win"

def test_show_for_4_for_7_v_7_s1lts2():
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set1 = ['8 hearts', '8 spades', '8 clubs','10 spades']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs 3 of a kind, player 2 should win"

def test_show_for_3_for_7_v_7_s1gts2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['8 hearts', '8 spades', '8 clubs']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 3 of a kind,player 1 should win"

def test_show_for_3_for_7_v_7_s1lts2():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['king hearts', 'king spades', 'king clubs']
    assert pxt.show(set1,set2) == '2',"3 of a kind vs 3 of a kind, player 2 should win"

def test_show_for_5_for_7_v_8():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['king hearts', 'king spades', 'jack diamonds','jack hearts','10 clubs']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 2 pair , 3 of a kind should win"

def test_show_for_4_for_7_v_8():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['king hearts', 'king spades', 'jack diamonds','jack hearts']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 2 pair , 3 of a kind should win"

def test_show_for_5_for_7_v_9():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['king clubs', 'king spades', 'jack spades','queen diamonds','10 diamonds']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 1 pair , 3 of a kind should win"

def test_show_for_4_for_7_v_9():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['king clubs', 'king spades', 'jack spades','queen diamonds']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 1 pair , 3 of a kind should win"

def test_show_for_3_for_7_v_9():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs 1 pair , 3 of a kind should win"

def test_show_for_5_for_7_v_10():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs high card, 3 of a kind should win"

def test_show_for_4_for_7_v_10():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades']
    set2 = ['9 spades', 'king diamonds', 'queen spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs high card, 3 of a kind should win"

def test_show_for_3_for_7_v_10():
    set1 = ['queen hearts', 'queen spades', 'queen clubs']
    set2 = ['9 spades', 'king diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '1',"3 of a kind vs high card, 3 of a kind should win"

def test_show_for_5_for_8_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs Royal Flush, Royal Flush should be a draw"

def test_show_for_4_for_8_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs Royal Flush, Royal Flush should be a draw"

def test_show_for_5_for_8_v_2():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    set2 = ['king diamonds', 'king spades', 'queen diamonds','queen clubs','10 clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs straight Flush, straight flush should win"

def test_show_for_4_for_8_v_2():
    set1 = ['10 spades', '9 spades', 'queen spades','jack spades']
    set2 = ['king diamonds', 'king spades', 'queen diamonds','queen clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs straight Flush, straight flush should win"

def test_show_for_5_for_8_v_3():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs','10 clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 4 of a kind,  4 of a kindshould win"

def test_show_for_4_for_8_v_3():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 4 of a kind,  4 of a kind should win"

def test_show_for_5_for_8_v_4():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    set2 = ['king diamonds', 'king hearts', 'queen spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs Full House, Full House should win"

def test_show_for_5_for_8_v_5():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs Flush,  flush should win"

def test_show_for_4_for_8_v_5():
    set1 = ['9 spades', '2 spades', '3 spades','4 spades']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs Flush,  flush should win"

def test_show_for_5_for_8_v_6():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs straight, straight should win"

def test_show_for_4_for_8_v_6():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs straight, straight should win"

def test_show_for_5_for_8_v_7():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    set2 = ['king diamonds', 'king spades', '10 clubs','queen diamonds','10 hearts']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 3 of a kind, 3 of a kind should win"

def test_show_for_4_for_8_v_7():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king diamonds', 'king spades', '10 clubs','queen diamonds']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 3 of a kind, 3 of a kind should win"

def test_show_for_5_for_8_v_8_s1gts2():
    set2 = ['jack diamonds', 'jack spades', 'queen diamonds','queen clubs','10 hearts']
    set1 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 2 pair , player 1 should win"

def test_show_for_5_for_8_v_8_s1lts2():
    set1 = ['jack diamonds', 'jack spades', 'queen diamonds','queen clubs','10 hearts']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"2 Pair vs 2 pair , player 2 should win"

def test_show_for_5_for_8_v_8_s1eqs2():
    set1 = ['king diamonds', 'king clubs', 'queen diamonds','queen clubs','10 hearts']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts','9 spades']
    assert pxt.show(set1,set2) == '0',"2 Pair vs 2 pair , it should be draw"

def test_show_for_4_for_8_v_8_s1gts2():
    set2 = ['jack diamonds', 'jack spades', 'queen diamonds','queen clubs']
    set1 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 2 pair , player 1 should win"

def test_show_for_4_for_8_v_8_s1lts2():
    set1 = ['jack diamonds', 'jack spades', 'queen diamonds','queen clubs']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '2',"2 Pair vs 2 pair , player 2 should win"

def test_show_for_4_for_8_v_8_s1eqs2():
    set1 = ['king diamonds', 'king clubs', 'queen diamonds','queen clubs']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '0',"2 Pair vs 2 pair , it should be draw"

def test_show_for_5_for_8_v_9():
    set1 = ['king diamonds', 'king spades', 'queen spades','queen clubs','10 clubs']
    set2 = ['king clubs', 'king hearts', 'jack spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 1 pair , 2 Pair should win"

def test_show_for_4_for_8_v_9():
    set1 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    set2 = ['king clubs', 'king hearts', 'jack spades','queen hearts']
    assert pxt.show(set1,set2) == '1',"2 Pair vs 1 pair , 2 Pair should win"

def test_show_for_5_for_8_v_10():
    set1 =['king diamonds', 'king spades', 'queen spades','queen clubs','10 spades']
    set2 = ['9 spades', 'king hearts', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"2 Pair vs high card, 2 Pair should win"

def test_show_for_4_for_8_v_10():
    set1 = ['king diamonds', 'king spades', 'queen spades','queen clubs']
    set2 = ['9 spades', 'king hearts', 'queen spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"2 Pair vs high card, 2 Pair should win"

def test_show_for_5_for_9_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '1',"1 Pair vs Royal Flush, Royal Flush should win"

def test_show_for_4_for_9_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen clubs']
    assert pxt.show(set1,set2) == '1',"1 Pair vs Royal Flush, Royal Flush should win"

def test_show_for_3_for_9_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '1',"1 Pair vs Royal Flush, Royal Flush should win"

def test_show_for_5_for_9_v_2():
    set1 = ['king clubs', 'king spades', 'jack clubs','queen hearts','10 clubs']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight Flush, straight flush should win"

def test_show_for_4_for_9_v_2():
    set1 = ['king clubs', 'king spades', 'jack clubs','queen hearts']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight Flush, straight flush should win"

def test_show_for_3_for_9_v_2():
    set1 = ['king clubs', 'king spades', 'jack clubs']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight Flush, straight flush should win"

def test_show_for_5_for_9_v_3():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 clubs']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 4 of a kind, 4 of a kind should win"

def test_show_for_4_for_9_v_3():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 4 of a kind, 4 of a kind should win"

def test_show_for_5_for_9_v_4():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king hearts','king diamonds']
    assert pxt.show(set1,set2) == '2',"1 Pair vs Full House, Full House should win"

def test_show_for_5_for_9_v_5():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs Flush, flush should win"

def test_show_for_4_for_9_v_5():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs Flush, flush should win"

def test_show_for_3_for_9_v_5():
    set1 = ['king clubs', 'king spades', 'jack spades']
    set2 = ['9 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs Flush, flush should win"

def test_show_for_5_for_9_v_6():
    set1 = ['king clubs', 'king spades', 'jack clubs','queen hearts','10 spades']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight, straight should win"

def test_show_for_4_for_9_v_6():
    set1 = ['king clubs', 'king spades', 'jack clubs','queen hearts']
    set2 = ['king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight, straight should win"

def test_show_for_3_for_9_v_6():
    set1 = ['king clubs', 'king spades', 'jack clubs']
    set2 = ['king diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs straight, straight should win"

def test_show_for_5_for_9_v_7():
    set1 = ['king clubs', 'king spades', 'jack diamonds','queen hearts','10 diamonds']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 3 of a kind, 3 of a kind should win"

def test_show_for_4_for_9_v_7():
    set1 = ['king clubs', 'king spades', 'jack diamonds','queen hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 3 of a kind, 3 of a kind should win"

def test_show_for_3_for_9_v_7():
    set1 = ['king clubs', 'king spades', 'jack diamonds']
    set2 = ['queen hearts', 'queen spades', 'queen clubs']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 3 of a kind, 3 of a kind should win"

def test_show_for_5_for_9_v_8():
    set1 = ['king clubs', 'king spades', 'jack spades','queen clubs','10 spades']
    set2 = ['king hearts', 'king diamonds', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 2 pair ,  2 pair should win"

def test_show_for_4_for_9_v_8():
    set1 = ['king clubs', 'king spades', 'jack spades','queen clubs']
    set2 = ['king hearts', 'king diamonds', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 2 pair ,  2 pair should win"

def test_show_for_5_for_9_v_9_s1gts2():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    set2 = ['queen clubs', 'queen spades', '10 spades','9 hearts','8 spades']
    assert pxt.show(set1,set2) == '1',"1 Pair vs 1 pair ,player 1 should win"

def test_show_for_5_for_9_v_9_s1lts2():
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    set1 = ['queen clubs', 'queen spades', '10 spades','9 hearts','8 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 1 pair , player 2 should win"

def test_show_for_5_for_9_v_9_s1eqs2():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts','10 spades']
    set2 = ['king hearts', 'king diamonds', 'jack spades','queen diamonds','10 clubs']
    assert pxt.show(set1,set2) == '0',"1 Pair vs 1 pair , It should be a draw"

def test_show_for_4_for_9_v_9_s1gts2():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    set2 = ['queen clubs', 'queen spades', '10 spades','9 hearts']
    assert pxt.show(set1,set2) == '1',"1 Pair vs 1 pair ,player 1 should win"

def test_show_for_4_for_9_v_9_s1lts2():
    set2 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    set1 = ['queen clubs', 'queen spades', '10 spades','9 hearts']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 1 pair , player 2 should win"

def test_show_for_4_for_9_v_9_s1eqs2():
    set1 = ['king clubs', 'king spades', 'jack spades','queen hearts']
    set2 = ['king hearts', 'king diamonds', 'jack spades','queen diamonds']
    assert pxt.show(set1,set2) == '0',"1 Pair vs 1 pair , It should be a draw"

def test_show_for_3_for_9_v_9_s1gts2():
    set1 = ['king clubs', 'king spades', 'jack spades']
    set2 = ['queen clubs', 'queen spades', '10 spades']
    assert pxt.show(set1,set2) == '1',"1 Pair vs 1 pair ,player 1 should win"

def test_show_for_3_for_9_v_9_s1lts2():
    set2 = ['king clubs', 'king spades', 'jack spades']
    set1 = ['queen clubs', 'queen spades', '10 spades']
    assert pxt.show(set1,set2) == '2',"1 Pair vs 1 pair , player 2 should win"

def test_show_for_3_for_9_v_9_s1eqs2():
    set1 = ['king clubs', 'king spades', 'jack spades']
    set2 = ['king hearts', 'king diamonds', '10 spades']
    assert pxt.show(set1,set2) == '0',"1 Pair vs 1 pair , It should be a draw"

def test_show_for_5_for_9_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    assert pxt.show(set1,set2) == '1',"1 Pair vs high card, royal flush should win"

def test_show_for_4_for_9_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['9 spades', 'king diamonds', 'queen spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"1 Pair vs high card, royal flush should win"

def test_show_for_3_for_9_v_10():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['9 spades', 'king diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '1',"1 Pair vs high card, royal flush should win"

def test_show_for_5_for_10_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 =['9 spades', 'king diamonds', '5 spades','jack clubs','10 clubs']
    assert pxt.show(set1,set2) == '1',"High Card vs Royal Flush, Royal Flush should  win"

def test_show_for_4_for_10_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['9 spades', 'king diamonds', '5 spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"High Card vs Royal Flush, Royal Flush should  win"

def test_show_for_3_for_10_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['9 spades', 'king diamonds', '5 spades']
    assert pxt.show(set1,set2) == '1',"High Card vs Royal Flush, Royal Flush should  win"

def test_show_for_5_for_10_v_2():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs straight Flush, straight flush should win"

def test_show_for_4_for_10_v_2():
    set1 =  ['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['10 spades', '9 spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"High Card vs straight Flush, straight flush should win"

def test_show_for_3_for_10_v_2():
    set1 =['9 spades', 'king diamonds', '5 spades']
    set2 = ['jack spades', '10 spades', 'queen spades']
    assert pxt.show(set1,set2) == '2',"High Card vs straight Flush, straight flush should win"

def test_show_for_5_for_10_v_3():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 4 of a kind,  4 of a kind should win"

def test_show_for_4_for_10_v_3():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts']
    assert pxt.show(set1,set2) == '2',"High Card vs 4 of a kind,  4 of a kindshould win"

def test_show_for_5_for_10_v_4():
    set1 = ['9 spades', 'king hearts', '5 spades','jack clubs','10 hearts']
    set2 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.show(set1,set2) == '2',"High Card vs Full House, Full House should win"

def test_show_for_5_for_10_v_5():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs Flush, flush should win"

def test_show_for_4_for_10_v_5():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['9 spades', '2 spades', '3 spades','4 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs Flush, flush should win"

def test_show_for_3_for_10_v_5():
    set1 =['9 spades', 'king diamonds', '5 spades']
    set2 = ['9 spades', '2 spades', '3 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs Flush, flush should win"

def test_show_for_5_for_10_v_6():
    set1 =['9 spades', 'king hearts', '5 spades','jack clubs','10 clubs']
    set2 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '2',"High Card vs straight, straight should win"

def test_show_for_4_for_10_v_6():
    set1 = ['9 spades', 'king hearts', '5 spades','jack clubs']
    set2 = ['king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.show(set1,set2) == '2',"High Card vs straight, straight should win"

def test_show_for_3_for_10_v_6():
    set1 = ['9 spades', 'king diamonds', '5 spades']
    set2 = ['king diamonds', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '2',"High Card vs straight, straight should win"

def test_show_for_5_for_10_v_7():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 3 of a kind, 3 of a kind should win"

def test_show_for_4_for_10_v_7():
    set1 =['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['queen hearts', 'queen spades', 'queen clubs','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 3 of a kind, 3 of a kind should win"

def test_show_for_3_for_10_v_7():
    set1 =['9 spades', 'king diamonds', '5 spades']
    set2 = ['queen hearts', 'queen spades', 'queen clubs']
    assert pxt.show(set1,set2) == '2',"High Card vs 3 of a kind, 3 of a kindh should win"

def test_show_for_5_for_10_v_8():
    set1 =['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 2 pair ,2 pair should win"

def test_show_for_4_for_10_v_8():
    set1 =['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['king hearts', 'king spades', 'queen spades','queen hearts']
    assert pxt.show(set1,set2) == '2',"High Card vs 2 pair , 2 pair should win"

def test_show_for_5_for_10_v_9():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs','10 hearts']
    set2 = ['king clubs', 'king spades', 'jack spades','queen clubs','10 spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 1 pair , 1 pair should win"

def test_show_for_4_for_10_v_9():
    set1 = ['9 spades', 'king diamonds', '5 spades','jack clubs']
    set2 = ['king clubs', 'king spades', 'jack spades','queen clubs']
    assert pxt.show(set1,set2) == '2',"High Card vs 1 pair , 1 pair should win"

def test_show_for_3_for_10_v_9():
    set1 =['9 spades', 'king diamonds', '5 spades']
    set2 = ['king clubs', 'king spades', 'jack spades']
    assert pxt.show(set1,set2) == '2',"High Card vs 1 pair , 1 pair should win"

def test_show_for_5_for_10_v_10_s1gts2():
    set1 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds','10 hearts']
    set2 = ['9 spades', 'queen diamonds', '5 spades','jack clubs','10 clubs']
    assert pxt.show(set1,set2) == '1',"High Card vs high card, player 1 should win"

def test_show_for_5_for_10_v_10_s1lts2():
    set2 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds','10 hearts']
    set1 = ['9 spades', 'queen diamonds', '5 spades','jack clubs','10 clubs']
    assert pxt.show(set1,set2) == '2',"High Card vs high card, player 2 should win"

def test_show_for_5_for_10_v_10_s1eqs2():
    set1 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds','10 hearts']
    set2 = ['9 spades', 'king hearts', '5 spades','jack clubs','10 clubs']
    assert pxt.show(set1,set2) == '0',"High Card vs high card, It should be a draw"

def test_show_for_4_for_10_v_10_s1gts2():
    set1 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds']
    set2 = ['9 spades', 'queen diamonds', '5 spades','jack clubs']
    assert pxt.show(set1,set2) == '1',"High Card vs high card, player 1 should win"

def test_show_for_4_for_10_v_10_s1lts2():
    set2 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds']
    set1 = ['9 spades', 'queen diamonds', '5 spades','jack clubs']
    assert pxt.show(set1,set2) == '2',"High Card vs high card, player 2 should win"

def test_show_for_4_for_10_v_10_s1eqs2():
    set1 = ['9 clubs', 'king diamonds', '5 hearts','jack diamonds']
    set2 = ['9 spades', 'king hearts', '5 spades','jack clubs']
    assert pxt.show(set1,set2) == '0',"High Card vs high card, It should be a draw"

def test_show_for_3_for_10_v_10_s1gts2():
    set1 = ['ace hearts', 'jack clubs', 'queen hearts']
    set2 = ['9 spades', 'jack diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '1',"High Card vs high card, player 1 should win"

def test_show_for_3_for_10_v_10_s1lts2():
    set2 = ['ace hearts', 'jack clubs', 'queen hearts']
    set1 = ['9 spades', 'jack diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '2',"High Card vs high card, player 2 should win"

def test_show_for_3_for_10_v_10_s1eqs2():
    set1 = ['ace hearts', 'jack clubs', 'queen hearts']
    set2 = ['9 spades', 'ace diamonds', 'queen spades']
    assert pxt.show(set1,set2) == '0',"High Card vs high card, It should be a draw"

def test_process_for_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.process(set1) == (1,14)

def test_process_for_2():
    set1 = ['9 spades', '8 spades', 'queen spades','jack spades','10 spades']
    assert pxt.process(set1) ==(2,12)

def test_process_for_3():
    set1 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
    assert pxt.process(set1) == (3,7)

def test_process_for_4():
    set1 = ['ace spades', 'ace hearts', 'ace clubs','king spades','king diamonds']
    assert pxt.process(set1) == (4,14)

def test_process_for_5():
    set1 =  ['9 spades', '2 spades', '3 spades','4 spades','7 spades']
    assert pxt.process(set1) == (5,9)

def test_process_for_6():
    set1 = ['9 clubs', 'king diamonds', 'queen spades','jack spades','10 hearts']
    assert pxt.process(set1) == (6,13)

def test_process_for_7():
    set1 = ['queen hearts', 'queen spades', 'queen clubs','jack spades','10 spades']
    assert pxt.process(set1) == (7,12)

def test_process_for_8():
    set1 = ['king hearts', 'king spades', 'queen spades','queen hearts','10 spades']
    assert pxt.process(set1) == (8,13)

def test_process_for_9():
    set1 = ['king clubs', 'king spades', 'jack spades','queen clubs','10 spades']
    assert pxt.process(set1) == (9,13)

def test_process_for_10():
    set1 = ['9 spades', 'queen diamonds', '5 spades','jack clubs','10 clubs']
    assert pxt.process(set1) == (10,12)

def test_generate_deck_doc():
    assert bool(pxt.generate_deck.__doc__),'No DocString for generate_dec'
def test_poker_x_teen_patti_docs():
    assert bool(pxt.poker_x_teen_patti.__doc__),'No DocString for poker_x_teen_patti'
def test_show_docs():
    assert bool(pxt.show.__doc__),'No DocString for show'

def test_process_docs():
    assert bool(pxt.process.__doc__),'No DocString for process'

def test_transform_value_list_docs():
    assert bool(pxt.transform_value_list.__doc__),'No DocString for transform_value_list'
def test_check_for_color_docs():
    assert bool(pxt.check_for_color.__doc__),'No DocString for check_for_color'
def test_check_for_number_sequence_docs():
    assert bool(pxt.check_for_number_sequence.__doc__),'No DocString for check_for_number_sequence'

def test_poker_x_teen_patti_annot():
    assert bool(pxt.poker_x_teen_patti.__annotations__),'No Annotation for poker_x_teen_patti'
def test_show_annot():
    assert bool(pxt.show.__annotations__),'No Annotation for show'

def test_process_annot():
    assert bool(pxt.process.__annotations__),'No Annotation for process'

def test_transform_value_list_annot():
    assert bool(pxt.transform_value_list.__annotations__),'No Annotation for transform_value_list'
def test_check_for_color_annot():
    assert bool(pxt.check_for_color.__annotations__),'No Annotation for check_for_color'
def test_check_for_number_sequence_annot():
    assert bool(pxt.check_for_number_sequence.__annotations__),'No Annotation for check_for_number_sequence'