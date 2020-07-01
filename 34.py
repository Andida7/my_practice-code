""" *
    **
    ***
    ****
    *****
    ******
    *******
    ********
"""
# Program prints the above pattern
# it has 8 rows
# its columns are increasing downwards from 1 to 8 columns
# number of rows equals number of asteriks in that raw 
# and also equals to the number of columns in each raw

#Create a variable to control the loop
another = 'y'
#proccess one or more times
while another == 'y' or another == 'Y':
    #Get the number of rows
    rows = int(input('Enter the number of rows: '))
    #Get the number of columns
    column = int(input('Enter the number of columns: '))
    #loop through each row
    for r in range(rows):
        for c in range(r+1):
            print('*', end='')
        print()

       

    #check if the user want to continue
    another = input('\nIf you want to continue enter (y):')