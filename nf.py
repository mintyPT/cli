#!/usr/bin/env python
# ln nf.py /usr/local/bin/nf.py
# chmod a+x nf.py

# After doing this I learned about touch :/

import os
import optparse


def nf():
	p = optparse.OptionParser()
	p.add_option('--file', '-f', default="file.txt")
	options, arguments = p.parse_args()

	file = open(options.file, 'w')
	file.write("")
	file.close()
	print '> File %s created' % (options.file)

if __name__ == '__main__':
	nf()
