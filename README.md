# CSV2Excel Processor

CSV2Excel Processor is a Python script that efficiently processes multiple CSV files, filters records based on specified criteria, and saves the filtered data into multiple Excel files. Each output file can contain a maximum number of records, making it easier to manage and analyze large datasets.

## Features

- **Batch Processing**: Read and process multiple CSV files in one go.
- **Dynamic Filtering**: Filter records based on a specific column (e.g., `src_sys`) and a defined value.
- **Custom File Splitting**: Split filtered data into multiple Excel files, each with a defined maximum record limit (e.g., 500,000).
- **User-Friendly Output**: Output Excel files are named sequentially (e.g., `File_1.xlsx`, `File_2.xlsx`), making them easy to organize.

## Requirements

- Python 3.x
- Pandas library
- OpenPyXL library

You can install the required libraries using pip:

```bash
pip install pandas openpyxl

## Usage

Clone the Repository:

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/csv2excel-processor.git
cd csv2excel-processor

##Set Up Your CSV Files:

Ensure you have your CSV files stored in a specific directory. Update the script to point to this directory.

## Modify the Script:

- Open the csv_to_excel.py file in a text editor and locate the following sections:

- Specify the Input Files: Update the path to your CSV files:

```python
input_files = glob.glob('path/to/your/csv/files/*.csv')
Set the Filter Value: Specify the value you want to filter by in the src_sys column:

```python
filter_value = 'your_filter_value'  # Replace with your actual filter value
Run the Script:

-Execute the script using Python from your terminal:

```bash
python csv_to_excel.py
Check the Output:

After the script runs, check the directory for the generated Excel files, named File_1.xlsx, File_2.xlsx, and so on. Each file will contain the filtered records, limited to the specified number of records per file.

## Example
If you have multiple CSV files and want to filter records where the src_sys column equals your_filter_value, the script will generate sequentially named Excel files containing the relevant data.

## Troubleshooting
- File Not Found Error: Ensure that the path to your CSV files is correct.
- Column Not Found: Make sure the column name you are filtering by (e.g., src_sys) exists in your CSV files.
- Memory Issues: If processing large datasets, consider using a machine with sufficient RAM or optimizing the code for chunk processing.
