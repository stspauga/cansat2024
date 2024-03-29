import time
import functions
import initCSV


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
        gpsSats = functions.gpsSats()
        tiltX = functions.tiltX()
        tiltY = functions.tiltY()
        rotation = functions.rotation()
        
        #Displaying those variables in their respective columns
        initCSV.df.at[rowNum,'Altitude'] = str(altitude)
        initCSV.df.at[rowNum,'GPS Time'] = GPSTime
        initCSV.df.at[rowNum,'Mission Time'] = MissionTime
        initCSV.df.at[rowNum,'Packet Count'] = packetCount
        initCSV.df.at[rowNum,'Mode'] = "FLIGHT MODE"
        initCSV.df.at[rowNum,'State'] = state
        initCSV.df.at[rowNum,'Airspeed'] = str(airSpeed) + " m/s"
        initCSV.df.at[rowNum,'Heat Shield Deployed'] = "Heat Shield NOT Deployed"
        initCSV.df.at[rowNum,'Parachute Deployed'] = "Parachute NOT Deployed"
        initCSV.df.at[rowNum,'Temperature'] = str(round(dummyTemp, 2)) + " F"
        initCSV.df.at[rowNum,'Pressure'] = str(round(dummyPressure, 2)) + " milibars"
        initCSV.df.at[rowNum,'Voltage'] = str(round(dummyVoltage, 2)) + " V"
        initCSV.df.at[rowNum,'GPS Altitude'] = str(altitude) + " meters"
        initCSV.df.at[rowNum,'GPS Latitude'] = lat
        initCSV.df.at[rowNum,'GPS Longitude'] = lon
        initCSV.df.at[rowNum,'GPS Sats'] = gpsSats
        initCSV.df.at[rowNum,'Tilt x'] = tiltX
        initCSV.df.at[rowNum,'Tilt y'] = tiltY
        initCSV.df.at[rowNum,'Rotation'] = rotation

        
        


        #Add all the changes from the data frame to the csv
        initCSV.df.to_csv('cansat_test.csv', index=False)
        dummyVoltage += .3
        dummyPressure += 2.6
        dummyTemp += .8
        packetCount = packetCount + 1
        rowNum = rowNum + 1
        dummyHorizontal = dummyHorizontal + .5
        time.sleep(.2)

simFile.close()
