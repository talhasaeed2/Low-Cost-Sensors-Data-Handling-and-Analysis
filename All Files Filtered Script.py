# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:54:26 2024

@author: Talha
"""

import os
import pandas as pd

# Main directory containing all subdirectories
main_directory = 'D:\\DUKE USA\\Data Pull out Pakistan\\Our Data\\Pakistan\\2021-12-01_2023-11-30'

# Specify the columns to retain
columns_to_keep = [
    'Timestamp (UTC)', 'PM2.5 (ug/m3)', 'PM10 (ug/m3)',
    'Typical Particle Size (um)', 'Temperature (Celsius)',
    'Relative Humidity (%)', 'PM2.5 NC (#/cm3)', 'PM10 NC (#/cm3)'
]

# Walk through the main directory
for root, dirs, files in os.walk(main_directory):
    for file in files:
        # Process only 'Level1.csv' files
        if file == 'Level1.csv':
            # Load the CSV file
            csv_file_path = os.path.join(root, file)
            data = pd.read_csv(csv_file_path)

            # Filter the data
            filtered_data = data[columns_to_keep]

            # Define the output file path (use the name of the parent directory of Level1.csv)
            parent_directory_name = os.path.basename(root)
            output_excel_file_name = f'{parent_directory_name}.xlsx'
            output_excel_file_path = os.path.join('C:\\Users\\Talha\\Documents\\Output', output_excel_file_name)

            # Save to Excel without the index
            filtered_data.to_excel(output_excel_file_path, index=False)

            print(f'Filtered data saved to {output_excel_file_path}')
