import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter - ")

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

spantags = soup('span')

sum = 0

for tag in spantags:
    #print tag
    #print tag.contents[0]
    sum = sum + int(tag.contents[0])
    # print tag.attrs

print "Sum ",sum
