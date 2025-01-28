import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the directory where your Excel files are located
excel_directory = 'D:\\DUKE USA\\Filtering Out Data 2023\\'

# List all Excel files in the directory
excel_files = [f for f in os.listdir(excel_directory) if f.endswith('.xlsx')]


# Loop through all Excel files and plot the PM2.5 time series
for excel_file in excel_files:
    # Create the full path to the Excel file
    excel_file_path = os.path.join(excel_directory, excel_file)
    
    # Load the Excel file into a DataFrame
    data = pd.read_excel(excel_file_path)
    
    # Convert the 'Timestamp (UTC)' to datetime objects
    data['PKT'] = pd.to_datetime(data['PKT'])
  
    # Set the 'Timestamp (GMT+5)' as the index of the DataFrame
    data.set_index('PKT', inplace=True)
    
    # Plot the 'PM2.5 (ug/m3)' time series
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['PM2.5 (ug/m3)'], label=f'PM2.5 - {excel_file}')
    
    # Add title and labels
    plt.title(f'PM2.5 Concentration Time Series - {excel_file}')
    plt.xlabel('PKT')
    plt.ylabel('PM2.5 (ug/m3)')
    
    # Show legend
    plt.legend()
    
    # Show the plot
    plt.show()
