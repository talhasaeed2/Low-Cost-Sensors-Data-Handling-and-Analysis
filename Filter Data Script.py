# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:31:15 2024

@author: Talha
"""
import pandas as pd

# Load the CSV file
csv_file_path = 'D:\\DUKE USA\\Data Pull out Pakistan\\Our Data\\Pakistan\\2021-12-01_2023-11-30\\41PK- G13 SFCT\\Level1.csv'
data = pd.read_csv(csv_file_path)

# Specify the columns to retain, including the new ones
columns_to_keep = [
    'Timestamp (UTC)', 'PM2.5 (ug/m3)', 'PM10 (ug/m3)',
    'Typical Particle Size (um)', 'Temperature (Celsius)', 
    'Relative Humidity (%)', 'PM2.5 NC (#/cm3)', 'PM10 NC (#/cm3)'
]

# Filter the data
filtered_data = data[columns_to_keep]

# Define the output file path (you can change this to your preferred location)
output_excel_file_path = 'C:\\Users\\Talha\\Documents\\41PK Raw.xlsx'
# Save to Excel without the index
filtered_data.to_excel(output_excel_file_path, index=False)

print(f'Filtered data saved to {output_excel_file_path}')



