#!/usr/bin/env python3
import sys, os


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
    if len(args) == 1 or "-h" or "--help" in args:
        usage()
    elif len(args) > 1 and "default arg" in args:
        # do anything
        pass


if __name__ == "__main__":
    main(sys.argv)
