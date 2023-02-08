#!/usr/bin/env python3
import sys
import os
from typing import Dict

# Definition of different argument types
arg_1: str = "--arg1"  # only a flag
file_names: str = "files"  # arg is file name
file_ending1: str = ".dat"
file_ending2: str = ".dat.gz"
def workload(arguments: Dict):
    print(f"Working  with args: {arguments}")
    print(f"everything is fine")


def usage():
    print("APP-NAME by Nicola Horst, Uni Potsdam, 2023")
    print("""
    $ python3 nh_task_1.py
    Usage: nh_task_1.py --help|--go|--doi [FILE] ?[FILE] ...?
    Uniprot-Parser by Nicola Horst, 2023
    Extract information from Uniprot data files.
    -------------------------------------------
    Optional arguments are:
        --help - display this help page
        --go   - show a protein id to GO id mapping
        --doi  - show a protein id to DOI mapping (not used today)
    Mandatory arguments are:
    FILE - one or more compressed or uncompressed Uniprot data files
    
    Example usage: nh_task_1.py --doi uniprot-corona-virus-data-2022-02.dat
    """)
    exit()


def main(args):
    mandatory_args: dict = {arg_1: "", file_names: []}

    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 1:
        multiple_args_index: int = 0
        if args[1] in ["--doi", "--go"]:
            mandatory_args[arg_1] = args[1]
        else:
            usage()

        multiple_args_index = 2
        # get the provided file name(s)
        while True:
            fn = args[multiple_args_index]
            if fn.endswith(file_ending1) or fn.endswith(file_ending2):
                if os.path.isfile(fn):
                    mandatory_args[file_names].append(fn)
                else:
                    print(f"Warning: file {fn} does not exist and is skipped")
            else:
                print(f"Warning: file type mismatch pleas use one of the following endings {file_ending1}, {file_ending2}")

            multiple_args_index += 1

            if len(args) <= multiple_args_index:
                break

            if args[multiple_args_index] in mandatory_args.keys():
                break

        if not mandatory_args[file_names]:
            print("Warning: No working files provided")
            usage()

        workload(mandatory_args)


if __name__ == "__main__":
    main(sys.argv)
