#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/insertion_sort.py
# Started On        - Wed 24 May 23:48:07 BST 2023
# Last Change       - Sat 10 Jun 23:26:12 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Insertion Sort arglorithm in Python. Unfortunately, it seems Python doesn't
# support the standard `--pos` or `pos--` syntax, which royally sucks.
#------------------------------------------------------------------------------

List = [8, 1, 7, 4, 9, 3, 6, 10, 5, 2]

for Index, Cur in enumerate(List):
	Pos = Index

	while Pos and List[Pos - 1] > Cur:
		List[Pos] = List[Pos - 1]
		Pos -= 1

	List[Pos] = Cur

print(List)
