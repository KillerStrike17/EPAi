<h1 align="center">Functional  Paramteres</h1>

<h2 align="center"> Assignment Question </h2>

### Time It Function

Write a function which gives out average run time per call, such that it's definition is:

```def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.```

We should be able to call it like this:

* ```time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)```
* ```time_it(squared_power_list, 2, start=0, end=5, repetitons=5)``` #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
* ```time_it(polygon_area, 15, sides = 3, repetitons=10)``` # 15 is the side length. This polygon supports area calculations of upto a hexagon
* ```time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)``` # 100 is the base temperature given to be converted
* ```time_it(speed_converter, 100, dist='km', time='min', repetitons=200)``` #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph

### Evaluation

* expecting you to add all the test conditions to check each of the above 6 functions. All must be checked for "basics"
* if you change any character in def time_it(fn, *args, repetitons= 1, **kwargs): then 0 marks
* your test file must have atleast 25 tests
* upload to github/github-actions and then share the github URL
* 250 for the code and 250 for the tests (code + tests getting cleared)

<h2 align="center"> Assignment Solution </h2>

Here we have to implement 6 functions and a helper functions i.e. 
* time_it
* myprint
* square_power_list
* create_list
* polygon_area
* temp_convereter
* speed_converter
* create_list (helper function)  

#### time_it function:

```def time_it(fn, *args,repititions = 1,**kwargs):```

This function takes in function name as paramter and stored it value in fn, this it takes the **positional arguments** of that funciton and stores then in ***args**, then it takes repetition parameter which tells how many time the function has to run in the time_it function and finally it takes and stores all the **keyword arguments** in ****kwargs**. By default, it takes the ```repititions``` value as 1

The function calculates the duration of the run time and fetches the result of the function and sends both back in the form of tuple.

#### myprint function:

```def myprint(*args,**kwargs)```

This function takes in the positional and keyword arguments as paramters and passes it on the print function. The print function then reads positional arguments and takes that as the input to the printed out, the keyword arguments specifies the values to the paramters of the print function i.e. ```sep``` and ```end```.

#### squared_power_list function:

```def squared_power_list(no, start = 0, end = 1)```

The task of this function is to generate a list in the range (```start```, ```end```+1) with power of ```no```.
This function takes in 3 parameters i.e. no, start and end. no is the positional argument where as start and end are keyword argument. By default, it takes the ```start``` and ```end``` as 0 and 1 respectively.
This function call a create list helper function helper function which returns the generated list. Then the power of each number of the list is calculated. Then the listed is returned.

#### create_list helper function:

```def create_list(start = 0, end = 1)```

This function is used to create a list in the range of ```start``` to ```end```. By default, the values of ```start``` and ```end``` is 0 and 1 respectively. 
If the ```end``` value is greater than ```start```, then it raises an ```ValueError``` else performs the operation to generate the list and returns that list.

#### polygon_area function:

```def polygon_area(length, sides = 3)```

This function returns the area of the polygon, It takes in 2 paramters i.e. ```length``` which is a positional argument and ```sides``` which is keyword argument. 
If the ```sides``` is less than 3 or greater than 6 and if the length is less than or equal to 0, it raises a ```ValueError```. 

Otherwise, the area is calcualte with the formulae:

and then the area is returned. 


#### temp_converter function:

```def temp_converter(temperature,temp_given_in = 'f')```

This function has the task to convert temperature in Celcius to Fahrenheit and vice versa. It takes ```temperature``` as positional argument and ```temp_given_in``` as keyword argument.
It checks if the given temperature is below absolute zero (as there cannot be any temperature below that) i.e. **-273.15** in celcius and **-459.67** in Fahrenheit, it raises a ```ValueError```. 
Otherwise if the temperature is in fahrenheit, 

formula is used to convert it to celcius and if the temperature is in celcius then 

formula is used to convert it to fahrenheit.
Then the converted temperature is returned back.

#### speed_converter function:

```def speed_converter(speed,dist = 'km',time = 'min')```

This function is used to convert the given speed in other units i.e. distance can be converted to kilometer(km), meter(m), feets(ft) or yards(yrd) and time can be converted to day,hour(hr),minutes(min),seconds(s), and microsecond (ms).
if the speed is less than zero,then it raises a 'ValueError' as speed cannot be negative else it converts in the desired format and returns the output. The function takes in ```speed``` as position argument and ```dist``` and ```time``` and keyword argument. By default, the input is in km per hr format, hence the default values of the keyword argument is that respectively. 

The formula used for conversion are:

<center>

|Sr No.| From | To | formulua |
|---| --- | --- | --- |
| 1 | km | m | 1 km = 1000 m |
| 2 | km | ft | 1 km = 3280.84 ft |
| 3 | km | yrd | 1 km = 1093.61 yrd |
| 4 | hr | day | 1 hr = 1/24 day |
| 5 | hr | m | 1 hr = 60 minutes |
| 6 | hr | s | 1 hr = 3600 seconds |
| 7 | hr | ms | 1 hr = 3600000 microseconds |

</center>

### Test Cases

Here are the 49 testcases which I ran to test the functions

<center>

|Sr No.| TestCase Name | Testcase Description |
|---| --- | --- |
| 1 | test_function_names | This test is check whe|
| 2 | test_readme_exists | This test is check whe|
| 3 | test_readme_contents | This test is check whe|
| 4 | test_readme_proper_description | This test is check whe|
| 5 | test_readme_file_for_formatting | This test is check whe|
| 6 | test_indentations | This test is check whe|
| 7 | test_print | This test is check whether the myprint function words the way it is designed to work, i.e. it prints the statement in the format user asked it to do.|
| 8 | test_create_list_end_gt_start | This test case is to check ```create_list``` function when the ```end``` value is more than the ```start``` value, the function should create the list and return it. |
| 9 | test_create_list_end_lt_start |This test case is to check ```create_list``` function when the ```end``` value is less than the ```start``` value, the function should raise a value error.|
| 10 | test_create_list_end_eq_start | This test case is to check ```create_list``` function when the ```end``` value is equal to the ```start``` value, the function should create the list and return it.|
| 11 | test_square_power_list_for_positives_for_end_gt_start | This test case is to check the ```squared_power_list``` function for positive values, when the ```end``` value is more than the ```start``` value, the function should return the powered list|
| 12 | test_square_power_list_for_positives_for_end_eq_start | This test case is to check the ```squared_power_list``` function for positive values, when the ```end``` value is equal to the ```start``` value, the function should return the powered list|
| 13 | test_square_power_list_for_positives_for_end_lt_start | This test case is to check the ```squared_power_list``` function for positive values, when the ```end``` value is less than the ```start``` value, the function should raise ```ValueError```|
| 14 | test_square_power_list_for_negatives_for_end_gt_start | This test case is to check the ```squared_power_list``` function for negative values, when the ```end``` value is more than the ```start``` value, the function should return the powered list |
| 15 | test_square_power_list_for_negatives_for_end_eq_start | This test case is to check the ```squared_power_list``` function for negative values, when the ```end``` value is equal to the ```start``` value, the function should return the powered list|
| 16 | test_square_power_list_for_negatives_for_end_lt_start | This test case is to check the ```squared_power_list``` function for positive values, when the ```end``` value is less than the ```start``` value, the function should raise ```ValueError```|
| 17 | def test_polygon_area_for_length_negative | This test is check the ```polygon_area function``` over negative ```length```, the funciton should raise ```ValueError```|
| 18 | test_polygon_area_for_length_zero |This test is check the ```polygon_area function``` over zero ```length```, the funciton should give area as 0|
| 19 | test_polygon_area_for_sides_lt_3 | This test is check the ```polygon_area function``` over ```sides``` less than 3, the funciton should raise ```ValueError``` |
| 20 | test_polygon_area_for_sides_gt_7 | This test is check the ```polygon_area function``` over ```sides``` greater than 7, the funciton should raise ```ValueError```|
| 21 | test_polygon_area_for_3_sides | This test is check the ```polygon_area function``` over area of regular triangle, the funciton should return area which should match with the formula |
| 22 | test_polygon_area_for_4_sides | This test is check the ```polygon_area function``` over area of regular quadrilateral, the funciton should return area which should match with the formula |
| 23 | test_polygon_area_for_5_sides | This test is check the ```polygon_area function``` overarea of regular pentagon, the funciton should return area which should match with the formula |
| 24 | test_polygon_area_for_6_sides | This test is check the ```polygon_area function``` overarea of regular Hexagon, the funciton should return area which should match with the formula |
| 25 | test_temp_converter_lt_absolute_zero_for_f | This test is to check the ```temp_converter``` function over value below absolute zero in Fahrenheit, which is **-459.67 F**, it should raise a ```ValueError```|
| 26 | test_temp_converter_lt_absolute_zero_for_c | This test is to check the ```temp_converter``` function over value below absolute zero in Celcius, which is **-273.15 C**, it should raise a ```ValueError```|
| 27 | test_temp_converter_f_to_c | This test is to check the ```temp_converter``` function over temperature conversion from fahrenheit to celcius, the result should match from the one generated from this formuala |
| 28 | test_temp_converter_c_to_f | This test is to check the ```temp_converter``` function over temperature conversion from celcius to fahrenheit, the result should match from the one generated from this formuala |
| 29 | test_speed_conversion_negative_speed_test | This test is check the ```speed_converter``` function over negative speed values, as there cannot be negative speed, hence the code should raise a ```ValueError```|
| 30 | test_speed_converion_km_per_hr | This test is check the ```speed_converter``` function over km/hr conversion, as the input is in km/hr, it should return same value|
| 31 | test_speed_converion_km_per_day |This test is check the ```speed_converter``` function over km/day conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 32 | test_speed_converion_km_per_min | This test is check the ```speed_converter``` function over km/min conversion, as the input is in  km/hr, the return value should match the result generated from the formula|
| 33 | test_speed_converion_km_per_second | This test is check the km/s, the return value should match the result generated from the formula|
| 34 | test_speed_converion_km_per_micro_seconds | This test is check the ```speed_converter``` function over km/ms conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 35 | test_speed_converion_m_per_hr | This test is check the ```speed_converter``` function over m/hr conversion, as the input is in  km/hr, the return value should match the result generated from the formula|
| 36 | test_speed_converion_m_per_day | This test is check the ```speed_converter``` function over m/day conversion, as the input is in  km/hr, the return value should match the result generated from the formula|
| 37 | test_speed_converion_m_per_min |This test is check the ```speed_converter``` function over m/min conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 38 | test_speed_converion_m_per_second | This test is check the ```speed_converter``` function over m/s conversion, as the input is in  km/hr, the return value should match the result generated from the formula|
| 39 | test_speed_converion_m_per_micro_seconds | This test is check the ```speed_converter``` function over m/ms conversion, as the input is in  km/hr, the return value should match the result generated from the formula|
| 40 | test_speed_converion_yrd_per_hr |This test is check the ```speed_converter``` function over yrd/hr conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 41 | test_speed_converion_yrd_per_day | This test is check the ```speed_converter``` function over yrd/day conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 42 | test_speed_converion_yrd_per_min | This test is check the ```speed_converter``` function over yrd/min conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 43 | test_speed_converion_yrd_per_second | This test is check the ```speed_converter``` function over yrd/s conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 44 | test_speed_converion_yrd_per_micro_seconds | This test is check the ```speed_converter``` function over yrd/ms conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 45 | test_speed_converion_ft_per_hr | This test is check the ```speed_converter``` function over ft/hr conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 46 | test_speed_converion_ft_per_day | This test is check the ```speed_converter``` function over ft/day conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 47 | test_speed_converion_ft_per_min | This test is check the ```speed_converter``` function over ft/min conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 48 | test_speed_converion_ft_per_second | This test is check the ```speed_converter``` function over ft/s conversion, as the input is in km/hr, the return value should match the result generated from the formula|
| 49 | test_speed_converion_ft_per_micro_seconds | This test is check the ```speed_converter``` function over ft/ms conversion, as the input is in km/hr, the return value should match the result generated from the formula|

</center>


---
<h3 align="center"> Made with love by KillerStrike</h3>
