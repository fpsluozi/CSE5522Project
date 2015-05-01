# Final project CSE5522 Yiran Luo, Jun Wang, Peixuan Jiang, Suhas Gudhe 
# Date: April 20, 2015
# Geographic coordinate generator
# Used to acquired coordinates for the 2011 predictions. 
# Module used: geopy w/ Google V3

from geopy.geocoders import *
from geopy.exc import GeocoderTimedOut
import csv

# Create a list to hold address
address = []
coordinate = []
listOfRow = []
geolocator = GoogleV3(api_key="")

# Load from source csv
with open('DOF__Condominium_comparable_rental_income___Manhattan_-_FY_2010_2011.csv', 'rU') as f:
    reader = csv.DictReader(f)
    for row in reader:
        address.append(row['MANHATTAN CONDOMINIUM PROPERTY Address'] + ', New York, NY')
i = 0

# Scan through each address
for ad in address:
    try:
        location = geolocator.geocode(ad, timeout=None)
        if location is None:
            coordinate.append("Can not find")
            print "Cannnot find coord"
        else:
            coordinate.append(str(location.latitude) + ' ' + str(location.longitude))
            print str(location.latitude) + ' ' + str(location.longitude)
    except GeocoderTimedOut as e:
        coordinate.append("Can not find")
        print "Cannnot find coord"

    i += 1

# Write the coordinates to the target chart
with open('2011_With_Coordinate_2.csv', 'r') as f2:
    reader = csv.reader(f2)
    for row2 in reader:
        listOfRow.append(row2)
    listOfRow[0].append('Coordinate')
    for i in range(0, len(coordinate)):
        listOfRow[i + 1].append(coordinate[i])

with open('2011_With_Coordinate_new.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(listOfRow)