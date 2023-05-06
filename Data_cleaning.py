"""
This is a Python script that performs various data cleaning operations on a dataset.
The script uses the pandas library to read the dataset from various file formats including CSV, Excel, JSON, HTML,
Fixed-wordth format and API.
The script also allows the user to remove columns, remove duplicates, fill null values and remove outliers.
"""

import pandas as pd
import requests
import os
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

def get_valid_filename():
    """
    The function prompts the user to input a number indicating the type of file being read
    1. for local file
    2. for API/website
    This function returns the filename or URL entered by the user.
    """
    # Ask user to choose file type
    while True:
        try:
            input_type = int(input('Please insert number.\n1: local file\n2. Url/API\n'))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if input_type == 1:
            while True:
                filename = input("Please enter the filename. \n")
                if os.path.isfile(filename):
                    return filename
                else:
                    print("Invalid filename. Please try again.")
        elif input_type == 2:
            filename = input("Please enter the Website/API url. \n")
            return filename
        # Ask user to select file format again
        else:
            print('Please select 1 or 2. ')

def dataset_format(filename):
    """
    The function prompts the user to enter a number indicating the format of the dataset
    1. csv
    2. Excel (xlsx)
    3. json
    4. HTML
    5. Fixed-wordth format
    6. API

    Returns:
        df (Dataframe)
    """
    while True:
        # Ask the user what format is the dataset
        dataset_format = int(input('Please choose what format your dataset is :\n1. Csv\n2. Excel (Xlsx)\
                                \n3. Json\n4. HTML\n5. Fixed-wordth format\n6. API\n'))
        try:
            if dataset_format == 1:
            # Read CSV
                df = pd.read_csv(filename)
                return df
            # Read Excel Xlsx
            elif dataset_format == 2:
                df= pd.read_excel(filename)
                return df
            # Read JSON
            elif dataset_format == 3:
                df = pd.read_json(filename)
                return df
            # Read HTML
            elif dataset_format == 4:
                df = pd.read_html(filename)
                return df
            # Read Fixed-width format
            elif dataset_format == 5:
                df = pd.read_fwf(filename)
                return df
            # Read API
            elif dataset_format == 6:
                r = requests.get(filename)
                df = pd.read_json(r.text)
                return df
            else:
                print("Please enter a valid number from 1 to 6.")
        # If the user enters a value that cannot be converted to an integer, the user will be asked to input again
        except ValueError:
            print("Something went wrong. Please choose the format of the dataset.")

def column_remove():
    """
    The function prompts the user to enter a number indicating whether to drop a column
    1. for Yes
    2. for No
    if Yes, prompts the user to enter the name of the column(s) to drop.
    The function removes the specified column(s) from the dataframe.
    """
    while True:
        drop_or_no = int(input('Would you like to drop a column? 1 for Yes, 2 for No: '))
        if(drop_or_no == 1):
            rowName = input('enter the columns that want to drop separated by spaces: ')
            rowName_list = list((rowName.split()))
            for name in rowName_list:
                df.drop([name], axis=1, inplace = True)
            break
        else:
            break

def drop_dups():
    """
    function prompts the user to enter a number indicating whether to drop duplicates
    1. for Yes
    2. for No
    If Yes, the function removes duplicates from the dataframe
    """
    while True:
        # Prompt user to input 1 for Yes or 2 for No.
        drop_or_no = int(input('Would you like to drop duplicates?  1 for Yes, 2 for No: '))
        if(drop_or_no == 1):
            # Remove duplicate rows from the DataFrame.
            df.drop_duplicates()
            break
        else:
            break

def null_values(df):
    """
    The function selects only the numeric columns from the dataframe and prompts the user to enter a number
    indicating how to fill null values for each numeric column.
    The function then applies the chosen fill option to null values in each numeric column.
    """                
    # Select only numeric columns
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns

    # Ask user how to fill null values for each numeric column
    fill_options = {}
    for column in numeric_columns:
        while True:
            fill_option = input(f"Enter fill option for column '{column}' (1=Remove row, 2=Replace with mean, 3=Replace with median): ")
            if fill_option in ['1', '2', '3']:
                fill_options[column] = fill_option
                break
            else:
                print("Invalid option. Please try again.")


    # Apply chosen fill options to null values in each numeric column
    for column, fill_option in fill_options.items():
        if fill_option == '1':
            df = df.dropna(subset=[column])
        elif fill_option == '2':
            df[column] = df[column].fillna(df[column].mean())
        else:
            df[column] = df[column].fillna(df[column].median())

def outliers_remove(df):
    """
    The function plots boxplots for each numeric column in the dataframe and prompts the user to enter
    a number indicating whether to remove outliers for each numeric column.
    If Yes, the function removes outliers from the dataframe.
    """
    # Plot boxplots for each numeric column
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns
    for column in numeric_columns:
        plt.boxplot(df[column].dropna())
        plt.title(column)
        plt.show()

    # Ask user to remove outliers for each numeric column
    for column in numeric_columns:
        while True:
            remove_outliers = input(f"Remove outliers for column '{column}'? (y/n): ")
            if remove_outliers in ['y', 'n']:
                break
            else:
                print("Invalid option. Please try again.")
        if remove_outliers == 'y':
            # Calculate lower and upper bounds for outliers
            q1, q3 = df[column].quantile([0.25, 0.75])
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            # Remove outliers from DataFrame
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def export_data_format(df):
    """
    THe function prompts the user to choose a file format to export the dataframe to,
    and then exports the dataframe to the chosen file format
    """
    # Ask user to choose file format
    while True:
        file_format = input("Choose a file format to export (CSV, XLSX, JSON, XML): ").lower()
        if file_format in ['csv', 'xlsx', 'json', 'xml']:
            break
        else:
            print("Invalid option. Please try again.")

    # Ask user to enter file name
    file_name = input("Enter a file name: ")

    # Export DataFrame to chosen file format
    if file_format == 'csv':
        df.to_csv(file_name + '.csv', index=False)
    elif file_format == 'xlsx':
        df.to_excel(file_name + '.xlsx', index=False)
    elif file_format == 'json':
        df.to_json(file_name + '.json', orient='records')
    elif file_format == 'xml':
        df.to_xml(file_name + '.xml', index=False)

if __name__ == "__main__":
    # Get the correct filename / location
    filename = get_valid_filename()
    df = dataset_format(filename)
    print(df.columns)
    column_remove()
    print(df)
    drop_dups()
    null_values(df)
    outliers_remove(df)
    export_data_format(df)
    print(df)
