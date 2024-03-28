import time
from datetime import datetime
import math 
from geopy.geocoders import Nominatim

def calcAltitude(airPressure):
    pressure_value = float(airPressure[-1])
    power = (1 / 5.255)
    base = (pressure_value / 101326)
    altitude = (44330 * (1 - (base ** power))) - 633.19
    if altitude < 0:
        return 0.0
    return str(round(altitude, 2))
    
    
def calculateCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
    
def calculateTime(startTime):
    elapsedSeconds = round(time.time() - startTime, 0)
    minutes = 0
    elapsedTime = f"{minutes}:{elapsedSeconds}"
    if elapsedSeconds % 60 == 0 and not elapsedSeconds == 0.0:
        minutes = minutes + 1
        elapsedSeconds = round(time.time() - startTime, 0)
        elapsedTime = f"{minutes}:{elapsedSeconds}"

    return elapsedTime

def determineState():
    #Need to change obviously but for now this is it
    return "IN FLIGHT"
    
#THIS FUNCTION IS VERY WRONG NEED TO FIX
#NOT TAKING SPEED FROM PREVIOUS
#COORDINATE, ONLY TAKING SPEED FROM 0,0 BASICALLY
def calcAirSpeed(stringAlt, horizontalDistance, startTime):
    altitude = float(stringAlt)
    trueDistance = math.sqrt(pow(altitude, 2) + pow(horizontalDistance, 2))
    elapsedSeconds = time.time() - startTime   
    if elapsedSeconds == 0:
        return "No speed yet"
    return round(float(trueDistance) / float(elapsedSeconds), 2)

def calcLatandLon():
    # calling the Nominatim tool and create Nominatim class
    loc = Nominatim(user_agent="Geopy Library")

    # entering the location name
    getLoc = loc.geocode("Arizona")

    # printing address
    #print(getLoc.address)

    def returnLat():
        #print("Latitude = ", getLoc.latitude, "\n")
        return getLoc.latitude

    def returnLon():
        #print("Longitude = ", getLoc.longitude)
        return getLoc.longitude

    return returnLat, returnLon