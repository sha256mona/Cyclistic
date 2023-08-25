# import pandas with shortcut 'pd'
import pandas as pd
  
# read_csv function which is used to read the required CSV file
data = pd.read_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTALCLEAN.csv')
  
print("Original input CSV Data: \n")
print( data.head())

#creates ride_length and day_of_week columns
#had trouble here with the start/end times, python read them as strings so i had to convert them
#using pd.to_datetime to be able to 
data["ride_length"] = pd.to_datetime(data.ended_at) - pd.to_datetime(data.started_at)

#pandas dataframes are all inherently of type Series so i had to typecast
#everything using pd.to_datetime (again) to be able to use .dt.dayofweek
data["day_of_week"] = pd.to_datetime(data["started_at"]).dt.weekday
# display
print("\nCSV Data after adding the columns:\n")
print(data)

# save to new file without index numbers
data.to_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-FINALCOL.csv',index = False)