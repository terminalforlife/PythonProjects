#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/human-size.py
# Started On        - Tue  6 Jun 23:48:10 BST 2023
# Last Change       - Fri  9 Jun 23:49:47 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# To convert sizes to human-readable sizes. This is the same approach I take in
# other languages, but I wanted to see how it works in Python. It's actually a
# lot nicer than in Perl, if you ignore 't', 'h', 'i', 's', crap.
#------------------------------------------------------------------------------

Power = 1024

def Human(Bytes: int) -> str:
	if Bytes < Power: return(str(Bytes))
	for Unit in 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y':
		Bytes /= Power
		if Bytes < Power:
			Out = f"{Bytes:0.1f}"
			if Out[-2:] == '.0':
				Out = Out[0:-2]

			return(f"{Out}{Unit}")

print(Human(123234234))
