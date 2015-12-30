import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")
print url
count = int(raw_input("Enter count: "))
print count
position = int(raw_input("Enter position: "))
print position

while True:
    # print count
    print "Retrieving: ", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")    
    atags = soup('a')
    
    # print atags[position].contents[0]
    url = atags[position-1].get('href',None)
    # print url


    count -= 1
    if count == -0:
        # print atags
        print atags[position-1].contents[0]
        break
    atags = []