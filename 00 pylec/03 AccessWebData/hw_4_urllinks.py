# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cnt = 0
pos = 0


url = input('Enter - ')
if len(url) < 1 :
    url =  'http://py4e-data.dr-chuck.net/known_by_Amanda.html'

#POSITION = URL POSITON, COUNT = CLICK URL
cnt = int(input('Enter count:'))
pos = int(input('Enter position:'))

gloURL = url

#GET HTML INFORMATION in urll
def autoLinker(urll='http://py4e-data.dr-chuck.net/known_by_Amanda.html'):
    print('Retrieving:', urll)
    tmphtml = urllib.request.urlopen(urll, context=ctx).read()
    tmpsoup2 = BeautifulSoup(tmphtml, 'html.parser')
    tmptags = tmpsoup2('a')
    return tmptags

#FIND URL STRING ON POSITON in tags
def findPostion(poss, tagss):
    i = 0
    for tag in tagss:
        i = i + 1
        if i == poss:
            return tag.get('href', None)

k = 0
while k <= cnt:
    tags = autoLinker(gloURL)
    gloURL = findPostion(pos, tags)
    k = k + 1
