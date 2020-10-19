import argparse
import resizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i','--input_path',type=str,help="Input Image Location")
    parser.add_argument('-o','--output_path',type=str,help="Output Image Location")
    parser.add_argument('--option',type=int,help="option")
    parser.add_argument('--res_p',type=float,help="res_p value")
    parser.add_argument('--res_w',type=int,help="res_w value")
    parser.add_argument('--res_h',type=int,help="res_h value")
    args = parser.parse_args()
    if args.option == 1:
        resizer.image_resizer(args.input_path,args.output_path,res_p = args.res_p,option = args.option)
    elif args.option == 2:
        resizer.image_resizer(args.input_path,args.output_path,res_w = args.res_w,option = args.option)
    elif args.option == 3:
        resizer.image_resizer(args.input_path,args.output_path,res_h = args.res_h,option = args.option)
    print(args)