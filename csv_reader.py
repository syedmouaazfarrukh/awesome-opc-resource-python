import pandas as pd

def read_column_from_csv(file_path, column_name):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path) 

        # Check if the column exists in the DataFrame
        if column_name in df.columns:
            # Retrieve the column as a list
            column_data = df[column_name].tolist()
            return column_data
        else:
            print(f"Column '{column_name}' not found in the CSV file.")
            return []
    except Exception as e:
        print(f"Error occurred while reading the CSV file: {e}")
        return []

 

# Example usage
file_path = "D:\\\\Mouaaz\\\\Octopus\\\\Cloud Engineer - GCP Trainee\\\\Daily Tasks\\\\Github\\\\awesome-opc-resource-python\\\\TagNames.csv"
column_name = "TagNames"
column_data = read_column_from_csv(file_path, column_name)
print(column_data)