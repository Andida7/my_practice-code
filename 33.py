# This program prints a pattern 
# of rows and columns entered by the user

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
        for c in range(column):
            #print * for each iteration
            print(c,end='')
        print()

    #check if the user want to continue
    another = input('\nIf you want to continue enter (y):')
