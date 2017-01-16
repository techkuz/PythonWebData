import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://zoneos.com/traffic/Райгородский.pdf')
for line in fhand:
    print(line.decode().strip())