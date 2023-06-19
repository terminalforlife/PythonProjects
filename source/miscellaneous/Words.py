#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/Words.py
# Started On        - Thu 25 May 12:51:27 BST 2023
# Last Change       - Sat 10 Jun 01:15:23 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# A class for handling the system's primary dictionary, except words which
# contain apostrophes for ownership, like dog's, and except words which start
# with an uppercase letter, as in proper nouns. Obviously, this is expect words
# which are English or follow similar rules. This filtering can be disabled.
#
# Includes some demonstrations at the end, because I got a bit carried away.
#------------------------------------------------------------------------------

import random
import sys
import re

class Words():
	Words = []

	def __init__(Self, File = '/usr/share/dict/words', Filter = True):
		with open(File, 'rt') as FH:
			for Line in FH.readlines():
				Line = Line.rstrip()

				if Filter:
					if Line[-2:-1] == "'": continue
					if Line[0:1].isupper(): continue

				Self.Words.append(Line)

	# Return a random word.
	def Rand(Self) -> str:
		return(random.choice(Self.Words))

	# Return number of gathered words.
	def Count(Self) -> int:
		return(len(Self.Words))

	# Return True/False if a given word is found or not.
	def Find(Self, Word) -> bool:
		if Word in Self.Words:
			return(True)
		else:
			return(False)

	# Return True/False if a REGEX pattern matches a given word or not.
	def Match(Self, Expr: str) -> list:
		Pattern = re.compile(Expr)

		Found = []
		for Word in Self.Words:
			if Pattern.match(Word):
				Found.append(Word)

		return(Found)

WordList = Words()

Words = WordList.Match(r'^baz')
Length = len(Words)

if Length:
	print(f"REGEX '\033[93m^baz\033[0m' matched {Length} word(s):\n")

	for Index, Word in enumerate(Words):
		print(f"  \033[96m{Index + 1}\033[0m. '\033[92m{Word}\033[0m'")

	print()

print(f"Picked '\033[92m{WordList.Rand()}\033[0m' from \033[92m{WordList.Count():,}\033[0m word(s).")

if WordList.Find('duh'):
	print("Word '\033[92mduh\033[0m' was also found among them.")
