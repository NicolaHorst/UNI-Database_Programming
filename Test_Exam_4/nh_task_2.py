#!/usr/bin/env python3
from typing import Dict

import sys
import os
import gzip

# Definition of different argument types
arg_1: str = "--arg1"  # only a flag
file_names: str = "files"  # arg is file name
file_ending1: str = ".dat"
file_ending2: str = ".dat.gz"


class UniProtParser:
    def __init__(self):
        pass

    def uniprot_file_to_dict(self, file_name: str, bos: str = "ID", filter_on=None) -> Dict:
        filter_on = ["SQ", "AC", "OS", "OC", "OX", "RX"] if filter_on is None else filter_on
        file_dict: Dict = {}

        is_first: bool = True
        id: str = ""
        content: Dict = {key: [] for key in filter_on}
        is_binary: bool = False

        if file_name.endswith(".dat.gz"):
            file = gzip.open(file_name, "rb")
            is_binary = True
        else:
            file = open(file_name, "r")

        for line in file:
            line = line.decode() if is_binary else line
            if line.startswith(bos):
                if is_first:
                    id = line.split("   ")[1]
                    is_first = False
                else:
                    file_dict.update({id: content})
                    content: Dict = {key: [] for key in filter_on}
                    id = line.split("   ")[1]
            else:
                line_start: str = line[:2]
                if line_start in filter_on:
                    content[line_start].append(line[5:].strip("\n"))

        # to catch the last entry
        file_dict.update({id: content})
        file.close()
        return file_dict

    def extract_go_ids(self, file_names):
        file_dicts = []
        return_strings = []

        for file_name in file_names:
            file_dicts.append(self.uniprot_file_to_dict(file_name=file_name, bos="ID", filter_on=["DR"]))

        for file_dicts in file_dicts:
            for key in file_dicts.keys():
                sub_strings = []
                if file_dicts[key] == []:
                    return_strings.append(f"{key}\t NA")

                for go_id in file_dicts[key]["DR"]:
                    if "GO:" in go_id:
                        sub_strings.append(f"{key}\t {go_id[4:14]}")

                if len(sub_strings) == 0:
                    return_strings.append(f"{key}\t NA")
                else:
                    return_strings += sub_strings

        return return_strings

    def extract_kegg_ids(self, file_names):
        pass


def workload(arguments: Dict):
    print(f"Working  with args: {arguments}")
    uniprot_parse = UniProtParser()

    if arguments[arg_1] == "--go":
        return uniprot_parse.extract_go_ids(arguments[file_names])

    else:
        print(f"Usage for {arguments[arg_1]} is not implemented yet")


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

    Example usage: nh_task_1.py --go uniprot-corona-virus-data-2022-02.dat
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
                print(
                    f"Warning: file type mismatch pleas use one of the following endings {file_ending1}, {file_ending2}")

            multiple_args_index += 1

            if len(args) <= multiple_args_index:
                break

            if args[multiple_args_index] in mandatory_args.keys():
                break

        if not mandatory_args[file_names]:
            print("Warning: No working files provided")
            usage()

        return workload(mandatory_args)


if __name__ == "__main__":
    results = main(sys.argv)
    if results:
        for r in results:
            print(r)

