#!/usr/bin/env python


# http://www.xhtml2pdf.com/
# http://code.google.com/p/wkhtmltopdf/

import os
import shutil


def bookme(path = './'):

    output = ''

    dirList = os.listdir(path)

    for file in dirList:
        (name, ext) = os.path.splitext(file)
        ext = ext.replace('.', '')

        if (ext == 'md' or ext == 'txt') and name[0] != '_' :
            f = open(file, 'r')
            filecontent = f.read()
            f.close()

            output += filecontent
            output += '\n\n'

    f = open('_bookme.md', 'w')
    f.write(output)
    f.close()



if __name__ == '__main__':
    bookme()

