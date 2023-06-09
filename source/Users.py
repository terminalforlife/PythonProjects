#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/Users.py
# Started On        - Fri  9 Jun 18:59:56 BST 2023
# Last Change       - Fri  9 Jun 21:45:42 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# A class for handling users in *nix systems using '/etc/passwd' fields. An
# optional path can be provided with 'File' keyword when calling for the class.
# The `User()` method just lets you access the nested dictionary in an easy and
# convenient way. If no field is given to the `User()` method, the UID will be
# returned.
#
# And yes, I know I'm reinventing the wheel, but I don't care. This was highly
# educational, giving me a much better understanding of how classes work in
# Python!
#
# Usage:
#
#   import Users
#
#   Users = Users()
#   print(Get.User('root', 'Home'))
#   print(Get.UserID(0, 'GroupID'))
#
# Remember, the `File` is optional, if you need to process a different file.
#
# Caveat: This uses the username as the primary key of each user, so if you
#         have a system which weirdly has duplicate usernames, this'll probably
#         break.
#------------------------------------------------------------------------------

class Get():
	FieldNames = (
		'User', 'Password', 'UserID', 'GroupID',
		'Comment', 'Home', 'Interpreter'
	)

	Data = {}

	def __init__(Self, File = '/etc/passwd'):
		with open(File, 'rt') as FH:
			for Line in FH.readlines():
				Line = Line.rstrip().split(':')

				Pos = 0
				Name = ''
				for Field in Line:
					if Pos == 0:
						Name = Field
						Self.Data[Name] = {}
					else:
						Self.Data[Name][Self.FieldNames[Pos]] = Field

					Pos += 1

	# Return a given `Field` for the given `User`. If no `Field` is provided, -
	# the given `User`'s `UserID` is returned.
	def User(Self, User: str, Field = 'UserID') -> str:
		return(Self.Data[User][Field])

	# Return a given `Field` (required) for the user with the given `UserID`.
	def UserID(Self, UserID: int, Field: str) -> str:
		for User in Self.Data:
			if Self.Data[User]['UserID'] == str(UserID):
				if Field == 'User':
					return(User)
				else:
					return(Self.Data[User][Field])
