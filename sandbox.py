name = "my-name.is  Mauro"

namef = name

repChars = ['.', '-', '_', '    ', '   ', '  ']


for c in repChars:
	namef = namef.replace(c, ' ')

print namef

