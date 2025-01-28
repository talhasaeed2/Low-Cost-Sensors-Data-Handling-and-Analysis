# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:43:35 2024

@author: Talha
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import pytz

# Function to convert UTC to GMT+5 and plot the data
def convert_and_plot(csv_file_path):
    # Load the dataset
    data = pd.read_csv(csv_file_path)

    # Convert the 'Timestamp (UTC)' to datetime objects assuming they are in UTC
    data['Timestamp (UTC)'] = pd.to_datetime(data['Timestamp (UTC)'], utc=True)

    # Convert the timestamp from UTC to GMT+5
    data['Timestamp (GMT+5)'] = data['Timestamp (UTC)'].dt.tz_convert(pytz.timezone('Asia/Karachi'))

    # Set the adjusted timestamp as the index of the DataFrame
    data.set_index('Timestamp (GMT+5)', inplace=True)

    # Plotting the time series of 'PM2.5 (ug/m3)'
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['PM2.5 (ug/m3)'], label='PM2.5 Concentration', color='purple')
    plt.title(f"PM2.5 Concentration Over Time - {os.path.basename(csv_file_path)}")
    plt.xlabel('Time (GMT+5)')
    plt.ylabel('PM2.5 (ug/m3)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Main directory containing all subdirectories
main_directory = 'D:\\DUKE USA\\Data Pull out Pakistan\\Our Data\\Pakistan\\2021-12-01_2023-11-30\\'

# Walk through the main directory
for root, dirs, files in os.walk(main_directory):
    for file in files:
        # Process only 'Level1.csv' files
        if file == 'Level1.csv':
            # Generate the full path to the CSV file
            csv_file_path = os.path.join(root, file)
            # Convert to GMT+5 and plot
            convert_and_plot(csv_file_path)
