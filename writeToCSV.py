import time
import pandas as pd
import random

# Read the CSV file into a DataFrame
df = pd.read_csv('cansat_test.csv')

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
    
simFile = open("cansat_2023_simp.txt", "r", encoding="utf-8")
rowNum = 0
for line in simFile:
    if "#" not in line:
        split_string = line.split(",")
        pressure = split_string[-1].strip().split()
        altitude = calcAltitude(pressure)
        if altitude is not None:
            print(altitude)
            df.at[rowNum,'Time'] = rowNum + 1
            df.at[rowNum,'Altitude'] = altitude
            df.to_csv('cansat_test.csv', index=False)
            rowNum = rowNum + 1
            time.sleep(.2)

simFile.close()


        

# if 'test' in df['Title'].values:
#     # Find the index of the row with the title 'test'
#     index_of_test = df.index[df['Title'] == 'test'].tolist()[0]

#     # Add random integers in the 10 rows below the 'test' row
#     for _ in range(10):
#         random_data = random.randint(1, 100)  # Adjust the range as needed
#         new_row = pd.DataFrame({'Title': [''], 'Data': [random_data]})
#         df = pd.concat([df.iloc[:index_of_test + 1], new_row, df.iloc[index_of_test + 1:]]).reset_index(drop=True)

#     # Save the updated DataFrame back to the CSV file
#     df.to_csv('your_file.csv', index=False)
# else:
#     print("Row with 'test' not found in DataFrame.")
