import argparse
from image_cropper import cropper
from image_resizer import resizer
from j2p import converter
from p2j import converter_jpg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-i','--input_path',type=str,help="Input Image Location")
    parser.add_argument('-o','--output_path',type=str,help="Output Image Location")
    parser.add_argument('--option',type=int,help="option")
    parser.add_argument('--choice',type=int,help="choice")
    parser.add_argument('--crp_px',type=int,help="crop pixel value")
    parser.add_argument('--crp_p',type=float,help="crop percentage value")
    parser.add_argument('--res_p',type=float,help="res_p value")
    parser.add_argument('--res_w',type=int,help="res_w value")
    parser.add_argument('--res_h',type=int,help="res_h value")
    args = parser.parse_args()

    if args.choice == 1:
        converter.image_converter(args.input_path,args.output_path)
    
    elif args.choice == 2:
        converter_jpg.image_converter(args.input_path,args.output_path)
    
    elif args.choice == 3:
        if args.option == 1:
            resizer.image_resizer(args.input_path,args.output_path,res_p = args.res_p,option = args.option)
        elif args.option == 2:
            resizer.image_resizer(args.input_path,args.output_path,res_w = args.res_w,option = args.option)
        elif args.option == 3:
            resizer.image_resizer(args.input_path,args.output_path,res_h = args.res_h,option = args.option)
    elif args.choice == 4:
        if args.option == 1:
            not_cropped_list = cropper.image_cropper(args.input_path,args.output_path,crp_px = args.crp_px,option = args.option)
        elif args.option == 2:
            not_cropped_list = cropper.image_cropper(args.input_path,args.output_path,crp_p = args.crp_p,option = args.option)
