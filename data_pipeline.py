# Peter Trieu - Future Associates Cuusoo Tech Assessment

# Imported Packages
import json
import os
from collections import Counter
import csv
from datetime import date

# ====================== EXTRACTING ===============================
# Extracting all files within the weather_data folder
path = "weather_data/"
files = os.listdir(path)
print(files)

# Opening JSON file
with open('weather_data/'+files[0]) as f:
    # Returning JSON object as a dictionary
    data = json.load(f)

# Create array based on the number of array of objects in JSON file to store the temperature, weather text and three common weather text
temp_array = [0]*len(data)
weather_text_array = ["No Data"]*len(data)
three_common_array = ["No Data"]*3

# Extract the city name
city_name = data[0]["city"].strip().title() # Remove leading and trailing white spaces and capitalise the first letter of word

# Iterating through the JSON list
for i in range(len(data)):
    # Retrieving the required data
    temp_array[i] = data[i]["Temperature"]["Metric"]["Value"] # Assume that we are using Metric Value
    weather_text_array[i] = data[i]["WeatherText"].title() # Capitalise the first letter of word

# Closing the JSON file
f.close()

# ====================== TRANFORMING ===============================
# Calculating the average temperature
average_temp = round(sum(temp_array)/len(temp_array),1) # Round to nearest 1 decimal place

# Calculating the top three most common weather text
weather_text_counter = Counter(weather_text_array) # Convert array of weather text to Counter class
three_common = weather_text_counter.most_common(3) # Ordered alphabetically

# Iterating to retrieve only the text value of the three common weather text
for j in range(len(three_common)):
    three_common_array[j] = three_common[j][0].strip() # Remove leading and trailing white spaces

# ====================== LOADING ===============================
# Create the file and open it in write mode
f = open('weather_results/'+str(date.today().strftime("%d-%m-%Y"))+'.csv', 'w', newline='') 

# Create the csv write
writer = csv.writer(f)

# write the header row to the csv file
writer.writerow(["City","Average Temperature in Celcius","Top Three Most Common Weather Text"])

# write the header row to the csv file
writer.writerow([city_name,average_temp,three_common_array]) 

# close the file
f.close()