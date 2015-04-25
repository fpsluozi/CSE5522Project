__author__ = 'junwang'
from geopy.geocoders import *
geolocator = GoogleV3(api_key="AIzaSyAcMoANDvLbymUGwhhtOhjW9BxcFghawd4")
location  = geolocator.geocode("3607 BROADWAY, New York, NY")
print(location.latitude, location.longitude)