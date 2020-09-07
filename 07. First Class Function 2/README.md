<h1 align="center">First Class Functions Part 2</h1>

<h2 align="center"> Assignment Question </h2>

1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100
2. Using list comprehension (and zip/lambda/etc if required) write an expression that: PTS:100
   1. add 2 iterables a and b such that a is even and b is odd
   2. strips every vowel from a string provided (tsai>>t s)
   3. acts like a ReLU function for a 1D array
   4. acts like a sigmoid function for a 1D array
   5. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200 (Links to an external site.)
4. Using reduce function: PTS:100
   1. add only even numbers in a list
   2. find the biggest character in a string (printable ascii characters)
   3. adds every 3rd number in a list
5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10 < DD < 99 & 1000 < DDDD < 9999 PTS:100
6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:100

<h2 align="center"> Assignment Solution </h2>

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

#### **Task 1**

In this task we are asked to check whether a number falls in the fabonacci series or not using **list**, **filters** and **lambda functions**. Here we create a function Fibonacci which returns the fabonacci series, Then randomly a list of numbers is generated and matched against the fabonacci list and the matched list is displayed.

#### **Task 2**

All the sub tasks here has to be done using list comprehension. 
   * A We need to take two list and check each elements, if element of list a is even where as element of list b is odd, we will add them else we will ignore them
     * User sends two list
     * The list is zipped and iterated
     * First tuple element is checked for evenness and second tuple element is checked for oddness
     * if the condition is matched those elements are added
   * We have to remove vowels from the string
     * iterate through string
     * check if element falls in the vowel category
   * Make a Relu Function
     * Iterate over the list of numbers
     * if Negative convert to zero, 
     * else leave as it is
   * Make a sigmoid function
     * Create a sigmoid function that takes integer as an input and returns its sigmoid form
     * iterate through the list that user provided and pass each element to sigmoid function
     * Store each element to a new list and return the list
   * Make an Alphabet Cipher
     * check order of each character
     * if order + 5 is greater than order of z which is 122, 
       * then substract 26 from the order of character +5 
     * else add 5 to the order of character
     * join the list to make string
     * return string

#### **Task 3**

In this function the user inputs the paragraph of length 200, if the paragragh word count is less than 200, it raises an error. There is predefined list of bad words [link](https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt ), it is fetched and converted to list. Then the list is check with each word in the para, of any word is found it is alerted.

#### **Task 4**

Here we need to perform tasks using reduce function

*   Add Only even numbers in the list
    *   filter is applied over the list to fetch the even numbers
    *   all the numbers are added using reduce function and lambda function performing the addition
*   To find the biggest character
    *   Here Max function is used
    *   Initial value is " " as this is the first ascii printable character
    *   the input string as passed as argument and max character is returned
*   Add Every 3 number in the list
    *   filter list to get every 3rd element i.e. at index 2,5,8,..
    *   use lambda function to perform addition over that list
    *   return the sum

#### **Task 5**:

In this task we had to create function using list comprehension to generate license plates. Here the format is KADDAADDDD where A is for Alphabet uppercase and D is for digit. random value is generated for DD and DDDD in the range 10 to 99 and 1000 to 9999 respectively. AA is also generated randomly using Ascii.uppercase characters.
Then the list is returned

#### **Task 6**:

* In this task we can switch between KA/DL as the statecode , here the user can give a list of numbers which they want in their number plate
* In task 2 of this we need to create a function which allows custom number plate and statecode and we need to create a partial function that calls this function providing a default number plate where as custom statecode.
  

### Test Cases

Here we have written a lot of testcases to check each functionality thoroughtly as out code shouldnt be breaking. Each function has it own test case and they are also checked for doc string and annotations

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>