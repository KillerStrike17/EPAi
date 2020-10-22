from PIL import Image
import os

def image_resizer(input_path:str, output_path:str,res_p:float=0.50,res_w:int=500,res_h:int=500,option:int=1)->None:
    """
    This Function takes in input, output path as string, resize percent as float, resize width and height and option as
    int. This function has the task to resize the image. 
    """
    for filename in os.listdir(input_path):
        img = Image.open(input_path +"/"+ filename)
        width, height = img.size
        if option == 1:
            img = img.resize((int(width*res_p),int(height*res_p)))
        elif option == 2:
            img = img.resize((res_w,height))
        elif option == 3:
            img = img.resize((width,res_h))
        img.save(output_path +'/' +filename)
        del img
