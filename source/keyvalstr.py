#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/keyvalstr.py
# Started On        - Wed 24 May 20:55:59 BST 2023
# Last Change       - Thu 25 May 22:57:02 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Iterate over a key=value string character-by-character to fetch both the key
# and the value, separately. I'm really hating 'camelCase', but, when in Rome.
#------------------------------------------------------------------------------

string = 'key=value'

out = ''
gotSep = False
key, value = '', ''
for index in range(0, len(string)):
	char = string[index]
	if gotSep == True:
		value = value + char
	elif char == '=':
		gotSep = True

		key = out
	else:
		out = out + char

	index += 1

print(key)
print(value)
