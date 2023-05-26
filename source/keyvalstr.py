#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/keyvalstr.py
# Started On        - Wed 24 May 20:55:59 BST 2023
# Last Change       - Fri 26 May 16:25:39 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Iterate over a key=value string character-by-character to fetch both the key
# and the value, separately. I'm really hating 'camelCase', but, when in Rome.
#
# Using Python features, I'd probably write:
#
#   key, value = (string.split('='))
#
# Although that's not as robust. The below allows for '=' in the value.
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

print(key)
print(value)
