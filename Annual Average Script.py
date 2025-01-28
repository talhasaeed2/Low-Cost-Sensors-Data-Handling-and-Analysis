# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:36:13 2024

@author: Talha
"""

import os
import pandas as pd

# Directory containing the Excel files
directory_path = 'C:\\Users\\Talha\\Desktop\\All Stations Hourly Dec2021-Nov2023'

# List all Excel files in the directory
excel_files = [file for file in os.listdir(directory_path) if file.endswith('.xlsx')]

# Initialize a dictionary to store the annual average PM2.5 for each file
annual_averages = {}

# Loop through each Excel file, calculate the annual average PM2.5 for 2023, and store the result
for file_name in excel_files:
    file_path = os.path.join(directory_path, file_name)
    
    # Load the data
    data = pd.read_excel(file_path)
    
    # Convert the 'Timestamp (UTC)' column to datetime format
    data['Timestamp (UTC)'] = pd.to_datetime(data['Timestamp (UTC)'])
    
    # Filter the data for the year 2023
    data_2023 = data[data['Timestamp (UTC)'].dt.year == 2023]
    
    # Calculate the annual average PM2.5 concentration for 2023
    annual_average_pm25_2023 = data_2023['PM2.5 (ug/m3)'].mean()
    
    # Store the result in the dictionary
    annual_averages[file_name] = annual_average_pm25_2023

# Print or process the annual averages as needed
for file_name, average in annual_averages.items():
    print(f"{file_name}: {average} µg/m³")
