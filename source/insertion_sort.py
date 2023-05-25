#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/insertion_sort.py
# Started On        - Wed 24 May 23:48:07 BST 2023
# Last Change       - Thu 25 May 22:47:48 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Insertion Sort arglorithm in Python. Unfortunately, it seems Python doesn't
# support the standard `--pos` or `pos--` syntax, which royally sucks.
#------------------------------------------------------------------------------

list = [8, 1, 7, 4, 9, 3, 6, 10, 5, 2]

for index in range(0, len(list)):
	cur = list[index]
	pos = index

	while pos > 0 and list[pos - 1] > cur:
		list[pos] = list[pos - 1]
		pos -= 1

	list[pos] = cur

print(list)
