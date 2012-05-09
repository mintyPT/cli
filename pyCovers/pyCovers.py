import os
import requests
import BeautifulSoup


OUTPUT_FOLDER = 'out/'
# TODO: as capas a gardar precisam de ser as inglesas

def getWiiCovers(item):
    """
    Function to handle all the work!
    """

    folders = list()
    cURLS   = list()

    print '==> Game %s:' % (item)

    url  = 'http://www.gametdb.com/Wii/' + item
    r    = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(r.content)

    frame = soup.findAll("img")

    for img in frame:
        
        img = str(img)

        if img.find(item) != -1:
            
            ind    = img.find('"')
            newStr = img[ind + 1:]

            ind = newStr.find('"')
            url = newStr[:ind]

            cURLS.append(url)
            
            urlt = url.replace('http://art.gametdb.com/wii/', '')
            fld  = urlt.split('/')[0]
            folders.append(fld)

    for i in range(len(cURLS)):
        if '?' in cURLS[i]:

            print '\t- Downloading %s' % (folders[i])

            if os.path.exists(OUTPUT_FOLDER + folders[i]) == False:
                os.makedirs(OUTPUT_FOLDER + folders[i])

            imgfile = requests.get(cURLS[i]).content

            f = open(OUTPUT_FOLDER + folders[i] + '/' + item + '.png', 'w')
            f.write(imgfile)
            f.close()




gameList = [
            'S5BETL',
            'ST7P01',
            # 'RQLE64',
            # 'SDXP4Q',
            # 'SF8E01',
            # 'RDSPAF',
            # 'SCJP4Q',
            # 'SIIP8P',
            # 'RM8P01',
            # 'RMKP01',
            # 'RMCP01',
            # 'RNJE4F',
            # 'SM8E52',
            # 'PPNE01',
            # 'SOJP41',
            # 'RRBP41',
            # 'R3RP8P',
            # 'RSMP8P',
            # 'RSBE01',
            # 'STKP08',
            # 'ST9E52',
            # 'R6REJH',
            # 'SSWDRM',
            # 'RWMP78',
            ]


# #gameList.append('SOUE01')

# while len(gameList) != 0:
#     getWiiCovers(gameList[-1])
#     del gameList[-1]
    
for game in gameList:
    getWiiCovers(game)



