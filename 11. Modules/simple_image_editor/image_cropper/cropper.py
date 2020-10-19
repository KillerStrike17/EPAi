from PIL import Image
import os

def image_cropper(input_path, output_path,crp_px=224,crp_p = 0.5,option=1):
    not_cropped = []
    for filename in os.listdir(input_path):
        img = Image.open(input_path +"/"+ filename)
        width, height = img.size
        
        if option == 1:
            if crp_px>width or crp_px>height:
                not_cropped.append(filename)
            else:

                left = (width - crp_px)/2
                top = (height - crp_px)/2
                right = (width + crp_px)/2
                bottom = (height + crp_px)/2
                # Crop the center of the image
                img = img.crop((left, top, right, bottom))

        elif option == 2:
            if (crp_p*width)>width or (crp_p*height)>height:
                not_cropped.append(filename)
            else:
                left = (width - int(width*crp_p))/2
                top = (height - int(height*crp_p))/2
                right = (width + int(width*crp_p))/2
                bottom = (height + int(height*crp_p))/2
                # Crop the center of the image
                img = img.crop((left, top, right, bottom))
        
        img.save(output_path +'/' +filename)
        # print(output_path +'/' +filename)
        del img
    return not_cropped