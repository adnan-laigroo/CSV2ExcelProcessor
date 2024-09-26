import pandas as pd
import glob

# Specify the path to your CSV files (change the path as needed)
input_files = glob.glob('path/to/your/csv/files/*.csv')

# List to hold all DataFrames
all_data = []

# Load all CSV files into a list of DataFrames
for file in input_files:
    df = pd.read_csv(file)
    all_data.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(all_data, ignore_index=True)

# Filter the DataFrame based on the src_sys column
filter_value = 'your_filter_value'  # Replace with your actual filter value
filtered_df = combined_df[combined_df['src_sys'] == filter_value]

# Number of records per Excel file
records_per_file = 500000

# Calculate number of chunks
num_chunks = (len(filtered_df) // records_per_file) + (1 if len(filtered_df) % records_per_file > 0 else 0)

# Loop to create each Excel file
for i in range(num_chunks):
    # Determine the start and end indices for the chunk
    start_index = i * records_per_file
    end_index = min(start_index + records_per_file, len(filtered_df))  # Ensure end_index does not exceed DataFrame length

    # Slice the DataFrame to get the chunk
    chunk = filtered_df[start_index:end_index]

    # Save the chunk to an Excel file with the desired naming format
    output_file = f'File_{i + 1}.xlsx'
    chunk.to_excel(output_file, index=False)

    print(f'Saved {output_file} with {len(chunk)} records.')
