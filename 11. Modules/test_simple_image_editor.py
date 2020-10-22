import os,inspect,re,random
import pytest
import simple_image_editor as sie
import subprocess
from simple_image_editor.j2p import converter
from simple_image_editor.p2j import converter_jpg
from simple_image_editor.image_resizer import resizer
from simple_image_editor.image_cropper import cropper

README_CONTENT_CHECK_FOR = [
    'j2p',
    'p2j',
    'resize',
    'cropping',
    'module',
    'percentage',
    'main'
]

def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(sie, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 25, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_j2p():
    cmd = 'python3 simple_image_editor/j2p --input_path ./Input_image_folder_jpg --output_path ./Output_folder_png'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_p2j():
    cmd = 'python3 simple_image_editor/p2j --input_path ./Input_image_folder_png --output_path ./Output_folder_jpg'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_image_resize_percent():
    cmd = 'python3 ./simple_image_editor/image_resizer --input_path ./Input_image_folder_png --output_path ./Output_image_resize --option 1 --res_p 0.5'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) > 0,"just reduce the size of the image.. it is not rocket science"

def test_image_resize_width():
    cmd = 'python3 ./simple_image_editor/image_resizer --input_path ./Input_image_folder_png --output_path ./Output_image_resize --option 2 --res_w 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) > 0,"just reduce the size of the image.. it is not rocket science"

def test_image_resize_height():
    cmd = 'python3 ./simple_image_editor/image_resizer --input_path ./Input_image_folder_png --output_path ./Output_image_resize --option 3 --res_h 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) > 0,"just reduce the size of the image.. it is not rocket science"

def test_image_crop_pixel():
    cmd = 'python3 ./simple_image_editor/image_cropper --input_path ./Input_image_folder_png --output_path ./Output_image_cropper --option 1 --crp_px 224'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) > 0,"just crop the image.. it is not rocket science"

def test_image_crop_percent():
    cmd = 'python3 ./simple_image_editor/image_cropper --input_path ./Input_image_folder_png --output_path ./Output_image_cropper --option 2 --crp_p 0.5'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) > 0,"just crop the image.... it is not rocket science"

# def test_image_crop_size_error():
#     cmd = 'python3 ./simple_image_editor/image_cropper --input_path ./Input_image_folder_png --output_path ./Output_image_cropper --option 2 --crp_p 1.5'
#     with pytest.raises(ValueError) as error:
#         value = subprocess.run(cmd,  check= True)

def test_convert_to_png():
    cmd = 'python3 simple_image_editor --input_path ./Input_image_folder_jpg --output_path ./Output_Combined --choice 1'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_convert_to_jpg():
    cmd = 'python3 simple_image_editor --input_path ./Output_Combined --output_path ./Output_Combined --choice 2'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_resize_to_80_percent():
    cmd = 'python3 simple_image_editor --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 1 --res_p 0.8'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_resize_to_500_width():
    cmd = 'python3 simple_image_editor --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 2 --res_w 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_resize_to_500_heigth():
    cmd = 'python3 simple_image_editor --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 3 --res_h 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_crop_224():
    cmd = 'python3 simple_image_editor --input_path ./Output_Combined --output_path ./Output_Combined --choice 4 --option 1 --crp_px 224'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just crop the image.. it is not rocket science"

def test_convert_to_png_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Input_image_folder_jpg --output_path ./Output_Combined --choice 1'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_convert_to_jpg_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Output_Combined --output_path ./Output_Combined --choice 2'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"format is not changing dude"

def test_resize_to_80_percent_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 1 --res_p 0.8'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_resize_to_500_width_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 2 --res_w 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_resize_to_500_heigth_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Output_Combined --output_path ./Output_Combined --choice 3 --option 3 --res_h 500'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just reduce the size of the image.. it is not rocket science"

def test_crop_224_with_zip():
    cmd = 'python3 simple_image_editor.zip --input_path ./Output_Combined --output_path ./Output_Combined --choice 4 --option 1 --crp_px 224'
    value = subprocess.run(cmd,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(value.stdout.decode('utf-8'))) == 0,"just crop the image.. it is not rocket science"

def test_doc_string():
    assert bool(converter.image_converter.__annotations__),"annotation missing"
    assert bool(converter_jpg.image_converter.__annotations__),"annotation missing"
    assert bool(resizer.image_resizer.__annotations__),"annotation missing"
    assert bool(cropper.image_cropper.__annotations__),"annotation missing"

def test_annotation():
    assert bool(converter.image_converter.__doc__),"doc string missing"
    assert bool(converter_jpg.image_converter.__doc__),"doc string missing"
    assert bool(resizer.image_resizer.__doc__),"doc string missing"
    assert bool(cropper.image_cropper.__doc__),"doc string missing"