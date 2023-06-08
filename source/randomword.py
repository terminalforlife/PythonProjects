#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/randomword.py
# Started On        - Thu 25 May 12:51:27 BST 2023
# Last Change       - Thu  8 Jun 16:22:07 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Print a random word from the system's (British English) dictionary, except
# words which contain apostrophes for ownership, like dog's, and except words
# which start with an uppercase letter, as in proper nouns.
#
# Includes my usual `Err()` function.
#------------------------------------------------------------------------------

from random import choice
from sys import stderr

def err(status, msg):
	print('Err: {}'.format(msg), file=stderr)
	if status > 0: exit(status)

file = '/usr/share/dict/british-english'

words = []

try:
	with open(file, 'rt') as fh:
		for line in fh.readlines():
			line = line.rstrip()
			if line[-2:-1] != "'" and line[0:1] != line[0:1].upper():
				words.append(line)
except FileNotFoundError:
	err(1, "File '{}' not found.".format(file))
except PermissionError:
	err(1, "File '{}' inaccessible.".format(file))

# Both approaches work, but the latter is far more appropriate.
#print(words[randint(0, len(words) - 1)])
print(choice(words))
