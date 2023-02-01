#!/usr/bin/env python3
import sys
import os
from typing import Dict, List


def file_to_dict(file_name: str) -> Dict:
    file_dict = {}
    is_first: bool = True
    key: str = ""
    seq: str = ""
    with open(file_name, "r") as reader:
        for line in reader:
            if line.startswith(">sp"):
                if is_first:
                    key = line.split(" ")[0][1:]
                    is_first = False
                else:
                    file_dict.update({key: seq})
                    key = line.split(" ")[0][1:]
                    seq = ""
            else:
                seq += line.strip('\n')

        # to also catch tha last entry
        file_dict.update({key: seq})

    return file_dict


def workload(acid: str, files: List):
    print(f"Using acid: {acid} as amino acid to search")
    print(f"using files: {files} as files to search in")

    return_values: List = []

    file_dicts: List = []
    for file_name in files:
        file_dict = file_to_dict(file_name=file_name)
        file_dicts.append(file_dict)

    for file_dict in file_dicts:
        return_values += [f"{key}:\t {acid}\t {file_dict[key].count(acid)}" for key in file_dict.keys()]

    return return_values


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

        return workload(acid=acid, files=files)


if __name__ == "__main__":
    results = main(sys.argv)
    for r in results:
        print(r)
