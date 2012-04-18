#!/usr/bin/env python
import os
import shutil

dest = {
    '# media': ['rmvb', 'mp4', 'avi', 'mkv', 'wmv', 'mov', 'flv'],
    '# pdf': ['pdf', 'djvu'],
    '# markdown': ['md'],
    '# arquive': ['zip', 'rar'],
    '# BD': ['cbr', 'cbds'],
    '# matlab': ['fig', 'm'],
    '# music': ['mp3', 'm4a', 'wma', 'ogg'],
    '# firefox': ['xpi'],
    '# photoshop': ['atn', 'acv'],
    '# email': ['eml'],
    '# webloc': ['webloc'],
    '# pics': ['jpg', 'jpeg', 'png', 'gif', 'psd'],
    '# powerpoint': ['pps', 'ppt', 'key'],
    '# doc': ['doc', 'docx', 'xls', 'xlsx'],
    '# txt': ['txt', 'rtf'],
    '# html': ['html'],
    '# wii': ['wbfs'],
    '# scripts': ['sh'],
    '# win stuff': ['exe'],
    '# mac apps': ['dmg', 'prefPane', 'pkg'],
    '# mac apps/# adium': ['AdiumSoundset', 'AdiumMessageStyle', 'AdiumMessageStyle']
    }


def isFolder(path):
    # Will check if path is a folder or not
    return os.path.isdir(path)


def createFolderIfNotExistant(path):    
    # Check is path is an existing folder. If not, creates it.
    if not os.path.isdir(path):
        os.mkdir(path)

def removedir(path):
    os.removedirs(path)



def handleFile(path, file):
    (name, ext) = os.path.splitext(file)
    ext = ext.replace('.', '')

    for destination in dest:
        if ext in dest[destination]:
            createFolderIfNotExistant(path + destination)
            src = path + file
            dst = path + destination + '/' + file
            shutil.move(src, dst)

def handleFolder(path, folder):
    fileNum = len(os.listdir(path + folder))

    if fileNum == 0:
        removedir(path + folder)
    elif fileNum == 1:
        oneFile = os.listdir(path + folder)
        src = path + folder + '/' + oneFile[0]
        dst = path + '/' + oneFile[0]
        shutil.move(src, dst)
        removedir(path + folder)


def cleanpy(path = './'):

    files   = []
    folders = []
    
    dirList = os.listdir(path)

    for item in dirList:

        # To delete ".DS_Store" files
        if item == ".DS_Store":
            os.remove(path + item)
            continue

        # Ignores files starting with a dot (invisible files)
        if item[0] == '.':
            continue    

        # Determine if item is a file or folder.
        if not isFolder(path + item):
            files.append(item)
        else:
            folders.append(item)

    # Sort files
    for file in files:
        handleFile(path, file)

    # Take action on folder if needed
    for folder in folders:
        handleFolder(path, folder)

cleanpy()

