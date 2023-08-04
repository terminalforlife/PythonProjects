#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/edit-file.py
# Started On        - Wed  7 Jun 13:31:38 BST 2023
# Last Change       - Fri  4 Aug 14:29:21 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Automate the edit of a file. Note that truncating the file immediately makes
# that change to the file itself, not just some sort of buffer.
#
# This script will remove the Cito line from '~/.bashrc', if the string '#cito'
# is found at the start of line 2. A backup ('~/.bashrc.bak') will be made
# before any changes are written.
#------------------------------------------------------------------------------

import os
import shutil

Home = os.environ['HOME']
File =  Home + '/.bashrc'
Pretty = File.replace(Home, '~', 1)

if not os.path.isfile(File + '.bak'):
	shutil.copy(File, File + '.bak')

try:
	with open(File, 'r+') as FH:
		Data = []
		LineNr = 0
		for Line in FH.readlines():
			Line = Line.rstrip()
			LineNr += 1

			try:
				if LineNr == 2 and Line.split()[0] == '#cito':
					Line = ''
			except IndexError:
				pass

			Data.append(Line)

		FH.seek(0)
		FH.truncate()

		print("\n".join(Data), file = FH)
except FileNotFoundError:
	sys.exit(1)
except PermissionError:
	sys.exit(1)
