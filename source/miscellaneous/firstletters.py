#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/firstletters.py
# Started On        - Mon 24 Jul 14:47:25 BST 2023
# Last Change       - Fri  4 Aug 14:29:26 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Output CSV of the top 10 and bottom 10 number of words beginning with the
# first letter of each word, per the words in the system's default dictionary.
# Difficult to explain, but it'll be clear when you run/read it. Doesn't take
# into account anything other than the English language, but it should work
# with most languages.
#
# Because sometimes you've just gotta know -- but, with code!
#
# Dependencies:
#
#   python (>= 3.6)
#------------------------------------------------------------------------------

import sys

File = '/usr/share/dict/words'

try:
	Words = []
	with open(File, 'rt') as FP:
		for Line in FP.readlines():
			Line = Line.rstrip()

			if Line[-2:] != "'s":
				Words.append(Line)
except FileNotFoundError:
	print(f"E: File '{File}' not found.", file = sys.stderr)
	sys.exit(1)
except PermissionError:
	print(f"E: File '{File}' inaccessible.", file = sys.stderr)
	sys.exit(1)

print('RANK,LETTER,COUNT')

Firsts = {}
for Word in Words:
	if Word[0] in Firsts:
		Firsts[Word[0]] += 1
	else:
		Firsts[Word[0]] = 1

Firsts = sorted(
	Firsts.items(),
	key = lambda X: X[1],
	reverse = True
)

# Grab first 10.
Rank = 0
for Key, Value in Firsts[:10]:
	Rank += 1

	print(f"{Rank},'{Key}',{Value}")

# Grab last 10.
Rank = len(Firsts) - Rank
for Key, Value in Firsts[-10:]:
	print(f"{Rank},{Key},{Value}")

	Rank += 1
