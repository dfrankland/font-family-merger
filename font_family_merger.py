import os
import shutil
from fontTools import ttx
import lxml
from bs4 import BeautifulSoup
from bs4 import NavigableString

def parseFont(files):
    for file in files:
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

def getFilesWith(extension):
    files = []
    for file in [file for file in os.listdir('.') if os.path.isfile(file)]:
        if file.endswith(extension):
            files.append(file)
    return files

if __name__ == "__main__":
    if not os.path.exists("merged_fonts"):
        os.makedirs("merged_fonts")
    for file in getFilesWith(".ttf"):
        shutil.copy(file,"merged_fonts")
    os.chdir("merged_fonts")
    ttx.main(getFilesWith(".ttf"))
    for file in getFilesWith(".ttf"):
        os.remove(file)
    parseFont(getFilesWith(".ttx"))
    ttx.main(getFilesWith(".ttx"))
    for file in getFilesWith(".ttx"):
        os.remove(file)
