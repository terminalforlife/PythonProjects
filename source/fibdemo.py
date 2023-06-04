#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/fibdemo.py
# Started On        - Sun  4 Jun 01:33:53 BST 2023
# Last Change       - Sun  4 Jun 02:01:21 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# A demonstration of the obligatory Fibonacci Sequence recursive function. This
# file includes both the simple version and the more advanced version. Python
# refuses to recurse beyond the 999th time.
#
# This was so much easier than in BASH!
#
# WARNING: If you have a potato, do NOT run this!
#------------------------------------------------------------------------------

import time

def Fib(Nr) -> int:
	if Nr <= 2:
		return(1)
	else:
		return(Fib(Nr - 1) + Fib(Nr - 2))

print('Using simple method for #37:\n')

SecsBefore = int(time.time())

Fib(37)

SecsAfter = int(time.time())
print('\nTook {} second(s).\n'.format(SecsAfter - SecsBefore))

Nrs = {0: 0, 1: 1}
def Fib(Nr) -> int:
	if Nr in Nrs.keys():
		return(Nrs[Nr])

	Result = Fib(Nr - 1) + Fib(Nr - 2)
	Nrs[Nr] = Result

	return(Result)

print('Using advanced method for #999:\n')

SecsBefore = int(time.time())

print(Fib(999))

SecsAfter = int(time.time())
print('\nTook {} second(s).\n'.format(SecsAfter - SecsBefore))
