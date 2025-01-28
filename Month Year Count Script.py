# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:45:31 2024
@author: Talha
"""

import pandas as pd
import calendar

# Load the uploaded CSV file
file_path = 'E:/2021-12-01_2023-12-03/1PK PAK EPA ISB/1PK_daily_averages.csv'
data = pd.read_csv(file_path)

# Convert 'PKT' column to datetime format
data['PKT'] = pd.to_datetime(data['PKT'])

# Extract year and month from the 'PKT' column
data['Year'] = data['PKT'].dt.year
data['Month'] = data['PKT'].dt.month_name()

# Group by year and month, and count the number of days above the specified PM2.5 levels
year_month_above_35 = data[data['Daily PM2.5'] > 35].groupby(['Year', 'Month']).size().reset_index(name='Days_Above_35')
year_month_above_15 = data[data['Daily PM2.5'] > 15].groupby(['Year', 'Month']).size().reset_index(name='Days_Above_15')

# Create pivot tables for days above 35 and 15 micrograms per cubic meter
pivot_above_35 = data[data['Daily PM2.5'] > 35].pivot_table(index='Year', columns='Month', aggfunc='size', fill_value=0)
pivot_above_15 = data[data['Daily PM2.5'] > 15].pivot_table(index='Year', columns='Month', aggfunc='size', fill_value=0)

# Rename the columns for clarity
pivot_above_35.columns = [f'Days_Above_35_{calendar.month_abbr[i+1]}' for i in range(len(pivot_above_35.columns))]
pivot_above_15.columns = [f'Days_Above_15_{calendar.month_abbr[i+1]}' for i in range(len(pivot_above_15.columns))]

# Merge the two pivot tables on Year
combined_pivot = pivot_above_35.merge(pivot_above_15, left_index=True, right_index=True)

# Define the output file path
output_file_path = 'E:/2021-12-01_2023-12-03/1PK PAK EPA ISB/PM2_5_Days_By_Month_Year.csv'

# Export the combined pivot table to a CSV file
combined_pivot.to_csv(output_file_path)

output_file_path
