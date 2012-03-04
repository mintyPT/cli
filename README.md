# Cli utilities

This is the repository for my own personal cli (*command line utilities*) and custom scripts, so I can scratch my own itches because no one else will scratch them for me :)


## nf - creates new files

This is meant to create new files. I was missing the 'right-button click > new txt file' from windows. It was only after coding this, I found the 'touch' command line utility. Anyway,

**Usage:** nf.py -f fileName.fileExtension

## cleaName - clean names
Small utility to help me clean the name of the files inside a directory.

This utility will simply remove '.', '-', '_' and multiple
spaces. Also, it will ask permission before doing any renaming.

**Usage:** Create a symlink and lauch inside a folder or put it inside the folder where you want to use it and launch.

## dontEvenTrack
Simple script to scrape the last post's title from dontevenreply.com so I can keep up. I use this script with geektool to display the info on my desktop.

**Usage:** Simply run it, it prints to the console.

## sorter.py

This will:
	- Sort your files
	- Delete folders with no files
	- Delete folders with one file after extracting them to the parent folder

Use carefully! 


### ToDo

- Comment the code
- Good support for the command 
- Sorting by keyword
- Support to run over time automatically
- Config type script
- More functions? 
- Convert it to a true cli utility and merge it into a new project


### Other

Had a problem with github's git app. Had to use 
<pre><code>git stash</code></pre>
to be able to commit this and then 
<pre><code>git stash pop</code></pre>
after committing and syncing, although I'm still not quite sure at the moment on how this works. This is only a quick fix.

