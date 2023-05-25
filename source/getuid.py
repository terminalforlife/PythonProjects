#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/getuid.py
# Started On        - Wed 24 May 23:08:13 BST 2023
# Last Change       - Thu 25 May 23:02:21 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Manually parse '/etc/passwd' character-by-character to fetch UID from the
# user given to the script as an argument. If no argument is provided, display
# the current user's UID. Essentially, `id -u [USER]`.
#
# The character-by-character approach is probaly pointless here, but it was
# good experience in getting used to Python, without resorting to methods and
# functions I don't know yet.
#------------------------------------------------------------------------------

from sys import argv, stderr
from os import environ

if len(argv) == 1:
	userArg = environ['USER']
else:
	userArg = argv[1]

file = '/etc/passwd'

try:
	fh = open(file, 'rt')

	for line in fh:
		line = line.rstrip()

		sepCount = 0
		out, user = '', ''
		for index in range(0, len(line)):
			char =  line[index]
			if char == ':':
				sepCount += 1
			elif sepCount == 1:
				user = out
				out = ''
			elif sepCount == 3:
				if user == userArg:
					print(out)

					break

				out = ''
			else:
				out = out + char

	fh.close()
except FileNotFoundError:
	print("Err: File '{}' not found.".format(file), file=stderr)
	exit(1)
except PermissionError:
	print("Err: File '{}' inaccessible.".format(file), file=stderr)
	exit(1)
