import pandas as pd
import time
import functions



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
        altitude = functions.calcAltitude(pressure)
        GPSTime = functions.calculateCurrentTime()
        MissionTime = functions.calculateTime(startTime)
        state = functions.determineState()
        airSpeed = functions.calcAirSpeed(str(altitude),dummyHorizontal, startTime)
        returnLat, returnLon = functions.calcLatandLon()
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
