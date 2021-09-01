"""
iss_tracker.py by Gabriel Braden
 
Terminal tool that calculates your two dimensional distance from the International Space Station
"""
import requests
import time
import numpy
import sys
 
 
def toRadian(deg):
   """
   Converts degrees to radians
 
   Parameters
   ----------
   deg: float
       some degree that will be converted to radians
  
   Returns
   --------
   rad: float
       the radian equivalent of deg
   """
 
   if -360 <= deg and 360 >= deg:
       rad = deg * (numpy.pi/180)
       return rad
   else:
       print("Error: invalid degree value, terminating the program.")
       sys.exit()
 
 
def calcDist(lat1, long1, lat2, long2):
   """
   Uses the haversine equation to calculate the distance between two points on the globe
 
   Parameters
   ----------
   lat1: float
       the latitude of the first location
   long1: float
       the longitude of the first location
   lat2: float
       the latitude of the second location
   long2: float
       the longitude of the second location
 
 
   Returns
   --------
   d: float
       distance in kilometers between the first and second locations
   """
  
   dLat = toRadian(lat2 - lat1)
   dLon = toRadian(long2 - long1)
 
   a = (
       numpy.sin(dLat/2) * numpy.sin(dLat/2) +
       numpy.cos(toRadian(lat1)) * numpy.cos(toRadian(lat2)) *
       numpy.sin(dLon/2) * numpy.sin(dLon/2)
   )
   c = 2 * numpy.arctan2(numpy.sqrt(a), numpy.sqrt(1 - a))
   d = 6377 * c
   return d
 
 
lat1 = float(input('Enter your current latitude: '))
long1 = float(input('Enter your current longitude: '))
 
while True:
   response = requests.get('http://api.open-notify.org/iss-now.json').json()
   print(f"Your two dimensional distance distance from the ISS is {calcDist(lat1, long1, float(response['iss_position']['latitude']), float(response['iss_position']['longitude']))} km")
   time.sleep(1)
 
