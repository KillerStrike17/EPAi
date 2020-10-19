from PIL import Image
import os

def image_resizer(input_path, output_path,res_p=0.50,res_w=500,res_h=500,option=1):
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
        # print(output_path +'/' +filename)
        del img
