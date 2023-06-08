#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/kernel-version.py
# Started On        - Thu  8 Jun 01:33:42 BST 2023
# Last Change       - Thu  8 Jun 01:40:14 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Get the Linux (kernel) version, using '/proc/version'.
#------------------------------------------------------------------------------

import sys

File = '/proc/version'

try:
	Version = ''
	with open(File, 'rt') as FH:
		for Line in FH.readlines():
			LinuxFound = False
			for Field in Line.split():
				if LinuxFound and Field != 'version':
					Version = Field

					break
				elif Field == 'Linux':
					LinuxFound = True
except FileNotFoundError:
	print(f"Err: {File} not found.", file = sys.stderr)
except PermissionError:
	print(f"Err: {File} inaccessible.", file = sys.stderr)

if len(Version):
	print(Version)
else:
	print('Err: Failed to acquire kernel version.', file = sys.stderr)
	exit(1)
