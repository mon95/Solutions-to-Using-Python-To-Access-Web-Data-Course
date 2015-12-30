import urllib
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    # address = raw_input('Enter location: ')
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    # url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    sum = 0

    results = tree.findall('.//count')
    for c in results:
        sum += int(c.text)
    print sum

    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text

    # print 'lat',lat,'lng',lng
    # print location