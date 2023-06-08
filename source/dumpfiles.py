#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/dumpfiles.py
# Started On        - Sat  3 Jun 22:37:20 BST 2023
# Last Change       - Thu  8 Jun 16:09:05 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Using function recursion and three standard modules, dump a list of file and
# directory names, modes, UIDs, and GIDs, recursively. These can be sent to a
# file to save as a database you can restore if you mess up these values.
#
# NOTE: Won't print or recurse through symbolical links or mount points.
#
# Usage: $0 [DIR]
#------------------------------------------------------------------------------

import os
import sys
import stat

def Stat(File) -> str:
	Mode, _, _, _, UID, GID = os.stat(File)[0:6]
	Mode = oct(stat.S_IMODE(Mode))[2:]

	return(f"{Mode} {UID} {GID} {File}")

def Recurse(Dir) -> str:
	for File in os.listdir(Dir):
		File = f"{Dir}/{File}"

		if File == '.' or File == '..': continue
		if os.path.islink(File): continue
		if os.path.ismount(File): continue

		if os.path.isfile(File):
			print(Stat(File))
		elif os.path.isdir(File):
			print(Stat(File))
			Recurse(File)

if len(sys.argv) == 2:
	Recurse(sys.argv[1].rstrip('/'))
else:
	print("Err: Argument required.", file=sys.stderr)

	exit(1)
