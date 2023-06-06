#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Started On        - Tue  6 Jun 23:36:54 BST 2023
# Last Change       - Tue  6 Jun 23:42:49 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Violently disgust your coworkers with unnecessary rainbows.
#------------------------------------------------------------------------------

import os
import sys
import random

File = sys.argv[1]

Colors = (
	"\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m",
	"\033[37m", "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m",
	"\033[96m", "\033[97m"
)

Styles = ("\033[0m", "\033[1m", "\033[2m", "\033[3m")

try:
	with open(File, 'rt', encoding = 'utf-8') as FH:
		for Line in FH:
			Line = Line.rstrip()

			for _, Char in enumerate(Line):
				RandColorIndex = random.randint(0, len(Colors) - 1)
				RandStyleIndex = random.randint(0, len(Styles) - 1)
				RandColor = Colors[RandColorIndex]
				RandStyle = Colors[RandStyleIndex]

				print(f"{RandStyle}{RandColor}{Char}\033[0m", end = '')

			print()
except FileNotFoundError:
	print(f"Err: File '{File}' not found.", file = os.stderr)
except PermissionError:
	print(f"Err: File '{File}' inaccessible.", file = os.stderr)
	exit(1)
