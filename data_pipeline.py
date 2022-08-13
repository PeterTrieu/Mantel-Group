# Peter Trieu - Future Associates Cuusoo Tech Assessment

# Imported Modules
import json
import os
from collections import Counter
import csv
from datetime import datetime
import shutil

# ====================== EXTRACTION ===============================
# Extract all file names within the weather_data folder
path = "weather_data/"
files = os.listdir(path)

# Iterate through all the JSON files
for i in range(len(files)):
    # Open JSON file
    with open('weather_data/'+files[i]) as f:
        # Return JSON object as a python dictionary
        data = json.load(f)

    # Create empty arrays based on the number of array of objects in JSON file to store the temperature and weather text
    temp_array = [0]*len(data)
    weather_text_array = ["No Data"]*len(data)

    # Initialise an empty array that will contain the top three most common weather text
    top_three = [""]*3

    # Retrieve the start datetime and end datetime of each file
    start_datetime = data[len(data)-1]["LocalObservationDateTime"]
    end_datetime = data[0]["LocalObservationDateTime"]

    # Extract the start date, start time, end date and end time
    start_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M:%S%z').date()
    end_date = datetime.strptime(end_datetime, '%Y-%m-%dT%H:%M:%S%z').date()
    start_time = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M:%S%z').time()
    end_time = datetime.strptime(end_datetime, '%Y-%m-%dT%H:%M:%S%z').time()

    # Retrieve the city name
    city_name = data[0]["city"].strip().title() # Remove leading and trailing white spaces and capitalise the first letter of word

    # Iterate through the JSON list
    for j in range(len(data)):
        # Retrieve the required data
        temp_array[j] = data[j]["Temperature"]["Metric"]["Value"] # Assume that we are using metric value
        weather_text_array[j] = data[j]["WeatherText"].title() # Capitalise the first letter of word

    # Close the JSON file
    f.close()

    # Archive the json file
    shutil.move(r'weather_data/'+files[i], r'archived_weather_data/'+str(start_date)+"_"+city_name+".json")

# ====================== TRANFORMATION ===============================
    # Calculate the average temperature
    average_temp = round(sum(temp_array)/len(temp_array),1) # Round to nearest 1 decimal place

    # Calculate the top three most common weather text
    weather_text_counter = Counter(weather_text_array) # Convert array of weather text to Counter class
    three_common = weather_text_counter.most_common(3) # Ordered from highest to lowest count then alphabetically

    # Iterate to retrieve only the text value of the top three most common weather text
    for k in range(len(three_common)):
        top_three[k] = three_common[k][0].strip() # Remove leading and trailing white spaces

# ====================== LOAD ===============================
    # Create a new csv file if csv file doesn't exist
    if(os.path.exists('weather_results/weather_results.csv') == False):
        # Open the file in write mode
        f = open('weather_results/weather_results.csv', 'w', newline='') 

        # Create the csv write
        writer = csv.writer(f)

        # Write the header row to the csv file
        writer.writerow(["Start Date","Start Time","End Date","End Time","City","Average Temperature in Celcius","Top Three Most Common Weather Text"])

        # close the file
        f.close()

    # Open the file in append mode
    f = open('weather_results/weather_results.csv', 'a', newline='') 

    # Create the csv write
    writer = csv.writer(f)

    # Write the row of data extracted from the JSON file
    writer.writerow([start_date,start_time,end_date,end_time,city_name,average_temp,top_three]) 

    # close the file
    f.close()