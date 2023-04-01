import openpyxl

def main():
    
    # Load the workbook
    workbook = openpyxl.load_workbook('karios.xlsx')
    
    # Select the sheet you want to work with
    worksheet = workbook['Sheet1']
    
    # Write the value "Mark" to cell A1
    worksheet['A1'] = 'Mark'
    
    # Save the changes to the workbook
    workbook.save('karios.xlsx')
    
    # Read the value from cell A1
    value = worksheet['A1'].value
    
    print(value)
    
    # Iterate through all rows and columns
    for row in worksheet.rows:
        for cell in row:
            print(cell.value)
            
    # Adding a formula 
    worksheet['A2'] = '=SUM(A1,A2)'

    # Save the changes to the workbook
    workbook.save('karios.xlsx')

if __name__ == '__main__':
    main()