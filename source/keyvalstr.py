#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/keyvalstr.py
# Started On        - Wed 24 May 20:55:59 BST 2023
# Last Change       - Fri  9 Jun 23:57:59 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Iterate over a key=value string character-by-character to fetch both the key
# and the value, separately. Also included a more 'pythonic' approach.
#------------------------------------------------------------------------------

def CharIter(String: str) -> tuple:
	SepFound = False
	Buffer, Char, Value = '', '', ''
	for Char in String:
		if SepFound == True:
			Value = f"{Value}{Char}"
		elif Char == '=':
			SepFound = True

			Key = Buffer
		else:
			Buffer = f"{Buffer}{Char}"

	return((Key, Value))

Key, Value = CharIter('Foo=Bar')
print(f"The value for '{Key}' is '{Value}'.")

# To satisfy my need for better code.
Key, Value = 'Foo=Bar'.split('=', 1)
print(f"The value for '{Key}' is '{Value}'.")
