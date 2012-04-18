#!/usr/bin/env python

import os



def newName(namef):
	repChars = ['.', '_', '    ', '   ', '  ']

	for c in repChars:
		namef = namef.replace(c, ' ')

	namef = namef.strip()

	return namef



def cleanName():
	dirList = os.listdir('./')

	for item in dirList:
		if item[0] != '.':
			
			(name, ext) = os.path.splitext(item)

			namef = newName(name)		
			
			if name != namef:
				print 'Rename? \t%s \nto:\t\t%s' % (name + ext, namef + ext)
				
				# v = raw_input('(y/n) ')
				# if v == 'y':
				# 	os.rename(name + ext, namef + ext)

				os.rename(name + ext, namef + ext) if raw_input('(y/n) ') == 'y' else ''


cleanName()
print 'Done!'