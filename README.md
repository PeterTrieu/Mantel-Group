# Introduction

Hi all,

The language used to write the weather data pipeline solution used was Python.
<div id="header" align="center">
  <img src="https://media0.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" width="100"/>
</div>

The modules that are used in this solution are listed below.
- [json](https://docs.python.org/3/library/json.html) - JSON encoder and decoder
- [os](https://docs.python.org/3/library/os.html) - Miscellaneous operating system interfaces
- [collections](https://docs.python.org/3/library/collections.html) - Container datatypes
- [csv](https://docs.python.org/3/library/csv.html) - CSV File Reading and Writing
- [datetime](https://docs.python.org/3/library/datetime.html) - Basic date and time types
- [shutil](https://docs.python.org/3/library/shutil.html) - High-level file operations

## How to run solution
To run the solution, the following is required:
- Ensure that the data to the processed is located within a folder called **weather_data** is on the same folder level as the **data_pipeline.py**
- Ensure that there is a folder called **archived_weather_data** and **weather_results** are on the same folder level as **data_pipeline.py**
- For the JSON data only the following keys that are listed below are required
```
{ 
    "LocalObservationDateTime": "2022-08-03T10:55:00+08:00",
    "WeatherText": " MOstlY ClOudy ",
    "Temperature": {
        "Metric": { 
            "Value": 15.0, 
            "Unit": "C", 
            "UnitType": 17 
        } 
    }, 
    "city": " pERTH " 
}
```
Then run the **data_pipeline.py** script that will generate the weather results into the folder **weather_results** and will archive all the JSON files into **archived_weather_data** folder. It will also rename the file as well with the date it was processed appended to the start of the file name.