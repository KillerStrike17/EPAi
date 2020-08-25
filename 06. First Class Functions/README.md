<h1 align="center">First Class Functions Part 1</h1>

<h2 align="center"> Assignment Question </h2>

```
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
```

<div align="center">
  <center>
    <img src="Assets/Poker Ranking.jpg">
  </center>
</div>

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 150 pts

###  Basics (applicable to 2/3 above):

1. Proper readme file - 50 (if not there then 0)
2. Docstrings must, and it must mention what the function is doing (2, 3) - 50
3. Write annotations for 3 - 50 pts
4. Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
5. Submit Github link with all test files and github actions in place. 
   
<h2 align="center">Assignment Solution </h2>

Here we are asked to implement a combined version of poker and teen patti. 

### The rules of the games

1. Players can get either of 3, 4 or 5 cards.
2. 2 players play the game
3. Once receiving the game, both the players should their cards
4. The winner is decided on the basis of the order shown in the image above i.e. Royal Flush is superior to all, straight flush is superior to all except royal flush and so on.
   
Based on the Rules I have deviced a very simple algorithm:

### Algorithm

1. First we generate a deck either by the generator function or list comprehension done in task 2 and 1 respectively. 
2. Then we shuffle the deck of card and randomly select either3, 4 or 5
3. we distribute the cards
4. The player shows the card
5. Each hand is processed under process function which calls in transform function
6. Transform function converts the cards like ace,king, queen and jack to numeric value(easy for evaluation)
7. under the process function
   1. we first check if the colors of all the cards are same or not
      1. if they are same we check for sequence
         1. if sequence is same, we match it with royal flush sequence, if true we return 1,14 (1 represents the listing from the image and 14 is the max value of the array corresponding to ace)
         2. else we return 2, max(hand) (straight flush)
      2. else we return 5, max(hand) (flush)
   2. else we check for sequence
      1. if true, then we return 6,max(hand) (straight)
      2. else we do a count of each number i.e. how many times they are being repeated and we sort them from higher to lower, then we check for length of the hand as algorithm now is specifically developed for ecah hand
         1. if length is 5
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we check for the next number count
               1. if the next number count is 2, we return 4, number(having count of 3) (Full House)
               2. else we return 7, number(3 of a kind)
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         2. if the length is 4
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we return 7, number(3 of a kind) as here full house doesnt makes sense in 4 cards
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         3. else if the number is 3:
            1. we check if a number is repeated 3 time, we return 7, number(3 of a kind)  as here full house and 4 at a time doesnt makes sense in 3 cards
            2. else if the number is repeated 2 times, we return 9,number as 2 of a kind doesnt makes sense in 3 cards
            3. else we return 10, max(hand)
8. Then once we get these tuples values, we check if the first element is greater of player 1 than player 2, then player 2 wins else vice versa.
9. if both have same, then we check the max value, i.e. the second element, so here if the second element of player 2 is more than the first player then second player wins and vice versa
10. if both the players have same secopnd value, then the game ends in a draw.

### Functions

|SR No. | Name | Functionality |
|--- | --- | --- |
|1 | generate_deck_using_list_comprehension | This function takes in suits and values as input and returns the combined deck using list comprehension as backend|
|2 | generate_deck| This function takes in suits, values and deck as input and returns the combined deck using loops as backend|
|3 |poker_x_teen_patti | This function takes in deck and total cards in hand as input, it calls show function in it. The function returns result as an output|
| 4| show | This Function takes in hands as input, i.e. set1 and set2. It internally calls process function which return result tuple. This function then computes the final result and returns that result.|
| 5| process | This function takes in list as an input, computes which category the hand falls in and returns the category | 
| 6| transform_value_list | This function takes in list as input  i.e. hand of the player and converts the list into int datatype and returns that list back| 
|7|check_for_color | This function takes in list as input i.e. the suits of the hand and checks whether they are same or not|
| 8 |check_for_number_sequence | This function takes in list an input (the hand of the player), then it checks whether it is in sequence or not | 

### TestCases

Here we have written a lot of testcases to check each functionality thoroughtly as out code shouldnt be breaking. 
To test each combination for each type of hand I have written a test for each, so the test cases in format ```test_show_for_3_for_6_v_10``` represents for hand length of 3 for combination of player 1 having a hand of straight and player 2 having a hand of high card and we check the result. Rest of the test cases are self explanatory.

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>