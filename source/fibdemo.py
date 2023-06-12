#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/fibdemo.py
# Started On        - Sun  4 Jun 01:33:53 BST 2023
# Last Change       - Mon 12 Jun 12:29:50 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# A demonstration of the obligatory Fibonacci Sequence recursive function. This
# file includes both the simple version and the more advanced version which
# uses memoization. Python 3.6 refuses to recurse beyond the 999th time, while
# Python 3.9 won't go past 995! Argh!
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

SecsBefore = int(time.perf_counter())

Fib(37)

SecsAfter = int(time.perf_counter())
print('\nTook {} second(s).\n'.format(SecsAfter - SecsBefore))

Nrs = {0: 0, 1: 1}
def Fib(Nr) -> int:
	if Nr in Nrs.keys():
		return(Nrs[Nr])

	Result = Fib(Nr - 1) + Fib(Nr - 2)
	Nrs[Nr] = Result

	return(Result)

print('Using advanced method for #995:\n')

SecsBefore = int(time.perf_counter())

print(Fib(995))

SecsAfter = int(time.perf_counter())
print('\nTook {} second(s).\n'.format(SecsAfter - SecsBefore))
