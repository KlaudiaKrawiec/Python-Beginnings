import urllib.request

with urllib.request.urlopen('http://uek.krakow.pl/') as response:
    html = response.read()
print(html)
