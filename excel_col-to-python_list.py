import openpyxl

def excel_column_to_list(excel_file, sheet_name, column_name):
    # Load the Excel file
    workbook = openpyxl.load_workbook(excel_file)

    # Select the worksheet by name
    sheet = workbook[sheet_name]

    # Find the column index based on the column name (assuming it's in the first row)
    column_index = None
    for cell in sheet[1]:
        if cell.value == column_name:
            column_index = cell.column
            break

    if column_index is None:
        raise ValueError(f"Column '{column_name}' not found in the Excel sheet.")

    # Extract the values from the specified column and convert them to a list of strings
    column_values = [str(cell.value) for cell in sheet[column_index]]

    return column_values

if __name__ == "__main__":
    excel_file = "tag-names.xlsx"
    sheet_name = "tag-names"
    column_name = "TagName"

    try:
        column_list = excel_column_to_list(excel_file, sheet_name, column_name)
        print(column_list)
    except Exception as e:
        print(f"Error: {e}")
