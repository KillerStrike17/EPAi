from PIL import Image
import os

def image_converter(input_path, output_path,res_p,res_w,res_h):
    for filename in os.listdir(input_path):
        img = Image.open(input_path +"/"+ filename)
        img = img.resize()
        img.save(output_path +'/' +filename)
        del img
