#!/usr/bin/env python3
import sys
import os

arg_1: str = "mode"
m_args1 = ["--get-n", "--get-seq", "--grep-seq"]
file_names: str = "files"
arg_2: str = "ID"

file_ending1: str = ".fasta"
file_ending2: str = ".txt"

mandatory_args: dict = {arg_1: "", file_names: [], arg_2: None}


def workload():
    print("Start workload with following config:")
    print(mandatory_args)


def usage():
    print("APP-NAME by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Usage: nh_task1-py --help|--get-seq|--grep-seq|--get-n [FILE]? [PATTERN|ID]?
    Uniprot-Parser by Nicola Horst, 2022
    Extract information from Uniprot data files.
    -------------------------------------------
    Mandatory arguments are:
        FILE - one FASTA file
    Optional arguments are (either --help, --get-n or ---get-seq or --grep-seq):
        --help      - display this help page
        --get-n     - show aequence length for the givenow tabulated sequence information 
        --get-seq   - show the sequence for a given ID 
        --grep-seq  - search the sequences for a given pattern
        PATTERN     - an amino acid pattern (regular expression enabled) 
        ID          - a valid sequence ID or a part of it""")
    exit()


def main(args):
    # Show usage when no arg is given or when help is used
    if len(args) == 1 or "-h" in args or "--help" in args:
        usage()
    # otherwise use logic
    elif len(args) > 1:
        if args[1] in m_args1:
            mandatory_args[arg_1] = args[1]
        else:
            print(f"{args[1]} not valid please use one ot the following {m_args1}")

        fn = args[2]
        if fn.endswith(file_ending1) or fn.endswith(file_ending2):
            if os.path.isfile(fn):
                mandatory_args[file_names].append(fn)
            else:
                print(f"file {fn} does not exist")
        else:
            print(f"file type mismatch pleas use one of the following endings {file_ending1}, {file_ending2}")

        if len(args) == 4:
            mandatory_args[arg_2] = args[3]

        workload()


if __name__ == "__main__":
    main(sys.argv)
