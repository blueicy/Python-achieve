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

url = input('Enter - ')

if len(url) < 1 :
    url =  'http://py4e-data.dr-chuck.net/comments_162282.html'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#    print(tag.get('href', None))


#FIND CONTENTS IN TAGS THEN EXTRACT CONTENTS (FOR EX, NUMBERS)
sm = 0
cnt = 0

tags = soup('span')
for tag in tags:

    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Attrs:', tag.attrs)
    sm = sm + int(tag.contents[0])
    cnt = cnt + 1


print('Count:', cnt)
print('Sum:', sm)
