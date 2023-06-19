#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/insertion_sort.py
# Started On        - Wed 24 May 23:48:07 BST 2023
# Last Change       - Mon 19 Jun 23:34:57 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Insertion Sort algorithm in Python. Unfortunately, it seems Python doesn't
# support the standard `--pos` or `pos--` syntax, which royally sucks. Python
# uses Timsort, named after Tim Peters who wrote an ingenious mix of merge sort
# and insertion sort in 2002.
#------------------------------------------------------------------------------

List = [8, 1, 7, 4, 9, 3, 6, 10, 5, 2]

for Index, Cur in enumerate(List):
	Pos = Index

	while Pos and List[Pos - 1] > Cur:
		List[Pos] = List[Pos - 1]
		Pos -= 1

	List[Pos] = Cur

print(List)
