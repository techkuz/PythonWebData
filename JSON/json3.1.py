import json
import urllib

address = ('https://stepik.org/api/docs/')
uh = urllib.urlopen(address)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

print (js)
