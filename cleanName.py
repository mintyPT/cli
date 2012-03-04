#!/usr/bin/env python

# cleanName.py is meant to clean the name of your files
# it will simply remove '.', '-', '_' and multiple
# spaces. 
# Before renaming, it will ask you for permission.

import os


def cleanName():
	path = './'

	dirList = os.listdir(path)

	for item in dirList:
		if item[0] != '.':
			
			(name, ext) = os.path.splitext(item)

			namef = name
			namef = namef.replace('.', ' ')
			namef = namef.replace('-', ' ')
			namef = namef.replace('_', ' ')

			namef = namef.replace('    ', ' ') # 4 espacos
			namef = namef.replace('   ', ' ')  # 3 espacos
			namef = namef.replace('  ', ' ')   # 2 espacos
			namef = namef.strip()
			
			if name != namef:
				print 'Rename? \t%s \nto:\t\t%s' % (name+ ext, namef+ ext)
				
				v = raw_input('(y/n) ')
				if v == 'y':
					os.rename(path + name + ext, path + namef + ext)


cleanName()