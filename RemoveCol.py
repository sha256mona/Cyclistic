# import pandas with shortcut 'pd'
import pandas as pd
  
# read_csv function which is used to read the required CSV file
data = pd.read_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTAL.csv')
  
# display
print("Original input CSV Data: \n")
print(data)
  
# pop function which is used in removing or deleting columns from the CSV files
#data.pop('start_lat')
#data.pop('start_lng')
#data.pop('end_lat')
#data.pop('end_lng')
data.pop('start_station_name')
data.pop('end_station_name')
data.pop('start_station_id')
data.pop('end_station_id')

#Loop through entire dataframe

#conditional: If ANY of the start/end of lat/lng values drop the row
  
# display
print("\nCSV Data after deleting the columns:\n")
print(data)

# save to new file without index numbers
data.to_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTALCLEAN.csv',index = False)