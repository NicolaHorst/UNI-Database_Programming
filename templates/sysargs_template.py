#!/usr/bin/env python3
import sys
import os

arg_1: str = "--arg1"  # only a flag
arg_2: str = "--arg2"  # arg with following value
arg_3: str = "--arg3"  # arg with following values
arg_4: str = "--arg4"  # arg with single value
file_names: str = "files"  # arg is file name
arg_5: str = "--arg5" # arg with different options
arg5_choices: list = ["choice1", "choice2", "choice3"]

file_ending1: str = ".fasta"
file_ending2: str = ".txt"

mandatory_args: dict = {arg_1: False, arg_2: "", arg_3: [], arg_4: "", file_names: [], arg_5: ""}


def usage():
    print("APP-NAME by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Mandatory arguments are: 
    \tFILE        - one or more compressed or uncompressed Uniprot data files\n
    Optional arguments are (either --help or  --seq-start must be given):
    \t--help      - display this help page
    \t--seq-start - show the first then amino acids for all or only for the given UniProt ID
    \t--get-entry - show the Uniprot entry for the given UniProt ID (not implemented) UPID - a valid UniProt ID  like AP3A_SARS2""")
    exit()


def main(args):
    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 1:
        multiple_args_index: int = 0
        if args[1] == arg_1:
            mandatory_args[arg_1] = True

        if args[2] == arg_2:
            mandatory_args[arg_2] = args[3]
        else:
            print(f"arg: {args[2]}, does not match the required arg for this position {arg_2}")

        if args[4] == arg_3:
            multiple_args_index = 4
            while True:
                multiple_args_index += 1
                # when end of args is reached
                if len(args) <= multiple_args_index:
                    break
                # when reached the next arg
                if args[multiple_args_index] in mandatory_args.keys():
                    break

                # when arg is a file or none file
                if args[multiple_args_index].endswith(file_ending1) or args[multiple_args_index].endswith(file_ending2):
                    break

                mandatory_args[arg_3].append(args[multiple_args_index])
        else:
            print(f"arg: {args[4]}, does not match the required arg for this position {arg_3}")

        if args[multiple_args_index] == arg_4:
            multiple_args_index += 1
            mandatory_args[arg_4] = args[multiple_args_index]
            multiple_args_index += 1

        # get the provided file name(s)
        while True:
            fn = args[multiple_args_index]
            if fn.endswith(file_ending1) or fn.endswith(file_ending2):
                if os.path.isfile(fn):
                    mandatory_args[file_names].append(fn)
                else:
                    print(f"file {fn} does not exist")
            else:
                print(f"file type mismatch pleas use one of the following endings {file_ending1}, {file_ending2}")
            multiple_args_index += 1
            if len(args) <= multiple_args_index:
                break
                # when reached the next arg

            if args[multiple_args_index] in mandatory_args.keys():
                break

        if args[multiple_args_index] in arg5_choices:
            mandatory_args[arg_5] = args[multiple_args_index]


if __name__ == "__main__":
    main(sys.argv)
    print(mandatory_args)
