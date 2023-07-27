#!/usr/bin/env python

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/update-wallpaper.py
# Started On        - Sun 25 Jun 22:21:27 BST 2023
# Last Change       - Thu 27 Jul 23:56:03 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Automatically adjust the wallpaper in Cinnamon whenever a resolution change
# is detected. This, at least for now, assumes and handles a single display.
# Set this to execute at login, using Startup Applications.
#
#   IE: `python3.10 /path/to/update-wallpaper.py`
#
# Written in hopes of addressing:
#
#   https://forums.linuxmint.com/viewtopic.php?t=398831
#
# Dependencies:
#
#   python (>= 3.6)
#   python3-xlib (>= 0.20-3)
#   libglib2.0-bin (>= 2.56.4)
#------------------------------------------------------------------------------

import time, subprocess
from Xlib.display import Display

Schema, Key = 'org.cinnamon.desktop.background', 'picture-uri'
Command = ['gsettings', '', Schema, Key]

def Resolution() -> tuple:
	Screen = Display().screen(0)

	return(Screen['width_in_pixels'], Screen['height_in_pixels'])

def Wallpaper(URI: str = None) -> None:
	if URI is None:
		Command[1] = 'get'
		URI = str(subprocess.check_output(Command), 'utf-8')

	Command[1] = 'set'
	subprocess.run((*Command, URI))

try:
	Old = Resolution()
	while True:
		New = Resolution()
		if New != Old: Wallpaper()
		Old = Resolution()

		time.sleep(1)
except KeyboardInterrupt:
	pass
