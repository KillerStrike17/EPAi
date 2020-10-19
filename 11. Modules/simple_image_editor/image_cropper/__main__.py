import argparse
import cropper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i','--input_path',type=str,help="Input Image Location")
    parser.add_argument('-o','--output_path',type=str,help="Output Image Location")
    parser.add_argument('--option',type=int,help="option")
    parser.add_argument('--crp_px',type=int,help="crop pixel value")
    parser.add_argument('--crp_p',type=float,help="crop percentage value")
    args = parser.parse_args()
    if args.option == 1:
        not_cropped_list = cropper.image_cropper(args.input_path,args.output_path,crp_px = args.crp_px,option = args.option)
    elif args.option == 2:
        not_cropped_list = cropper.image_cropper(args.input_path,args.output_path,crp_p = args.crp_p,option = args.option)
    # print(args)
    print(not_cropped_list)