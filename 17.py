import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



"""
counts = dict()

for line in fname:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""

