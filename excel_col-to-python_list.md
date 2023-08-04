# Converting Excel Column to Python List

## Read Column from CSV
This Python function reads a specific column from a CSV file and returns the data as a list.

## Function Signature
```python
def read_column_from_csv(file_path, column_name):
```
## Parameters

- `file_path (str)`: The file path to the CSV file.
- `column_name (str)`: The name of the column to be retrieved.

## Return Value
Returns a list containing the data from the specified column.

## Example Usage

```python
file_path = "D:\\Mouaaz\\Octopus\\Cloud Engineer - GCP Trainee\\Daily Tasks\\Github\\awesome-opc-resource-python\\TagNames.csv"
column_name = "TagNames"
column_data = read_column_from_csv(file_path, column_name)
print(column_data)
```
## Description
- The function reads the CSV file using the pandas.read_csv() method from the pandas library.
- It checks if the specified column_name exists in the DataFrame's columns using if column_name in df.columns.
- If the column exists, it retrieves the data from the specified column using df[column_name].tolist() and returns it as a list.
- If the column is not found, it prints a message indicating that the column is not present in the CSV file and returns an empty list.
- If an error occurs during reading the CSV file, it prints an error message and returns an empty list.

## Example
Suppose we have a CSV file named `TagNames.csv` with the following data:

```python
file_path = "D:\\Mouaaz\\Octopus\\Cloud Engineer - GCP Trainee\\Daily Tasks\\Github\\awesome-opc-resource-python\\TagNames.csv"
column_name = "TagNames"
column_data = read_column_from_csv(file_path, column_name)
print(column_data)
# Output:
# ['Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5']
```

In this example, the function will read the "TagNames" column from the CSV file and return its data as a list containing `['Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5']`.

