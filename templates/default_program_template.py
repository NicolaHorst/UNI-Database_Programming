#!usr/bin/env python3
import sys


def usage():
    print("usage")


def main(args):
    if len(args) < 2:
        usage()
    else:
        print("main is running")


if __name__ == "__main__":
    main(sys.argv)
