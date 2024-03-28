import time
import pandas as pd
import random
from datetime import datetime
import time



#-------------INITIALIZING CSV FILE-------------#
# Define the headers for the new DataFrame
headers = [
    "Mission Time", "Packet Count", "Mode", "State", "Altitude", "Airspeed", 
    "Heat Shield Deployed", "Parachute Deployed", "Temperature", "Pressure", 
    "Voltage", "GPS Time", "GPS Altitude", "GPS Latitude", "GPS Longitude", 
    "GPS Sats", "Tilt x", "Tilt y", "Rotation"
]

# Create an empty DataFrame with the specified headers
df = pd.DataFrame(columns=headers)

# Save the DataFrame to 'cansat_test.csv', overwriting any existing file
df.to_csv('cansat_test.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv('cansat_test.csv')




#--------------FUNCTIONS------------------#
def calcAltitude(airPressure):
    try:
        pressure_value = float(airPressure[-1])
        power = (1 / 5.255)
        base = (pressure_value / 101326)
        altitude = 44330 * (1 - (base ** power))
        return altitude
    except (ValueError, IndexError):
        # Handle the case when conversion fails or the list is empty
        return None
    
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
    




#----------OPENING AND WRITING TO CSV FILE------------#
simFile = open("cansat_2023_simp.txt", "r", encoding="utf-8")
rowNum = 0
startTime = time.time()
packetCount = 1
for line in simFile:
    if "#" not in line:
        split_string = line.split(",")
        pressure = split_string[-1].strip().split()
        altitude = calcAltitude(pressure)
        GPSTime = calculateCurrentTime()
        MissionTime = calculateTime(startTime)
        state = determineState()
        if altitude is not None:
            print(altitude)
            df.at[rowNum,'Altitude'] = altitude
            df.to_csv('cansat_test.csv', index=False)
            rowNum = rowNum + 1
            time.sleep(.2)
        df.at[rowNum,'GPS Time'] = GPSTime
        df.at[rowNum,'Mission Time'] = MissionTime
        df.at[rowNum,'Packet Count'] = packetCount
        df.at[rowNum,'Mode'] = "FLIGHT MODE"
        df.at[rowNum,'State'] = state




        packetCount = packetCount + 1

simFile.close()
