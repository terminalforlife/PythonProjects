#!/usr/bin/env python3.6

#------------------------------------------------------------------------------
# Project Name      - PythonProjects/source/miscellaneous/gtkdemo.py
# Started On        - Thu 25 May 00:00:01 BST 2023
# Last Change       - Mon 19 Jun 23:34:57 BST 2023
# Author E-Mail     - terminalforlife@yahoo.com
# Author GitHub     - https://github.com/terminalforlife
#------------------------------------------------------------------------------
# Demonstrating using a basic Gtk GUI to print out the output entered into an
# Entry widget via a Button widget. Even with the class, this is easier than in
# Perl, especially as Gtk is well documented in Python!
#------------------------------------------------------------------------------

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Root(Gtk.Window):
	# The constructor.
	def __init__(self):
		# The Gtk.Window constructor, to set the title.
		Gtk.Window.__init__(self, title='Test')
		self.set_default_geometry(400, 30)

		# Create the box inside the main window.
		self.box = Gtk.Box()
		self.add(self.box)

		# Create a button, set up an event, and add to box.
		self.button = Gtk.Button(label='Click Me')
		self.button.connect('clicked', self.button_clicked)
		self.box.pack_start(self.button, True, True, 0)

		self.input = Gtk.Entry()
		self.box.pack_end(self.input, True, True, 0)

	def button_clicked(self, widget):
		print(self.input.get_text())


window = Root()
window.connect('delete-event', Gtk.main_quit)
window.show_all()

Gtk.main()
