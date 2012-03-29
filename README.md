# Cli utilities

This is the repository for my own personal cli (*command line utilities*) and custom scripts, so I can scratch my own itches because no one else will scratch them for me :)


## Command Line Utilities

### cleaName - clean names
Small utility to help me clean the name of the files inside a directory.

This utility will simply remove '.', '-', '_' and multiple
spaces (you can edit the list of symbols at the beggining of the file). Also, it will ask permission before doing any renaming, just to be safe.

**Usage:** Create a symlink and lauch inside a folder or put it inside the folder where you want to use it and launch.

### nf - creates new files

This is meant to create new files. I was missing the 'right-button click > new txt file' from windows. It was only after coding this, I found the 'touch' command line utility. Anyway,

**Usage:** nf.py -f fileName.fileExtension

### sorter.py

This will:
* Sort your files
* Delete folders with no files
* Delete folders with one file after extracting them to the parent folder

Use carefully! 

**Usage:** Create a symlink and launch inside the folder where the files to sort are, or put it inside the folder and run it.


## Custom scripts

### pyterest.py
**I love pinups!** Once upon a time, I found a pinterest board, full of pinup images! I simply wasn't gonna download 311 images by hand so I coded this: 

I present to you an image scraper from the pinterest's boards. 

**Usage:** Open the file and change the url to the board and the folder to keep the images. Don't forget to create the folder before running.

_ps:_ I ended up not keeping any of those pictures since in the end, it was all about writing a couple of lines in python to see if I could scrape like a mad man! 

### dontEvenTrack
Simple script to scrape the last post's title from dontevenreply.com so I can keep up. I use this script with geektool to display the info on my desktop.

**Usage:** Simply run it, it prints to the console.



