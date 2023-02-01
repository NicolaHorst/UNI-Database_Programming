#!/usr/bin/env python3
import sys
import os
from typing import Dict, List


def workload(acid: str, files: List):
    print(f"Using acid: {acid} as amino acid to search")
    print(f"using files: {files} as files to search in")
    print(f"all fine :)")


def usage():
    print("nh_task1 by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Usage: nh_task1.py [-h] [LETTER FILE] ?[FILE ...]?
    Fasta-Parser by Nicola Horst, 2023
    Extract information from FASTA data files.
    -------------------------------------------
    Mandatory arguments are:
        LETTER      - Aminoacid letter
        FILE        - or more FASTA files
    Optional arguments are (either --help, -h):
        --help      - display this help page
    """)
    exit()


def main(args):
    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 1:
        acid: str = args[1]
        if len(acid) != 1:
            print(f"WARN:   given acid {acid} is too long and will be cut to {acid[:1]}")
            acid = acid[:1]
        if acid.islower():
            print(f"WARN:   given acid {acid} is lowercase and will be used as upper case: {acid.upper()}")
            acid = acid.upper()

        files: List = []
        idx: int = 2
        while True:
            if len(args) <= idx:
                break
            else:
                file_name: str = args[idx]
                idx += 1
                if os.path.isfile(file_name):
                    files.append(file_name)
                else:
                    print(f"WARN:   {file_name} is not a valid file name")

        if len(files) < 1:
            print("WARN:    No files were provided please provide at least one valid filename")

        workload(acid=acid, files=files)


if __name__ == "__main__":
    main(sys.argv)
