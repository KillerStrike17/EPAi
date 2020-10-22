from PIL import Image
import os

def image_converter(input_path:str, output_path:str)->None:
    """
    This Function takes in input and output path as string and 
    converts the png to jpg.
    """
    for filename in os.listdir(input_path):
        img = Image.open(input_path +"/"+ filename)
        img = img.convert('RGB')
        img.save(output_path +'/' +filename.split('.')[0] + '.jpg')
        del img
