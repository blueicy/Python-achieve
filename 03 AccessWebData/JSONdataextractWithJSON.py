import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

#api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#INPUT WEB ADDRESS
address = input('Enter location: ')
if len(address) < 1:
    address =  'http://py4e-data.dr-chuck.net/comments_42.json'
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
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#print(data.decode())


sm = 0

try:
    js = json.loads(data)
except:
    js = None

if not js or 'comments' not in js:
    print('===FAILURE===')
    print(js)


for i in range(len(js["comments"])):
    sm = sm + int(js["comments"][i]["count"])

#XML FIND 'count' with TREE

#comments = tree.findall('comments')
#comment = comments[0].findall('comment')
#for i in range(len(comment)):
#    sm = sm + int(in.find('count').text)


print ('Count:', len(js["comments"]))
print ('Sum:', sm)
