<h1 align="center">Named Tuples</h1>

<h2 align="center"> Assignment Question </h2>

1. Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings). - 250
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250
3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500

Add the notebook as well to your github where logs can be visible. 

<h2 align="center"> Assignment Solution </h2>

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

`Note: For Task 1 and 2, I am using size as 20000, because it gives me much better results.`

#### **Task 1**

In this task we need to create fake profiles using faker library and store that inside named tuple. Then we need to create a namedtuple containing all the profiles and we need to perform the following operations:

**Largest Blood Type**

Here I am using lambda function and mapping operation to extract the blood type, Then we are storing it map object to list and pass it as a parameter to mode function defined in statistics library. We measure the time and record the readings. 

**Mean Current Location**

Here I am using lambda function and mapping operation to extract the tuple containing the location, Then we access each tuple and  perform an average operation and return the value with the time stamp.

**Average Age**

Here I am using lambda function and mapping operation to extract the birthdate, We then obtain the age by substracting the birthdate with current date. We then perform the average operation over the age and record the time.

**Oldest Person**

Here I am using lambda function and mapping operation to extract the birthdate, I then perform a minimum operation with key as the extracted birthdate and record the time.

#### **Task 2**

It is pretty much the same as done in task 1 except it is done via dictionary in dictionary. 

#### **Task 3**

Here in this task we need to create a stock market scenario by generating 100 company data. Name is created using faker library. Symbol is generating using random sample from ascii characters. Weights are randomly generated in range 0 to 1 and stored in namedtuple. Then the weights are being normalized and are stored in tuple. open value is generated from randint from range 1000 to 50000 multiplied. High, Low and close is generated from multiplying the open value with randomly generated value from range 0.85 to 1.15, 0.7 to 1 and 0.7 to 1.15 respectively.We then compare the high, open, close and low value for border conditions. Then these randomly generated values are stored in named tuples.

### Test Cases

There are test case for to check the working of each task function. There are some general test cases of checking documentation of the project and the python files,There are testcases to check to whether they are acutally closures or not.

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>