# Peter Trieu - Future Associates Cuusoo Tech Assessment

# Imported Packages
import json
import os
from collections import Counter

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

# Extract the city name
city_name = data[0]["city"].title() # Capitalise the first letter of word
print(city_name)

# Iterating through the JSON list
for i in range(len(data)):
    # Retrieving the required data
    temp_array[i] = data[i]["Temperature"]["Metric"]["Value"] # Assume that we are using Metric Value
    weather_text_array[i] = data[i]["WeatherText"].title() # Capitalise the first letter of word

# Calculating the average temperature
average = round(sum(temp_array)/len(temp_array),1) # Round to nearest 1 decimal place

# Calculating the top three most common weather text
weather_text_counter = Counter(weather_text_array) # Convert array of weather text to Counter class
three_common = weather_text_counter.most_common(3) # Ordered alphabetically
print(weather_text_array)
print(three_common)