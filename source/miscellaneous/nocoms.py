#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/nocoms.py
# Started On        - Tue  1 Dec 03:04:13 GMT 2020
# Last Change       - Mon 19 Jun 23:34:57 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Experimenting with file I/O. This script will just output itself without
# comments.
#
# I would prefer to use string splicing in a loop to determine comment lines, -
# but I couldn't get it to work on only comment lines. I'll probably add
# additional approaches, in time.
#------------------------------------------------------------------------------

from re import match

# Not using `with`, so I can practice this approach, plus it's Perl-y.
FH = open(__file__, 'r')

# Print the contents of this script, without comments.
for Line in FH:
	if not match('^[\s\t]*#', Line):
		print(Line, end='')

FH.close()
