#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/getuid.py
# Started On        - Wed 24 May 23:08:13 BST 2023
# Last Change       - Fri  4 Aug 14:35:10 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Parse '/etc/passwd' to fetch UID from the user given to the script as an
# argument. If no argument is provided, display the current user's UID.
# Essentially, id(1)'s `-u` flag.
#
# Dependencies:
#
#   python (>= 3.6)
#------------------------------------------------------------------------------

import os, sys

if len(sys.argv) == 1:
	Arg = os.environ.get('USER')
else:
	Arg = sys.argv[1]

File = '/etc/passwd'

try:
	with open(File, 'rt') as FP:
		for Line in map(str.rstrip, FP.readlines()):
			USER, _, UID = Line.split(':')[:3]

			if Arg == USER:
				print(UID)

				break
except FileNotFoundError:
	print(f"E: File '{File}' not found.", file = sys.stderr)
	sys.exit(1)
except PermissionError:
	print(f"E: File '{File}' inaccessible.", file = sys.stderr)
	sys.exit(1)
