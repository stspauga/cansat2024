import pandas as pd

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