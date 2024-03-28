import time
import pandas as pd
from datetime import datetime
import time
import math 
from geopy.geocoders import Nominatim



#-------------INITIALIZING CSV FILE-------------#
# Define the headers for the new DataFrame
headers = [
    "Mission Time", "Packet Count", "Mode", "State", "Altitude", "Airspeed", 
    "Heat Shield Deployed", "Parachute Deployed", "Temperature", "Pressure", 
    "Voltage", "GPS Time", "GPS Altitude", "GPS Latitude", "GPS Longitude", 
    "GPS Sats", "Tilt x", "Tilt y", "Rotation", 
]

# Create an empty DataFrame with the specified headers
df = pd.DataFrame(columns=headers)

# Save the DataFrame to 'cansat_test.csv', overwriting any existing file
df.to_csv('cansat_test.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv('cansat_test.csv')




#--------------FUNCTIONS------------------#
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
def calcAirSpeed(stringAlt, horizontalDistance):
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



#----------OPENING AND WRITING TO CSV FILE------------#
simFile = open("cansat_2023_simp.txt", "r", encoding="utf-8")
rowNum = 0
startTime = time.time()
packetCount = 1
dummyHorizontal = 1
dummyTemp = 98.0
dummyPressure = 1013.25
dummyVoltage = 20
for line in simFile:
    if line.startswith("CMD"):
        #Assigning returns from functions to their respective variables
        split_string = line.split(",")
        pressure = split_string[-1].strip().split()
        altitude = calcAltitude(pressure)
        GPSTime = calculateCurrentTime()
        MissionTime = calculateTime(startTime)
        state = determineState()
        airSpeed = calcAirSpeed(str(altitude),dummyHorizontal)
        returnLat, returnLon = calcLatandLon()
        lat = returnLat()
        lon = returnLon()
        
        #Displaying those variables in their respective columns
        df.at[rowNum,'Altitude'] = str(altitude) + " meters"
        df.at[rowNum,'GPS Time'] = GPSTime
        df.at[rowNum,'Mission Time'] = MissionTime
        df.at[rowNum,'Packet Count'] = packetCount
        df.at[rowNum,'Mode'] = "FLIGHT MODE"
        df.at[rowNum,'State'] = state
        df.at[rowNum,'Airspeed'] = str(airSpeed) + " m/s"
        df.at[rowNum,'Heat Shield Deployed'] = "Heat Shield NOT Deployed"
        df.at[rowNum,'Parachute Deployed'] = "Parachute NOT Deployed"
        df.at[rowNum,'Temperature'] = str(round(dummyTemp, 2)) + " F"
        df.at[rowNum,'Pressure'] = str(round(dummyPressure, 2)) + " milibars"
        df.at[rowNum,'Voltage'] = str(round(dummyVoltage, 2)) + " V"
        df.at[rowNum,'GPS Altitude'] = str(altitude) + " meters"
        df.at[rowNum,'GPS Latitude'] = lat
        df.at[rowNum,'GPS Longitude'] = lon
        


        #Add all the changes from the data frame to the csv
        df.to_csv('cansat_test.csv', index=False)
        dummyVoltage += .3
        dummyPressure += 2.6
        dummyTemp += .8
        packetCount = packetCount + 1
        rowNum = rowNum + 1
        dummyHorizontal = dummyHorizontal + .5
        time.sleep(.2)

simFile.close()
