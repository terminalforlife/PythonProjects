#!/usr/bin/env bash

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/nemo-scripts/new-dir-date/install.sh
# Started On        - Fri 23 Jun 12:30:19 BST 2023
# Last Change       - Fri 23 Jun 15:58:13 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Installer, mainly targetting Linux Mint, but will do the basics in pretty
# much anything Linux. You may need to adjust the shebang if you're not on a
# version of Linux Mint which is handled here.
#------------------------------------------------------------------------------

Repo='https://github.com/terminalforlife/PythonProjects'
URL="$Repo/raw/master/source/nemo-scripts/new-dir-date/new-dir-date"
Dir="$HOME/.local/share/nemo/scripts"
TargetFile='New Directory with Date'

if ! [[ -d $Dir ]]; then
	mkdir -p "$Dir"
elif (( UID == 0 )); then
	printf "Err: Administrative privileges not required.\n" 1>&2
	exit 1
fi

if type -P wget &> /dev/null; then
	Get='wget -qO '
elif type -P curl &> /dev/null; then
	Get='curl -so '
else
	printf "Err: Neither Wget nor cURL found.\n" 1>&2
	exit 1
fi

if $Get "$Dir/$TargetFile" "$URL"; then
	chmod u+x "$Dir/$TargetFile"
else
	printf "Err: Unable to download data.\n" 1>&2
	exit 1
fi

OS_File='/etc/os-release'
if [[ -f $OS_File ]]; then
	while IFS='=' read Key Value; do
		if [[ $Key == NAME ]]; then
			Name=${Value//\"}
		elif [[ $Key == VERSION_ID ]]; then
			LM_Version=${Value//\"}
		fi
	done < "$OS_File"
else
	printf 'Err: Automatic handling of shebang unavailable.\n' 1>&2
	exit 1
fi

if [[ $Name == Linux\ Mint ]]; then
	case $LM_Version in
		21|21.*)
			sed -i '1s/python/python3.10/' "$Dir/$TargetFile"
			printf 'Python 3.10 set in shebang.\n' ;;
		20|20.*)
			sed -i '1s/python/python3.8/' "$Dir/$TargetFile"
			printf 'Python 3.8 set in shebang.\n' ;;
		19|19.*)
			sed -i '1s/python/python3.6/' "$Dir/$TargetFile"
			printf 'Python 3.6 set in shebang.\n' ;;
		''|*)
			printf 'Err: Unknown version of Linux Mint.\n' 1>&2
			exit 1 ;;
	esac
else
	printf 'NOTE: Linux Mint not found -- shebang may be incorrect.\n'
fi
