import urllib
from BeautifulSoup import*

url = input()

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    print (tag.get('href', None))