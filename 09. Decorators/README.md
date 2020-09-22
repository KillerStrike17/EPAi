<h1 align="center">Decorators</h1>

<h2 align="center"> Assignment Question </h2>

Write separate decorators that:
1. allows a function to run only on odd seconds - 100pts
2. log - 100pts
3. authenticate - 300pts
4. timed (n times) - 100pts
5. Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) - 200pts
Write our htmlize code using inbuild singledispatch - 100pts
No readme or no docstring for each function, or no test cases → 0.

Write test cases to check boundary conditions that might cause your code to fail. 

<h2 align="center"> Assignment Solution </h2>

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

#### **Task 1.1**

Here in this task we need to create a decorator which runs the function if the seconds of the current time is odd. Here I created `dec_factory_1` which takes in current time as a parameter. It has a closure defined in which takes in function as a parameter adn wraps it to the `inner` function which checks for seconds and runs the function if the seconds is odd. 

#### **Task 1.2**

Here in this task we need to create a decorator which returns the information regarding the class. Here we define`info` function which takes in the class object as parameter and returns a list containing the information.

#### **Task 1.3**

Here in this function we need to create an `authenticate` function which takes in `user password`, matches with the one present in the database and if matched allows the function to run which is passed as the parameter to the closure defined in this function.

#### **Task 1.4**

Here in this function we need to create a decorator which takes in reps as an input which contains the numbers as parameter i.e. how many times the function will run. Timed function is defined inside the decorator which takes in function as an input and runs that function reps number of time.

#### **Task 1.5**

Here in this function he had to create an access function which allows user to access functions according to the level of clearance. Hence here we defined a function `access_level` which takes in the level as parameter. Inside this function we have defined the access function, if the level has the clearance then the function is run else it raises an error.

#### **Task 2**

Here in this function we need to define functions which can convert normal texts to html formats. Here we convert integers, strings, floats, tuple, set, list, frozen set, dictionary and string.

### **Testcases**

The test cases are defined to check each task and their attributes i.e. whether they are closure, docstring, or decorators

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>