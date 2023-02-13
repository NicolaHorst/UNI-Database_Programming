#!/usr/bin/env python3
import sys
import os
from typing import Dict, List


def workload(arguments: Dict):
    print(f"All Fine")
    print(f"using {arguments} for workload")


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
    # Definition of different argument types
    arg_1: str = "--arg1"  # Only a flag
    arg_2: str = "--arg2"  # Choice
    arg_3: str = "--arg3"  # List of args
    mandatory_args: dict = {arg_1: "", arg_2: "", arg_3: []}

    min_args: int = len(mandatory_args.keys())

    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 3:
        choices_a1: List = [arg_1]
        if args[1] in choices_a1:
            mandatory_args[arg_1] = args[1]
        else:
            print(f"Error:\t{args[1]} is invalid expected one of the following {choices_a1}")
            exit()

        choices_a2: List = [arg_2]
        if args[2] in choices_a2:
            mandatory_args[arg_2] = args[2]
        else:
            print(f"Error:\t{args[2]} is invalid expected one of the following {choices_a2}")
            exit()

        start_index: int = 3
        for fn in args[start_index:]:
            if os.path.isfile(fn):
                pass
                if fn.endswith(".dat") or fn.endswith(".dat.gz"):
                    mandatory_args[arg_3].append(fn)
                else:
                    print(f"Info:\tfile: {fn} is wrong filetype")
            else:
                print(f"Info:\tfile: {fn} does not exist")

        if not mandatory_args[arg_3]:
            print("Error:\tNo matching file names were provided")
            exit()

        workload(arguments=mandatory_args)
    else:
        print(f"Error:\tNot enough arguments were given expected at least {min_args} arguments but {len(args) - 1} were given\n")
        usage()


if __name__ == "__main__":
    main(sys.argv)
