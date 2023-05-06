# Data Cleaning Python Script

This Python script is designed to clean and transform data in CSV files. The script is built using the pandas library, which allows the user to read CSV files as well as other file formats like Excel, JSON, HTML, fixed-wordth format, and API. The script enables the user to perform various cleaning operations such as removing columns, removing duplicates, filling null values, and removing outliers.

## Getting Started

To run the script, follow these steps:

1.  Clone the repository to your local machine.
2.  Install the required dependencies by running the command `pip install matplotlib`, `pip install os`, `pip install requests`, and `pip install pandas`
3.  Run the script using a command-line interface.

## Usage

To use the script, follow the instructions below:

1.  Run the script in a Python environment such as Jupyter Notebook, Google Colab, or any other Python environment of your choice.
2.  The script will prompt you to input a number indicating the type of file being read.
3.  Enter 1 for a local file or 2 for an API/website.
4.  If you entered 1, enter the filename. If you entered 2, enter the website/API URL.
5.  The script will then prompt you to choose the format of your dataset by inputting a number.
6.  Enter the number corresponding to the format of your dataset as follows:
    1.  CSV
    2.  Excel (Xlsx)
    3.  JSON
    4.  HTML
    5.  Fixed-width format
    6.  API
7.  The script will read the file and output a pandas DataFrame.
8.  The script will then prompt you to choose whether to drop a column.
9.  Enter 1 to drop a column or 2 to keep all columns.
10.  If you entered 1, the script will prompt you to enter the name of the column(s) to drop.
11.  The script will then remove the specified column(s) from the DataFrame.
12.  The script will prompt you to choose whether to drop duplicates.
13.  Enter 1 to drop duplicates or 2 to keep all rows.
14.  If you entered 1, the script will remove duplicates from the DataFrame.
15.  The script will prompt you to choose how to fill null values for each numeric column.
16.  Enter 1 to remove the row, 2 to replace with the mean, or 3 to replace with the median.
17.  The script will then apply the chosen fill option to null values in each numeric column.
18.  Finally, the script will output the cleaned DataFrame which can be exported to either csv, xlsx, txt or json.

