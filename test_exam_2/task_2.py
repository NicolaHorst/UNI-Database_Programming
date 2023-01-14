#!/usr/bin/env python3
import re
import sys, os


def usage():
    print("Appname by Author, Uni Potsdam, 2020")
    print("""
    Usage: MaxYiu-FastaParser1.py [FILE] --help|--get-seq|--grep-seq|--get-n ?[PATTERN|ID]?
    Uniprot-Parser by Maxi Yiu, 2022
    Extract information from Uniprot data files.
    -------------------------------------------
    Mandatory arguments are:
        FILE - one FASTA file
    Optional arguments are (either --help, --get-n or ---get-seq or --grep-seq):
        --help      - display this help page
        --get-n     - show sequence length for the given row tabulated sequence information 
        --get-seq   - show the sequence for a given ID 
        --grep-seq  - search the sequences for a given pattern
        PATTERN     - an amino acid pattern (regular expression enabled) 
        ID          - a valid sequence ID or a part of it
    """)
    exit()


def get_n(fn):
    isFirst = True
    acids = ""
    name = ""
    with open(fn, "r") as file_reader:
        for line in file_reader:
            name = line.split(" ")[0]
            if line.startswith(">sp"):
                if isFirst:
                    isFirst = False
                    continue
                else:
                    print(f"{name}:  {len(acids)}")
                    name = ""
                    acids = ""
            else:
                acids += line

def get_seq(fn, id):
    found = False
    acid = ""
    with open(fn, "r") as file_reader:
        for line in file_reader:
            if found == True and line.startswith(">sp"):
                print(f"{name}:     {acid}")
                break
            else:
                acid += line
            if id in line:
                name = line.split(" ")[0]
                found = True


def grep_seq(id):
    pass

def functionality(file_name, arg, value):
    print(f"execute logic with {arg}, and file {file_name} and {value}" )
    if arg == "--get-n":
        get_n(file_name)
    if arg == "--get-seq":
        get_seq(file_name, value)

def main(args):
    file_name: str = ""
    value = ""
    arg_idx = 1
    used_optional: str = ""
    if len(args) <= 2 or "--help" in args:
        usage()
    elif len(args) > 1:
        for i in range(len(args)):
            if len(args) == arg_idx:
                break
            arg = args[arg_idx]
            if arg.endswith(".fasta"):
                if os.path.isfile(arg):
                    file_name = arg
                    arg_idx += 1
                else:
                    print(f"file: {arg} does not exist")
            elif arg == "--get-n":
                used_optional = "--get-n"
                arg_idx += 1
            elif arg == "--get-seq":
                used_optional = "--get-seq"
                value = args[arg_idx + 1]
                arg_idx += 2
            elif arg == "--grep-seq":
                used_optional = "--grep-seq"
                value = args[arg_idx + 1]
                arg_idx += 2
            else:
                print(f"{arg} does not exist. Did you mean one of the following:")
                arg_idx += 1

    functionality(file_name=file_name, arg=used_optional, value=value)


if __name__ == "__main__":
    main(sys.argv)