import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_311213.xml'


uh = urllib.urlopen(serviceurl)
data = uh.read()

root = ET.fromstring(data)

comments = root.getchildren()[1]

sums = 0
for comment in comments.getchildren():
    sums = sums + int(comment.findtext('count'))

print (sums)
    


