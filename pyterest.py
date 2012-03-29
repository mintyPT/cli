import requests
from bs4 import BeautifulSoup
import urllib



def getPic(link, folder):
	"""
	Return the link to the pinterest image
	"""
	r = requests.get(link)
	soup = BeautifulSoup(r.text)
	p = soup.find(id="PinImageHolder").img.get('src')

	savePic(p, folder)

	return p


def savePic(imglink, folder):
	"""
	Save an image from the web to the hd
	"""
	temp = imglink.split('/')[-1]
	fileName = temp[:-4]
	fileExt = temp[-3:]
	f = open("%s/%s.%s" % (folder, fileName, fileExt),'wb')
	f.write(urllib.urlopen(imglink).read())
	f.close()
	print "> %s/%s.%s" % (folder, fileName, fileExt)


def getBoard(board):
	""" 
	Get all the links from a board
	"""
	result = []
	r = requests.get(board)
	soup = BeautifulSoup(r.text)
	for s in soup.find_all("div", "pin"):
		for t in s.find_all("a", "PinImage"):#.a["PinImage"]#.get('href')
			result.append('http://pinterest.com' + t.get('href'))
	print "> Got %s links..." % (len(result))
	return result

def main():

	# Folder to store the pictures from the board
	folder = 'pinup'

	# Don't forget the '/' slash at the end of the link
	board = 'http://pinterest.com/charmainezoe/art-pin-up-calendar-pulp-art/'



	pinPages = []

	i =1
	while(1):

		link = '%s?page=%s' % (board, i)

		boardLinks = getBoard(link)

		[pinPages.append(l) for l in boardLinks]

		if len(boardLinks) != 50:
			break

		i+=1
	
	print len(pinPages)


	pinImages = [getPic(p, folder) for p in pinPages]


if __name__ == '__main__':
	main()

# r = requests.get(imgLink)

# i = StringIO(r.content)



