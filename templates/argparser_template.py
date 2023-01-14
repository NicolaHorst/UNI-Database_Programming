#!usr/bin/env python3
import argparse


def default_processor(_args):
    print("USED DEFAULT SETTINGS")
    print(f"input file path: {_args.input_file}")
    print(f"output file path: {_args.output_file}")


def const_processor(_args):
    print("USED CONST SETTINGS")
    print(f"input file path: {args.input_file}")
    print(f"output file path: {args.output_file}")


parser = argparse.ArgumentParser(description='Process some integers.')

# this is a positional argument stored in args.integers
parser.add_argument('--input',
                    dest="input_file",
                    type=str,
                    nargs='+',
                    help='the directory of an input file')

parser.add_argument('--output',
                    dest="output_file",
                    type=str,
                    nargs='+',
                    help='directory of output file')


parser.add_argument('-d',
                    dest="processor",
                    action="store_const",
                    default=default_processor,
                    const=const_processor,
                    help='sample default setting')

if __name__ == "__main__":
    args = parser.parse_args()  # parse arguments
    args.processor(args)
