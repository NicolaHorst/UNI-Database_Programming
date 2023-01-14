#!/usr/bin/env python3
#Author: Nicola Horst

import random

class colors:
	red: str = "\033[31m"
	green: str = "\033[32m"
	normal: str = "\033[0m"

operators = {
	"a" : "+",
	"s" : "-",
	"d" : "/",
	"m" : "*",
}

def calc(operator):
	while(True):
		num_1 = random.randint(1, 20)
		num_2 = random.randint(1, 20)
		
		result = input(f"what is {num_1} {operator} {num_2}:	")
		correct_result = eval(f"{num_1}{operator}{num_2}")
		try:
			result = float(result)
			
			if (result == correct_result):
				print(colors.green, "thats correct", colors.normal)
				
			else:
				print(colors.red, f"the correct answer would be {correct_result}", colors.normal)
		except:
			if (result == 'q'):
				break
			else:
				print(f"{result} is not a number")
				


def menue():
	print("menue:")
	print("a: add \n m: multiply \n s: subtract \n d: divide \n q: quit")
	
	while(True):
		operator = input("pelase input operator: ")
		if (operator in operators.keys()):
			calc(operators[operator])
		elif (operator == 'q'):
			break
		
		else:
			print("not a valid operator")


if __name__ == "__main__":
	menue()
