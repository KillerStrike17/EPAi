<h1 align="center">Modules</h1>

<h2 align="center"> Assignment Question </h2>

1. Create these modules:
    1. jpg/jpeg to png conversion (use PIL library) j2p
    2. png to jpg conversion (use PIL library) p2j
    3. image resizer that can resize bulk images with these features:
       1. resize by user determined percentage (say 50% for height and width) (proportional) res_p
       2. resize by user determined width (proportional) res_w
       3. resize by user determined height (proportional) res_h
    4. image cropper that can crop bulk images with these features:
       1. center square/rectangle crop by user-determined pixels crp_px
       2. centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
       3. it let's user know which all images were not cropped due to size mismatches
    5. a __main__ module that exposes all these features (using argparse)
    6. finally create an zipped app, that exposes all of these features
2. How to test your code:
   1. each module must be independently available and tested (write test to check whether you can call them from command line) 
   2. each feature must be available via argument selection
   3. images must not be required to be in the same folder where your code is
   4. final test:
      1. download 20 jpeg images of size more than 1000x1000
      2. convert to png
      3. convert to jpg
      4. resize to 80%
      5. resize to 500 width
      6. resize to 500 height
      7. all this using your zipped app
      8. center crop to 224x224
3. You must have at least 20+ test. (github actions)
4. Each test is worth 50 points (no additional points for more tests). So total 1000 pts.
5. Failing test, reduces mark. 

<h2 align="center"> Assignment Solution </h2>

In this problem we had to create 4 modules i.e. to convert jpg image to png image, png image to jpg image, resizing the image and cropping the image. Then we have to make a main module containing all of these.

We will split these modules in task and will solve it part by part.
### **Tasks**
#### Task 1

In this task we create a j2p module which will convert the jpg images to png. Here we pass the input and output image path, Then we load every image in the folder using PIL and then convert it to png.

#### Task 2

In this task we create a p2j module which will convert the png images to jpg. Here we pass the input and output image path, Then we load every image in the folder using PIL and then convert it to jpg.

#### Task 3

In this task we need to create a resize module. This module takes in option as an input. This option will decide which resizing task has to be done. Option 1 will resize the image using resize percentage, option 2 will resize using resize width and option 3 will resize using resize height. We pass in input directory, the function reads all the images and opens using pil one by one and then converts and stores back to the output directory.

#### Task 4

In this task we need to create a cropping module. This module takes in option as an input. This option will decide which cropping task has to be done. Option 1 will crop the image using pixel value and option 2 will crop using pixel percentage. We pass in input directory, the function reads all the images and opens using pil one by one and then converts and stores back to the output directory.

#### Task 5

Here we create a final module incorporating all the modules. The main function takes in all the arguments required for each module. This function also takes in choice function which will decide which function to run. 

### **Test cases**

There are test case for to check the working of each task function. There are some general test cases of checking documentation of the project and the python files.

---
<h3 align = "center"> Made with ❤ & 🍻 by KillerStrike</h3>