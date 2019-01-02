import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

#api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




#INPUT WEB ADDRESS
address = input('Enter location: ')
if len(address) < 1:
    address =  'http://py4e-data.dr-chuck.net/comments_162284.xml'
    #'http://py4e-data.dr-chuck.net/comments_42.xml'

#DISREGARD  URL CHANGER : check geoxml.py
parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
#/DISREGARD

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

#BUILDING XML TREE
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

sm = 0

#FIND TREE TAGS THEN EXTRACT DATA tagged 'count'
comments = tree.findall('comments')
comment = comments[0].findall('comment')
for i in range(len(comment)):
    sm = sm + int(comment[i].find('count').text)

#lat = comments[1].find('comment').find('count').text
#lng = results[0].find('geometry').find('location').find('lng').text
print ('Count:', len(comment))
print ('Sum:', sm)
