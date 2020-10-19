import argparse
import converter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i','--input_path',type=str,help="Input Image Location")
    parser.add_argument('-o','--output_path',type=str,help="Output Image Location")
    args = parser.parse_args()
    converter.image_converter(args.input_path,args.output_path)