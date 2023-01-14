#!usr/bin/env python3
# Author: Nicola Horst

import sys
import re

def wc(file_path: str):
	num_lines: int = 0
	num_words: int = 0
	num_chars: int = 0
	n_low: int = 0
	n_up: int = 0

	with open(file_path, 'r') as file:
		for line in file:
			num_lines += 1
			num_words += len(line.split(" "))
			num_chars += len(re.sub("[' ']*", "", line))
			n_low += len(re.sub("[A-Z, " "]*", "", line))
			n_up += len(re.sub("[a-z, " "]*", "",line))

	return (num_lines, num_words, num_chars, n_low, n_up) 

def usage():
	print("usage")
	file_path = "./sample_text.txt"

def main(args):
	if (len(args) < 2):
		usage()
	else:
		print("main is running")


if __name__ == "__main__":
	main(sys.argv)
	path = sys.argv[1]
	out = wc(path)
	print(out)
