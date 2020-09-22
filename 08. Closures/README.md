<h1 align="center">Closures</h1>

<h2 align="center"> Assignment Question </h2>

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
2. Write a closure that gives you the next Fibonacci number - 100
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 

<h2 align="center"> Assignment Solution </h2>

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

#### **Task 1**

In this task we need to create a function to check each function has docstring and docstring should be of 50 character each. here we create docstring_check function which takes the function who has to be checked as a parameter. here we have defined `min_count` which is the minimun character count. Then we have defined another function `mycount` which is a closure which takes in mincount as non local parameter and then checks its length by fetching the dfocstring of the function. It returns a True if docstring is more than 50 characters else returns false

#### **Task 2**

In this Task we need a function to calculate the next fibonacci number, here we define `first` and `second` number as free variables i.e. will be used by `generate_my_next_number` closure and that closure will add these numbers and then will update the value of these numbers and then will return the added result

#### **Task 3**

In this task we need to calculate how many times a function is being called, so to do that we define a `mycounter` function with `count` as free variable. Then we defined `inner` function which updates the `count` value and returns it.

#### **Task 4**

This task is slight addition to the previous task, here we define 4 functions i.e. `add`, `mul`, `sub`, and `div`. in this task we keep a global dictionary `mydict` to have a check on how many times each operation is being called. so here we define a function `mycounter_with_global_dict` which takes in function as a parameter, the    free variable `count` is the value obtained from the key of the global dictioanry as function name. Here we define a closure called inner which takes in  `a` and `b` as parameters, which are the numbers over which each operation will be perfomed. The function updated the global dictionary and returns the count

#### **Task 5**

This task is and upgraded version of task 4, The only difference is that instead of updating in global variable we pass a dictionay as a parameter and that gets updated. 

### Test Cases

There are test case for to check the working of each task function. There are some general test cases of checking documentation of the project and the python files,There are testcases to check to whether they are acutally closures or not.

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>