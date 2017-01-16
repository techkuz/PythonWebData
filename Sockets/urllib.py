import urllib
fhand = urllib.urlopen('http://www.yandex.ru')

for line in fhand:
    print(line.strip())