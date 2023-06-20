#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/total-ram.py
# Started On        - Wed  7 Jun 00:11:39 BST 2023
# Last Change       - Mon 19 Jun 23:34:57 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Displays the total RAM found on the system, using the '/proc/meminfo' file.
# This starts at K, hence a null value for bytes being omitted from `Human()`.
#------------------------------------------------------------------------------

import sys

Power = 1024

def Human(Ks) -> str:
	for Unit in 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y':
		if Ks < Power:
			Out = f"{Ks:0.1f}"
			if Out[-2:] == '.0':
				Out = Out[0:-2]

			return(f"{Out}{Unit}")

		Ks /= Power

File = '/proc/meminfo'

try:
	Digits = ''
	with open(File, 'rt') as FH:
		for Line in FH:
			Field1, Field2 = Line.rstrip().split(':')[0:2]

			if Field1 == 'MemTotal':
				for Char in Field2:
					if Char.isdigit():
						Digits += Char

			break

	print(Human(int(Digits)))
except FileNotFoundError:
	print(f"Err: File '{File}' not found.", file = sys.stderr)
	exit(1)
except PermissionError:
	print(f"Err: File '{File}' inaccessible.", file = sys.stderr)
	exit(1)
