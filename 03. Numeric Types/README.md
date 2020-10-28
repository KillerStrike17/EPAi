<h1 align="center">Numeric Types I</h1>

<h2 align="center"> Assignment Question </h2>

Use this link: [Assignment Link](https://classroom.github.com/a/o3ZNYvMJ). It will creata a repo for you, complete all the test cases and functions of that repo.

<h2 align="center"> Assignment Solution</h2>

Here we manually implemented functions like round, math.isclose, math.trunc and encoded_from_base10 without using inbuilt functions like int, float, ceil, trunc, floor, isclose and round.

### **Functions**

#### **Implementing encoded_from_base10 function aka encoded_from_base10 function**

This function takes in three arguments i.e. number, base, and digit_map. we had to raise an error of ValueError with proper description if the base value
was less than 2 or more than 36. We also had to raise an error of ValueError with proper description if there was insufficient digit_map length as compared to base or there were
repeating characters in digit_map as the mapping has to be unique.

**Algorithm**
* Check for Negative, if yes flag it and make the number positive for performing operations. Here we used check variable to do so.
* create a list variable to store the remainders
* Run loop until number is less than 0
    * get remainder of number when divided by base
    * reassign the original number to the quotient value
    * insert the remainder to list variable
* check flag, if yes add a negative sign in front of output
* run a lambda function to map the output list to digit_map string.
* return the value
Python provides us inbuilt functions like bin(), oct(), hex(), etc to convert the number to binary, octal and hexadecimal format from decimal format.

#### **Implementing math.isclose function aka float_equality_testing function**

This function takes in two parameters i.e. a and b which are the two numbers whose closeness we need to find out.
Here we assume the relative and absolute error as 1e-12 and 1e-05 respectively. If absolute error is not given, it is
assumed to be 0.

**Algorithm**
* Finding total tolerance using the formulae `max(rel_tol x (max(abs(number1)),(abs(number2))),abs_tol)`
* calculate the absolute difference between the numbers
* compare it with total tolerance
* If absolute difference is less than total tolerance then return true else false

#### **Implementing truncation function aka manual_truncation_function**

This function is written to mimic the math.trunc function.
This function returns the integer value of the floating point number
For example:

`math.trunc(10.4) = 10`
`math.trunc(-10.4) = -10`

We can get integer value out as quotient if we divide the number by 1.
**Algorithm**
* check if the number is positive or negative.
* If positive, find quotient of the number when divided by 1
* else find quotient of the number when divided by 1 and add 1 to the final answer
* return the output.

The reason of adding 1 in negative numbers is that when we divide a negative number by a
positive number it gives the quotient variable a bigger value as compared to the dividend. Hence to compensate that we add 1 to it.


#### **Implementing rounding off function aka manual_rounding_function**

The solution of this function is inspired from the solution of truncation function. Here also we use the concept of div and module to get the quotient and remainder out.

**Algorithm**
* if number is positive
  * calculate quotient and remainder using div and mod respectively.
  * if remainder is greater than 0.5 then round it off to the bigger number by adding 1 to the quotient
* if the number is zero, return zero
* else if the number is negative, we add 1 to the quotient. The reason is same as mentioned in the documentation of truncation function.
  * if the remainder is less than 0.5, then we add 1 to the quotient.
* return the value.

We may still be using the inbuilt functions for our work but the task of this exercise was to understand the implementation of it by taking the abstraction away by Implementing it.

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>