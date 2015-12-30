import urllib

fhandle = urllib.urlopen("http://www.py4inf.com/code/romeo.txt")

for line in fhandle:
    print line,
    if len(line)<1:
        break
