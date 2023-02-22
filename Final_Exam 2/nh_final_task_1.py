#!/usr/bin/env python3

import sys
import os
from typing import Dict, List
import re


def workload(arguments: Dict):
    print(f"All Fine")
    print(f"using {arguments} for workload")


def usage():
    print("Final Exam Task C by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Usage: nh_final_task_1.py --help| --species | --entry [FILE] ?[ID]
        Mandatory arguments are: 
    \tFILE        - one or more compressed or uncompressed Uniprot data files\n
    Optional arguments are (either --help or  --seq-start must be given):
    \t--help        - display this help page
    \t--species     - show all species with data in the file
    \t--entry       - show a protein id entry
    
    \tID            - an optional uniprot ID
    """)
    exit()


def main(args):
    # Definition of different argument types
    arg_1: str = "--arg1"  # Only a flag
    uniport_id = ""
    mandatory_args: dict = {arg_1: "", "up_id": "", "files": []}

    min_args: int = len(mandatory_args.keys())

    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) >= 3:
        choices_a1: List = ["--entry", "--species"]
        if args[1] in choices_a1:
            mandatory_args[arg_1] = args[1]
        else:
            print(f"Error:\t{args[1]} is invalid expected one of the following {choices_a1}")
            exit()

        start_index: int = 2
        for fn in args[start_index:]:
            if os.path.isfile(fn):
                pass
                if fn.endswith(".dat") or fn.endswith(".dat.gz"):
                    mandatory_args["files"].append(fn)
                else:
                    print(f"Info:\tfile: {fn} is wrong filetype")
            else:
                if fn.isupper() and re.match(r'([^\W ^(a-z])+', fn):
                    if fn == args[-1]:
                        mandatory_args["up_id"] = fn
                    else:
                        print(f"Info:\t{fn} is not a valid ID or non existing file name")

        if not mandatory_args["files"]:
            print("Error:\tNo matching file names were provided")
            exit()

        workload(arguments=mandatory_args)
    else:
        print(f"Error:\tNot enough arguments were given expected at least {min_args} arguments but {len(args) - 1} were given\n")
        usage()


if __name__ == "__main__":
    main(sys.argv)
