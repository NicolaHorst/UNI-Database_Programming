#!/usr/bin/env python3
import random


def create_colored_places(num_elements: int):
    token = "*"
    return_string = ""
    for i in range(0, num_elements):
        is_colored = random.randint(0, 4)
        if is_colored == 1:
            return_string += f"{colors.red}{token}{colors.normal}"
        else:
            return_string += f"{colors.green}{token}{colors.normal}"

    return return_string

class colors:
    red: str = "\33[91m"
    yellow: str = "\033[93m"
    green: str = "\033[92m"
    normal: str = "\033[0m"
    dark_yellow = "\33[33m"


height: int = int(input("insert the height for the xmas-tree"))
amount_s_per_line: [] = [i for i in range(1000) if i % 2 != 0]
amount_s_per_line = amount_s_per_line[:height + 1]

for i in amount_s_per_line:
    if i == 1:
        center = int(amount_s_per_line[-1] / 2) if amount_s_per_line[-1] % 2 == 0 else int(
            (amount_s_per_line[-1] + 1) / 2)

        tree_stringr = " " * ((center - int(i / 2))-1)
        tree_stringm = "*" * i
        print(tree_stringr, colors.yellow, tree_stringm, colors.normal)
    else:
        center = int(amount_s_per_line[-1] / 2) if amount_s_per_line[-1] % 2 == 0 else int((amount_s_per_line[-1] + 1) / 2)
        tree_stringr = " " * (center - int(i / 2))
        tree_stringm = create_colored_places(num_elements=i)
        tree_stringl = " " * (center - int(i / 2))

        print(tree_stringr, tree_stringm, tree_stringl)

else:
    for i in range(0, 3):
        tree_stringr = " " * ((center - int(1 / 2))-2)
        tree_stringm = "***"
        print(tree_stringr, colors.dark_yellow, tree_stringm, colors.normal)

print(f"{colors.green} test {colors.yellow} test2")
