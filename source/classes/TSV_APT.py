#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/classes/TSV_APT.py
# Started On        - Tue 20 Jun 01:20:22 BST 2023
# Last Change       - Tue 20 Jun 17:56:17 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Send TSV data of installed packages to STDOUT.
#
# Example:
#
#   Data = StatusFile()
#
#   print(Data.Header())
#   for Package in Data.Packages:
#   	Out = Package
#   	for Key in Data.Get(Package):
#   		Out = f'{Out}\t{Data.Get(Package, Key)}'
#
#   	print(Out)
#
# Features:
#
# N/A
#
# Bugs:
#
# N/A
#
# Dependencies:
#
#   python (>= 3.6)
#------------------------------------------------------------------------------

import sys

def Err(Status, Message):
	print(f"Err: {Message}", file = sys.stderr)
	if Status > 0: exit(Status)

class StatusFile:
	def __init__(Self, File: str = '/var/lib/dpkg/status'):
		try:
			Lines = []
			with open(File, 'rt') as FH:
				Lines = FH.readlines()
		except FileNotFoundError:
			Err(1, "File '{File}' not found.")
		except PermissionError:
			Err(1, "File '{File}' inaccessible.")

		Self.Packages = {}

		Self.Keys = (
			'priority', 'section', 'installed-size', 'maintainer', 'arch',
			'multi-arch', 'source', 'version', 'depends', 'homepage'
		)

		for Line in Lines:
			Line = Line.rstrip()

			if Line[0:7] == 'Status:' and Line[8:] == 'install ok installed':
				Installed = True
			elif Line[0:8] == 'Package:':
				Package = Line[9:]
			elif Line[0:9] == 'Priority:':
				Priority = Line[10:]
			elif Line[0:8] == 'Section:':
				Section = Line[9:]
			elif Line[0:15] == 'Installed-Size:':
				Bytes = int(Line[16:]) * 1024 # <-- Back to bytes.
			elif Line[0:11] == 'Maintainer:':
				Maintainer = Line[12:]
			elif Line[0:13] == 'Architecture:':
				Arch = Line[14:]
			elif Line[0:11] == 'Multi-Arch:':
				MultiArch = Line[12:]
			elif Line[0:7] == 'Source:':
				Source = Line[8:]
			elif Line[0:8] == 'Version:':
				Version = Line[9:]
			elif Line[0:8] == 'Depends:':
				Depends = Line[9:]
			elif Line[0:9] == 'Homepage:':
				Homepage = Line[10:]
			elif len(Line) == 0:
				if Installed:
					Self.Packages[Package] = {
						'priority': Priority,
						'section': Section,
						'installed-size': Bytes,
						'maintainer': Maintainer,
						'arch': Arch,
						'multi-arch': MultiArch,
						'source': Source,
						'version': Version,
						'depends': Depends,
						'homepage': Homepage,
					}

	def Get(Self, Package: str, Key: str = None) -> str:
		if Key is None:
			return(Self.Packages[Package])
		else:
			return(Self.Packages[Package][Key])

	def Header(Self) -> str:
		Out = 'PACKAGE'
		for Index, Key in enumerate(Self.Keys):
			Out = f'{Out}\t{Key.upper()}'

		return(Out)
