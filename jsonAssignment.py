import json
import urllib

url = raw_input('Enter URL: ')
data = urllib.urlopen(url).read()
jsondata = json.loads(data)
# print json.dumps(jsondata, indent=4)
sum = 0
for i in jsondata["comments"]:
    sum += int(i['count'])

print sum
