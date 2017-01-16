import urllib
from bs4 import BeautifulSoup as bs

url = raw_input()
print (url)
html = urllib.urlopen(url).read()
soup = bs(html)

tags = soup('a')

for tag in tags:
    print (tag.get('href', None))
