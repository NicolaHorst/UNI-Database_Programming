#!/usr/bin/env python3
import random

rand_number: int  = random.randint(0, 1000)
n: int = 0
print('Hello dear gueess game player')
print('enter q to exit the game')

while(True):
	num: str = input('please insert a number:	')
	try:
		num: int  = int(num)
		if (num == rand_number):
			print(f"\033[32m you win after taking {n} turns  \033[0m")
			break
		elif (num > rand_number):
			print("\033[31m your guess is too high \033[0m")
		else:
			print("\033[31m your guess is too low\033[0m")
	except ValueError:
		if num == "q":
			break
		else:
			print(f"{num} is not a valid number")
			
	n += 1
