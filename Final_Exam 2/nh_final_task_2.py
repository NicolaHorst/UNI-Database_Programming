#!/usr/bin/env python3

import sys
import os
from typing import Dict, List
import re
import gzip


class UniprotReader:
    def __init__(self):
        pass

    def uniprot_file_to_dict(self, file_name: str, filter_on=None) -> Dict:
        """
        Extract all information from uniprot files
        :param file_name: a file name of a uniprod file
        :param filter_on: a list of elements to be extracted ["AC", "OS", "OC", "OX", "RX", "DR"]
        :return: a dictionary containing all information requested from the uniprot files
        """
        filter_on = ["AC", "OS", "OC", "OX", "RX", "DR"] if filter_on is None else filter_on
        file_dict: Dict = {}

        # some flags
        is_binary: bool = True if file_name.endswith(".dat.gz") else False

        # store current used id
        _id = ""

        # open the file in binary or normal mode
        if is_binary:
            file = gzip.open(file_name, "rb")
        else:
            file = open(file_name, "r")

        for line in file:
            # some preprocessing for binary strings
            line = line.decode() if is_binary else line

            if re.match("^ID", line):
                _id = line.split("   ")[1]
                file_dict.update({_id: {target: [] for target in filter_on}})
            else:
                line_start = line[:2]  # take first two characters from string
                if line_start in filter_on:
                    file_dict[_id][line_start].append(line[5:].strip("\n"))

        return file_dict

    def get_species(self, file_names: List):
        file_dicts = []
        for file_name in file_names:
            file_dicts.append(self.uniprot_file_to_dict(file_name=file_name, filter_on=["OS"]))

        return file_dicts

    def get_entry(self, file_name: str, id: str):
        seq: List = []
        is_binary: bool = True if file_name.endswith(".dat.gz") else False
        found_id = False
        if is_binary:
            file = gzip.open(file_name, "rb")
        else:
            file = open(file_name, "r")

        for line in file:
            # some preprocessing for binary strings
            line = line.decode() if is_binary else line

            if re.match("^ID", line):
                _id = line.split("   ")[1]
                if _id == id:
                    seq.append(line)
                    found_id = True
            elif line.startswith("//"):
                found_id = False
                continue

            elif found_id:
                seq.append(line)
        file.close()

        return seq
def workload(arguments: Dict):
    results = {}
    if arguments["--arg1"] == "--species":
        reader = UniprotReader()

        if arguments["up_id"] == "":
            for result in reader.get_species(file_names=arguments["files"]):
                for key in result.keys():
                        results.update({key.split("_")[1]: result[key]["OS"][0].split("(")[0]})
        else:
            for result in reader.get_species(file_names=arguments["files"]):
                for key in result.keys():
                    if key == arguments["up_id"]:
                        results.update({key.split("_")[1]: result[key]["OS"][0].split("(")[0]})
        return results
    else:
        print("Not Implemented Yet")


def usage():
    print("Final Exam Task B by Nicola Horst, Uni Potsdam, 2023")
    print("""
    Usage: nh_final_task_2.py --help| --species | --entry [FILE] ?[ID]
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

        return workload(arguments=mandatory_args)
    else:
        print(
            f"Error:\tNot enough arguments were given expected at least {min_args} arguments but {len(args) - 1} were given\n")
        usage()


if __name__ == "__main__":
    results = main(sys.argv)

    for key in results.keys():
        print(f"{key}: \t{results[key]}")
