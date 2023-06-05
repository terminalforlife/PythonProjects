#!/usr/bin/env python3.6
#cito M:755 O:0 G:0 T:/usr/local/bin/inout
#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/inout.py
# Started On        - Mon  5 Jun 13:12:57 BST 2023
# Last Change       - Mon  5 Jun 14:42:21 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Simple Python script for displaying the data downloaded and uploaded in the
# current session for all network devices. Sizes are displayed in
# human-readable format (IEC), and the data is formatted as a dynamically-sized
# table.
#
# Dependencies:
#
#   python (>= 3.6)
#------------------------------------------------------------------------------

import os
import sys

File = '/proc/net/dev'

if not os.path.isfile(File):
	print(f"Err: File '{File}' not found.", file = sys.stderr)
	exit(1)
elif len(sys.argv[1:]):
	print('Err: No arguments required.', file = sys.stderr)
	exit(1)

def Human(Bytes) -> str:
	for Unit in '', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y':
		if Bytes < 1024:
			Number = f"{Bytes:0.1f}"
			if Number[-2:] == '.0':
				Number = Number[:-2]

			return(f"{Number}{Unit}")

		Bytes /= 1024

def LenChk(Str, MaxLen) -> int:
	Len = len(Str)
	if Len > MaxLen:
		return(Len)
	else:
		return(MaxLen)

Data = {}
NameLenMax = 4
DownLenMax = 4
with open(File, 'rt') as FH:
	LineNr = 0
	for Line in FH.readlines():
		Line = Line.rstrip()
		Split = Line.split()

		# Ignore header.
		if LineNr != 2:
			LineNr += 1

			continue

		Name = Split[0].rstrip(':')
		Down = Human(int(Split[1]))
		Up = Human(int(Split[9]))

		NameLenMax = LenChk(Name, NameLenMax)
		DownLenMax = LenChk(Down, DownLenMax)

		Data[Name] = (Down, Up)

print('%*s %-*s %-s' % (NameLenMax, 'NAME', DownLenMax, 'DOWN', 'UP'))

for Name in Data:
	Down, Up = Data[Name]

	print('%*s %-*s %-s' % (NameLenMax, Name, DownLenMax, Down, Up))
