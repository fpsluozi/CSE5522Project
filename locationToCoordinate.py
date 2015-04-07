__author__ = 'junwang'
from geopy.geocoders import Nominatim
import csv
# creat a list to hold address
address = []
coordinate = []
listOfRow = []
geolocator = Nominatim()
with open('DOF__Condominium_Comparable_Rental_Income___Manhattan___FY_2009_2010.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        address.append(row['MANHATTAN CONDOMINIUM PROPERTY Address'] + ' NY')

for ad in address:
    location = geolocator.geocode(ad)
    coordinate.append(str(location.latitude) + ' ' + str(location.longitude))
with open('DOF__Condominium_Comparable_Rental_Income___Manhattan___FY_2009_2010.csv', 'r') as f2:
    reader = csv.reader(f2)
    for row2 in reader:
        listOfRow.append(row2)
    listOfRow[0].append('Coordinate')
    for i in range(0, len(coordinate)):
        listOfRow[i + 1].append(coordinate[i])
with open('DOF__Condominium_Comparable_Rental_Income___Manhattan___FY_2009_2010_With_Coordinate.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(listOfRow)