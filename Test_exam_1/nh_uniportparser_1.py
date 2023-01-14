#!/usr/bin/env python3
import sys, os
import re

def usage():
    print("Appname by Author, Uni Potsdam, 2020")
    print("""
    Mandatory arguments are: 
    \tFILE        - one or more compressed or uncompressed Uniprot data files\n
    Optional arguments are (either --help or  --seq-start must be given):
    \t--help      - display this help page
    \t--seq-start - show the first then amino acids for all or only for the given UniProt ID
    \t--get-entry - show the Uniprot entry for the given UniProt ID (not implemented) UPID - a valid UniProt ID  like AP3A_SARS2""")
    exit()


def main(args):
    if len(args) == 1 or "-h" in args:
        usage()
    elif len(args) > 1 and "--seq-start" in args or "--seq-start" in args or "--get-entry" in args:
        file_names = list()
        up_id = ""
        if "--seq-start" in args:
            idx = args.index("--seq-start")

            while True:
                if len(args) > idx + 1:
                    if args[idx + 1] == "--get-entry":
                        break
                    else:
                        arg_n = args[idx + 1]
                        if arg_n.endswith(".dat") or arg_n.endswith(".dat.gz"):
                            if os.path.isfile(arg_n):
                                file_names.append(args[idx + 1])
                            else:
                                print(f"{arg_n} is not an existing file")
                        else:
                            print(f"{arg_n} is not a valid filename or UPID must end with .dat.gz or .dat")
                else:
                    break
                idx += 1

        if "--get-entry" in args:
            idx_entry = args.index("--get-entry") + 1
            if args[idx_entry].isupper() and re.match(r'([^\W ^(a-z])+', args[idx_entry]):
                up_id = args[idx_entry]
            else:
                print(f"{args[idx_entry]} is not a valid id")

        print(file_names)
        print(up_id)

    else:
        print("Warning: none of the given arguments matched the required arguments")
        usage()


if __name__ == "__main__":
    main(sys.argv)
    print(sys.argv)
