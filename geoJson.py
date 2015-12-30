import json
import urllib
while True:
    loc = raw_input('Enter location: ')
    if len(loc)<1: break

    baseurl = 'http://python-data.dr-chuck.net/geojson?'
    url = baseurl + urllib.urlencode({'sensor':'false', 'address':loc})
    print "Retrieving", url

    data = urllib.urlopen(url).read()
    print "Retrieved ",len(data)," characters"

    jsonData = json.loads(str(data))

    # print json.dumps(jsonData, indent=4)
    print jsonData["results"][0]["place_id"]
