<h1 align="center">Numeric Types II</h1>

<h2 align="center"> Assignment Question </h2>


1. Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
   1. It implements these functions (with exactly the same names)
      1. __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__
2. Your task is to write the above class, and then write all the functions. 
3. Then you need to write a test file, that tests all of the functions mentioned above + the other basic ones you have seen in the tests till now. Your unit test file must contain at least 25 tests, and they must not be repetitive. Some of the tests it must implement are:
   1. q + q + q ... 100 times = 100 * q
   2. q.__sqrt__() = Decimal(q).sqrt
   3. sum of 1 million different qs is very close to zero (use isclose)
   4. q1 and q2 returns False when q2 is not defined as well and q1 is False
   5. q1 or q2 returns True when q2 is not defined as well and q1 is not false
4. Upload your code and your test file and make use of GitHub Actions and submit the GitHub link. 
5. No README, no evaluation. README must explain each function and each test case. 150 points for your code. 250 points for your test file

<h2 align="center"> Assignment Solution </h2>

Here we are given functions __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__ and __bool__ to implement inside a class named Qualean which takes in an integer (either 1,0 or -1 ) and randimly selects a number from range -1 to 1 and multiplies to that number. Then the number is rounded off to 10th decimal digit. 
This Assignmented also required is to write minimum of 25 test cases but we wrote **34 test cases and implemented all functionalities**. 

### **Functions**

* #### **__init__ function**:

    Here the number selected from the user is passed as the paramter, it is generally of type Decimal. The choice of the user is then passed to number_transformation function which returns a value which is stored in self.value variable.

* #### **number_transformation function**:

    This function is called from the __init__ function. The choice of the user is passed as the parameter, it randomly selects a number between -1 and 1, converts to Decimal type, multiplied it with the choice of the user, rounded it off to 10th decimal place and returned back to __init__ function.

* #### **__and__ function**: 

    The task of this function is to perform and operation, it takes in other_object as parameter. If self.value is not zero, then it proceeds to check for the ottehr value else via shorthand returns False. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condiiton fails it returns False, else it performs an and operation and returns the result.

* #### **__or__function**:

    The task of this function is to perform or operation, it takes in other_object as parameter. If self.value is zero, then it proceeds to check for the ottehr value else via shorthand returns True. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condiiton fails it returns False, else it performs an or operation and returns the result.

* #### **__repr__ function**:

    Here we had to override this function, the task of this function is to return object represenation. Initially it was displaying the location of the object. Later we make it display the object and the user choice value.

* #### **__str__ function**:

    The task of this function is to return the string representation of the object. it is invoked when print() and str() is called. Initially is was also displaying the memory location of the object. Now is displaying the object and its user choice value.

* #### **__add__ function**:

    This function takes in value as a paramter, This value is added to the original value i.e. self.value and final result is returned back.

* #### **__eq__ function**:

    This function checks whether the numbers are equal or not. It takes in other number as paramter. The other number is compared with self. value number and the comparision result is returned i.e. True if they are equal else false. 

* #### **__float__ function**:

    This function has the task to convert the datatype of our value variable i.e. self.value, to float. The result is returned back.

* #### **__ge__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than or equal to value. 

* #### **__gt__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than value. 

* #### **__le__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than or equal to value. 

* #### **__lt__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than value. 

* #### **__invertsign__ function**:

    This function has the task to convert negative numbers postive and positive numbers negative. Once the conversion is done it returns the value

* #### **__mul__ function**:

    This function is similar as __add__ function, here the value parameter is multiplied with self.value and the result is returned back.

* #### **__sqrt__ function**:

    This function has the task to get the square root of the number. If self.value number is negative, it converts the number to postive, performs the square root and returns the result with an 'i' added in the result. Whereas if the number is positive, it follows the same process where as i is not added here. The result directly is returned back.

* #### **__bool__ function**:

    This function is used to convert the self.value variable to boolean value

### **Testcases**:

1. #### **test_function_names test**:

    This test is used to check whether the function name contains capital letters or not. According the python function naming convention, function shouldnt contain capital letters in the name of the function. Here is function calls a function called function_name_has_cap_latters which takes module as paramters, This function parses the module and feteches all the functions from the module. Then it does a capital letter check over it. If none are capital then it returns True, else False. If True is returned our test is passed. 

2. #### **test_readme_exits test**:

    This test function checks whether readme exists or not. README.md file is a very important file. It contains all the documentation of the code. Hence if the file exists at the location, this test is considered pass.

3. #### **test_readme_contents test**:

    The task of this test function is to check whether total number of words written in the readme file is more than **2000**. this will make sure that our documentation has a lot of detail.

4. #### **test_readme_proper_discription test**:

    The task of this function is to check whether the content of the readme is relevant to the code implemented or not. It will do a word check over the README file from a list containing important words which should be present in the documentation. 

5. #### **test_readme_file_for_formatting test**:

    The task of this function is to check whether the formatting has been done properly in the documentation i.e. headings and subheadings. It does so any counting the number of hashed. Here we are checking that the documentation should have minimum of **150** hashed. 

6. #### **test_indentations test**:

    Python is very prone to indentation erros to do improper use of tabs and spaces. Hence this function is implemented to check indentation is properly maintained, throughout the code. It counts the number of spaces before and statement and checks if that is a multiple of 4, if yes there there shouldnt be any indentation issues thus the test is passed else fail. 

7. #### **test_qualean_repr test**:

    This test is to check the representation of the qualean class. It should be displaying the old output which was displaying the meory it was stored in. 

8. #### **test_qualean_string test**:

    This test is to check whether the str and print function of the class have been updated or not i.e. if we do a print over to the class, it should not be giving the old display or message showing the memory where the object is stored. 

9. #### **test_add_function test**:

    This function is written to check the add functionality of the class. Here the random number is generated and is passed as a parameter to the __add__ function. The add function adds its value with the self.value and returns. We are verifying the value of add function with manually adding those numbers and checking its equality.

10. #### **test_equal_function_on_random test**:

    This test is to check __eq__ function, It will be one in a milion or more than that to get the same random number twice, hence we compare self.value with a random number and it should return false to be considered as Pass. 

11. #### **test_equal_function_on_same_number test**:

    This test is to check the behaviour of equal function on same value. Same value i.e. self.value is passed as parameter. Hence it should return output as True. 

12. #### **test_float_fucntion test**:

    This test is designed to check the __float__ functionality. The __float__  function converts the decimal type to float, hence here we assert the type of the number to be float.

13. #### **test_greater_than_equal_function test**:

    This test is to check __ge__ function. Here r1 is an object of Qualean class initialized with random user choice, where as r2 is initialized with user choice as 0. So if r2.value is positive or zero, then r2 should be greater than r1 and vice versa. 

14. #### **test_greater_than_function test**:

    This test is to check __gt__ function. Here r1 is an object of Qualean class initialized with random user choice from either 1 or -1, where as r2 is initialized with user choice as 0. So if r2.value is negative, then r1 should be greater than r2 and vice versa.

15. #### **test_invert_function test**:

    This test function checks __invertsign__ function, Here r1 is initialized randomly with a user choice and invertsing function is called. The output should be a postive number should become negatrive and a negative number should become positive. 

16. #### **test_less_than_equal_function test**:

    This test is to check __le__ function. Here r1 is an object of Qualean class initialized with random user choice, where as r2 is initialized with user choice as 0. So if r2.value is positive, then r1 should be less than r2 and vice versa. 

17. #### **test_less_than_function test**:

    This test is to check __lt__ function. Here r1 is an object of Qualean class initialized with random user choice from either 1 or -1, where as r2 is initialized with user choice as 0. So if r2.value is negative or zero, then r2 should be less than r1 and vice versa. 

18. #### **test_multiply_function test**:

    This test is very similar to test_add_function, here multiplication is the operation which is getting tested instead of addition.

19. #### **test_true_bool_function test**:

    This function checked the boolean value and return, so if the object is not zero, it will return True, therefore here it is being tested for userchoice as either 1 or -1

20. #### **test_false_bool_function test**:

    This function checked the boolean value and return, so if the object is zero, it will return False, therefore here it is being tested for userchoice or zero.

21. #### **test_check_sqrt test**:

    This test is to check the __sqrt__function. Here qualean class is initialized a random user choice and __sqret function is called. We get the value of quanlean class with get_iten function. Thus we take that value convert it to decimal and check its square root. If both are same, then the test is considered pass. 

22. #### **test_get_item test**:

    This test is to check the get_item function. The function should return self.value. A qualean class is initialized a random user choice, we are accessing its value by get_item and via object_name.value, if both are same then the test is pass.

23. #### **test_hundred_sum test**:

    This test is to check that if a value of Qualean class is added 100 times, it should be equal to 100*q. Therefore here we initialize Qualean class object with random user choice, Then we run a loop for 50 iterations and in it we call object.__add__ function, as it already add self.value to the value passes as parameter, it is working on two numbers than 1 in an iteration, hence running for 50 times rather 100. if both values are same then the test is considered pass.

24. #### **test_million_q_sum test**:

    In this test, we add randiom q values 1 million times and check its closeless with zero. As it is an addition operation, small numbers when added a million times will form a number greater than 0, hence this check should return False and that is considered as a pass.

25. #### **test_million_q_mul test**:

    In this test, we multiply randiom q values 1 million times and check its closeless with zero. As it is a multiplication operation, small numbers when multiplied a million times will form a very small number close to zero, hence this check should return True and that is considered as a pass.

26. #### **test_and_function_q2_undefined test test**:

    This test is to check 'and' functionality. A Qualean class r1 is initialized with random user choice and r2 is some number which is not a Qualean object. The and funnction should return False on comparision.

27. #### **test_and_function_q1_undefined test test**:

    This test is to check 'and' functionality. A Qualean class r2 is initialized with random user choice and r2 is a qualeanb object with value as 0. Thus and funnction should return False on comparision.

28. #### **test_and_function_both_undefined test**: 

    This test is to check 'and' functionality. A Qualean class r2 and r1 is initialized with userchoice as 0. Thus and function should return False on comparision as zero is considered false in python

29. #### **test_and_function_both_defined test**: 

    This test is to check 'and' functionality. A Qualean class r2 and r1 is initialized with random userchoice as -1 or 1. Thus and function should return True on comparision as both the objects are defined.

30. #### **test_or_function_q2_undefined test**: 

    This test is to check 'or' functionality. A Qualean class r1 is initialized with random user choice and r2 is some number which is not a Qualean object. The or funnction should return True on comparision.

31. #### **test_or_function_q1_undefined test**: 

    This test is to check 'or' functionality. A Qualean class r2 is initialized with random user choice and r2 is a qualeanb object with value as 0. Thus or function should return False on comparision.

32. #### **test_or_function_both_undefined test**: 

    This test is to check 'or' functionality. A Qualean class r2 and r1 is initialized with userchoice as 0. Thus or function should return False on comparision as zero is considered false in python

33. #### **test_or_function_both_defined test**:

    This test is to check 'or' functionality. A Qualean class r2 and r1 is initialized with random userchoice as -1 or 1. Thus or function should return True on comparision as both the objects are defined.

34. #### **test_decimal_upto_ten test**:

    This test is to check whether the rounnding off function is working properly or not. Here if the number is postive, its length when converted to string should bne 12 i.e. 10 digits after decimal, 1 for decimal and 1 for digit before decimal. And for negative numbers the length should be 13, 1 extra for the negative sign.

### **Test_output**

<div align="center">
  <center>
    <img src="Assets/output.jpg"">
  </center>
</div>


### **Result**

**All test have been passed successfully**

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>