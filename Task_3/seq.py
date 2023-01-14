#!usr/bin/env python3


def seq(fr=0, to=0, by=1):
	return tuple(i for i in range(fr, to+1, 2))

sequence = seq(1, 10, 2)
print(sequence)

