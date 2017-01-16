import json
import urllib

address = raw_input('Enter website: ')
uh = urllib.urlopen(address)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

sums = 0
for element in js['comments']:
    sums = sums + element['count']

print sums

'''http://python-data.dr-chuck.net/comments_311217.json   http://python-data.dr-chuck.net/comments_42.json
