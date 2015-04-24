from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import csv
# creat a list to hold address
address = []
coordinate = []
listOfRow = []
geolocator = Nominatim()
with open('DOF__Condominium_comparable_rental_income___Manhattan_-_FY_2010_2011.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        address.append(row['MANHATTAN CONDOMINIUM PROPERTY Address'] + ', New York City, NY')
i = 0
for ad in address:
    print(i)
    try:
        location = geolocator.geocode(ad,timeout=None)
        if location is None:
            coordinate.append("Can not find")
        else:
            coordinate.append(str(location.latitude) + ' ' + str(location.longitude))
    except GeocoderTimedOut as e:
        coordinate.append("Can not find")

    i += 1
with open('2011_With_Coordinate.csv', 'r') as f2:
    reader = csv.reader(f2)
    for row2 in reader:
        listOfRow.append(row2)
    listOfRow[0].append('Coordinate')
    for i in range(0, len(coordinate)):
        listOfRow[i + 1].append(coordinate[i])
with open('2011_With_Coordinate_new.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(listOfRow)