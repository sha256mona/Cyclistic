# import pandas with shortcut 'pd'
import pandas as pd

# read_csv function which is used to read the required CSV file
#change this argument to cycle through the csv files you want to append to the total.
#if i was better i would loop this to go through all the files in the directory.
# so instead i hardcoded the source and destination arguments for .read_csv and .to_csv
data = pd.read_csv('DataAnalysis/202305-divvy-tripdata/202305-divvy-tripdata.csv')

# display
print("Original input CSV Data: \n")
print(data)



# save to new file without index numbers
#use this one to create new .csv file
#data.to_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTAL.csv',index = False)

#append and save to above file w/o index numbers and headers
#use this one to append 
data.to_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTAL.csv',mode = 'a', header = False,index = False)


newData = pd.read_csv('DataAnalysis/2206-2305-divvy-tripdata/2206-2305-divvy-tripdata-TOTAL.csv')
# display total data
print("Appended input CSV Data: \n")
print(newData)

