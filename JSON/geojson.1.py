import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'


address = input('Enter location: ')
if len(address) < 1: print ('Not Good')

url = serviceurl + urllib.parse.urlencode(
    {'sensor': 'false', 'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

#if not js or 'status' not in js or js['status'] != 'OK':
#    print('==== Failure To Retrieve ====')
#    print(data)
#    continue

#print(json.dumps(js, indent=4))

place_id = js["results"][0]["place_id"]
print (place_id)