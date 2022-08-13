# Peter Trieu - Future Associates Cuusoo Tech Assessment

# Imported Packages
import json
import os

# Extracting all files within the weather_data folder
path = "weather_data/"
files = os.listdir(path)
print(files)

# Opening JSON file
with open('weather_data/'+files[0]) as f:
    # Returning JSON object as a dictionary
    data = json.load(f)

# Create array based on the number of array of objects in JSON file to store the temperature and weather text
temp_array = [0]*len(data)
weather_text_array = ["No Data"]*len(data)
print(temp_array)
print(weather_text_array)

# Iterating through the JSON list
for i in data:
    print("New Line")