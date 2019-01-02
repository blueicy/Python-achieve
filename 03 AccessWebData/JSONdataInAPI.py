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
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




#INPUT WEB ADDRESS
address = input('Enter location: ')
if len(address) < 1:
    address = 'South Federal University'


# URL CHANGER : check geoxml.py
parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key


#CONCANATE URL with address
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')


#READ data by json
try:
    js = json.loads(data)
except:
    js = None

#FAIL SAFE
if not js or 'status' not in js or js['status'] != 'OK':
    print('=== No JS ===')


#PRINT JSON PRETTY
#print(json.dumps(js, indent=4, sort_keys=True))
#print(len(js))

#FIND place_id in JS
for i in range(len(js)):
    try:
        placeid = js['results'][i]['place_id']
        print('Place id', placeid)
    except:
        continue
