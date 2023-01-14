#!usr/bin/env python3
import argparse
from typing import List

import regex as re


def wc(file_paths: List[str], lines: bool, chars: bool, words: bool) -> None:
    """
    Count Lines, Words and Characters for each file in filenames
    :param file_paths: list of filenames
    :param lines: whether lines should be counted
    :param chars: whether characters should be counted
    :param words: whether words should be counted for each file
    :return: tuples

    if all are false, meaning none was set, they will be set to True
    This means, if only paths are given, then all values will be returned
    """

    if lines == chars == words:
        lines = chars = words = True

    for file_path in file_paths:
        num_lines: int = 0
        num_words: int = 0
        num_chars: int = 0
        with open(file_path, 'r') as file:
            for line in file:
                if lines:
                    num_lines += 1
                if words:
                    num_words += len(line.split(" "))
                if chars:
                    num_chars += len(re.sub("[' ']*", "", line))

        print(f"File {file_path: <30}{f'number of lines: {num_lines: <10} ' if lines else ' '}"
              f"{f'number of words: {num_words: <10} ' if words else ' '}"
              f"{f'number of characters: {num_chars: <10} ' if chars else ' '}")


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("file_paths",
                    metavar="FP",
                    type=str,
                    nargs="+",
                    help="All files to be processed")

parser.add_argument('-l', '--lines',
                    dest="l",
                    action="store_const",
                    default=False,
                    const=True,
                    help='count the lines of all files')

parser.add_argument('-w', "--words",
                    dest="w",
                    action="store_const",
                    default=False,
                    const=True,
                    help='count the words of all files')

parser.add_argument('-c', '--characters',
                    dest="c",
                    action="store_const",
                    default=False,
                    const=True,
                    help='count the characters of all files')

parser.add_argument('-m', '--multiple',
                    dest="m",
                    nargs=1,
                    type=str,
                    help='alias for all combinations of multiple args like lw | lwc etc')


if __name__ == "__main__":
    args = parser.parse_args()  # parse arguments
    if args.m:
        l = w = c = False
        m = args.m[0]
        if re.search("[lL]", m):
            l = True
        if re.search("[wW]", m):
            w = True
        if re.search("[cC]", m):
            c = True

        wc(args.file_paths, l, c, w)
    else:
        wc(args.file_paths, args.l, args.c, args.w)
