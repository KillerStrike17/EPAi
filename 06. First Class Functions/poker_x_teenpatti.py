import random
from collections import Counter

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def generate_deck_using_list_comprehension(suits,value):
    # Using List Comprehension
    deck = [i+' ' + j for i in value for j in suits]
    return deck

test_deck = generate_deck_using_list_comprehension(suits, value)
print(test_deck)

#Using Normal Function
def generate_deck(suits, value, mydeck = None):
    '''
    This function takes suits and value list, combines them and returns the deck
    # Input :
        suits: list
        value: list
        mydeck: list(optional)
    # Functionality:
        Iterates over suits and value and combines each value.
    
    # Returns: 
        A list is returned containing the result of combination of value and suits.
    '''
    mydeck = mydeck or []
    for i in value:
        for j in suits:
            mydeck.append(i + " " + j)
    return mydeck

print(generate_deck(suits,value),end = "\n\n")


def poker_x_teen_patti(deck: list,cards_in_hand: int) -> str:
    '''
    creates hands, call s show function and returns results
    # Input: 
        deck: The list of cards of deck 
        cards_in_hand: total number of cards each player should have.
    # Returns:
        Returns result i.e. string value contain the player won
    '''
    set1 = []
    set2 = []
    print('Cards in hand:',cards_in_hand)
    random.shuffle(deck)
    for _ in range(0,cards_in_hand):
        set1.append(deck.pop())
        set2.append(deck.pop())
    print("Remaining Deck:",deck,"\n lenght: ",len(deck))
    print("Player 1 Hand:",set1)
    print("Player 2 Hand:",set2)
    result  = show(set1, set2)
    return result

def show(set1: list,set2: list) -> str:
    '''
    call process function which returns a tuple, this function analyzes that tuple 
    to figure out who won.
    # input: 
        set1 : List of cards player 1 is having
        set2 : List of cards player 2 is having
    # Returns:
        This function returns a string which indicated which plaeyr won i.e. 0 for a draw, 
        1 for player 1 won and 2 for player 2 won.
    '''

    a,b = process(set1)
    c,d = process(set2)
    print("Player 1 hand rating:",a,b)
    print("Player 2 hand rating:",c,d)
    if a<c:
        print("Winner is player 1")
        return '1'
    elif a>c:
        print("Winner is player 2")
        return '2'
    elif a == c:
        if b>d:
            print("Winner is player 1")
            return '1'
        elif b<d:
            print("Winner is player 2")
            return '2'
        elif b==d:
            print("It is a draw!!")
            return '0'

def process(set1: list) -> tuple:
    '''
    This function takes in list as an input, and  validates if over various possible outcomes and 
    then returns a tuple containing the output and a corresonding element that will help in segregating in case of draw. For more detailed algorithm
    please check the readme file.
    # Input: 
        set1: list  of transformed hand
    # Returns:
        tuple: first element is the value in which the hand landed. 2 element is to help the show function to come to a conclusion in case of draw
    '''
    value_set_list = []
    suit_set_list = []
    for _ in set1:
        value,suit = _.split()
        value_set_list.append(value)
        suit_set_list.append(suit)
    color_check = check_for_color(suit_set_list)
    value_set_list = transform_value_list(value_set_list)
    sequence_check = check_for_number_sequence(value_set_list)
    print(color_check, sequence_check)
    if color_check == True:
        if sequence_check == True:
            x =  str(",".join(map(str,sorted(value_set_list,reverse = True))))
            print(x)
            if len(value_set_list) == 5:
                if str(",".join(map(str,sorted(value_set_list,reverse = True)))) == "14,13,12,11,10":
                    return 1,14
                else:
                    return 2, max(value_set_list)
            elif len(value_set_list) == 4:
                if str(",".join(map(str,sorted(value_set_list,reverse = True)))) == "14,13,12,11":
                    return 1,14
                else:
                    return 2, max(value_set_list)
            elif len(value_set_list) == 3:
                if str(",".join(map(str,sorted(value_set_list,reverse = True)))) == "14,13,12":
                    return 1,14
                else:
                    return 2, max(value_set_list)
        else:
            return 5, max(value_set_list)
    else:
        if sequence_check == True:
            return 6, max(value_set_list)
        else:
            duplicate_count = dict(Counter(value_set_list))
            duplicate_count = {k: v for k, v in sorted(duplicate_count.items(), key=lambda item: item[1],reverse =  True)}
            print(duplicate_count)
            if len(value_set_list) == 5:
                key1 = list(duplicate_count.keys())[0]
                key2 = list(duplicate_count.keys())[1]
                if duplicate_count[key1] == 4:
                    return 3, key1
                elif duplicate_count[key1] == 3:
                    if duplicate_count[key2] == 2:
                        return 4, key1
                    else:
                        return 7, key1
                elif duplicate_count[key1] == 2:
                    if duplicate_count[key2] == 2:
                        return 8, max(key1,key2)
                    else:
                        return 9, key1
                else:
                    return 10,max(value_set_list)
            
            elif len(value_set_list) == 4:
                key1 = list(duplicate_count.keys())[0]
                if duplicate_count[key1] == 4:
                    return 3, key1
                elif duplicate_count[key1] == 3:
                    return 7, key1
                elif duplicate_count[key1] == 2:
                    key2 = list(duplicate_count.keys())[1]
                    if duplicate_count[key2] == 2:
                        return 8, max(key1,key2)
                    else:
                        return 9, key1
                else:
                    return 10,max(value_set_list)
            elif len(value_set_list) == 3:
                key1 = list(duplicate_count.keys())[0]
                
                if duplicate_count[key1] == 3:
                    return 7, key1
                elif duplicate_count[key1] == 2:
                    key2 = list(duplicate_count.keys())[1]
                    return 9, key1
                else:
                    return 10,max(value_set_list)
                
def transform_value_list(value_set_list:list)->list:
    '''
    This function converts the list to integer format and also  converts values liek aces,etc to its numeric form
    # Input
        value_set_list: List of cards without suits. 
    # Returns
        Returns a list of card converted to numeric datatype.
    '''
    for i in range(len(value_set_list)):
        if value_set_list[i]=='jack':
            value_set_list[i] = 11
        elif value_set_list[i]=='queen':
            value_set_list[i] = 12
        elif value_set_list[i]=='king':
            value_set_list[i] = 13
        elif value_set_list[i]=='ace':
            value_set_list[i] = 14
    return list(map(lambda x: int(x),value_set_list))

def check_for_color(suit_set_list: list) -> bool:
    '''
    This function checks if the list contains the suits of the hands are all same or not
    # Input
        suit_set_list: list of suits of cards that a player is holding
    # Returns
        It returns a bool value which says whether they are of same color or not
    '''
    if len(set(suit_set_list)) == 1:
        return True
    else:
        return False

def check_for_number_sequence(value_set_list:list) -> bool:
    '''
    This function checks if the list caontaining all numeric value of card are in sequence
    # Input:
        value_set_list: List containing all the numeric value of cards
    # Output:
        It returns a bool value indicating whether they are in sequence or not.
    '''
    print(sorted(value_set_list))
    print(list(range(min(value_set_list),max(value_set_list)+1)))
    return sorted(value_set_list) == list(range(min(value_set_list),max(value_set_list)+1))

# set1 = ['9 hearts', 'king clubs', 'queen spades','jack diamonds','10 hearts']
# set2 = ['7 hearts', '7 diamonds', '7 spades','7 hearts','10 spades']
# show(set1,set2)
set1 = ['ace hearts', 'king clubs', 'queen hearts']
set2 = ['9 spades', 'ace diamonds', 'queen spades']
show(set1,set2)