import os
from fontTools import ttx
import lxml
from bs4 import BeautifulSoup
from bs4 import NavigableString

def parseFont(file):
    with open(file, 'r+') as fileOpen:
        data = fileOpen.read()
        fileOpen.close()
    soup = BeautifulSoup(data,'xml')
    for name in soup.findAll('namerecord'):
        nameAttrs = dict(name.attrs)
        if nameAttrs[u'nameID'] == "1":
            names = name.string.lstrip().split(" ",1)
            name.string.replace_with(names[0])
        if nameAttrs[u'nameID'] == "2":
            name.string.replace_with(names[1])
    newFileName = names[0] + "-" + names[1].rstrip() + ".ttx"
    data = soup.prettify("utf-8")
    with open(file, 'w') as fileClose:
        fileClose.write(data)
    os.renames(file, newFileName)
    return newFileName

def getFiles():
    return [file for file in os.listdir('.') if os.path.isfile(file)]

if __name__ == "__main__":
    ttfFiles = ttxFiles = []
    for file in getFiles():
        if file.endswith(".ttf"):
            ttfFiles.append(file)
    ttx.main(ttfFiles)
    for file in getFiles():
        if file.endswith(".ttx"):
            ttxFiles.append(parseFont(file))
    ttx.main(ttxFiles)
    for file in getFiles():
        if file.endswith(".ttx"):
            os.remove(file)
