#This program calculates retail prices.

MARK_UP = 2.5 #the mark up percentage
another = 'y' # variable to control the loop

#process one or more items.
while another == 'y' or another == 'Y':
    ## Get the item's wholesale cost.
    wholesale = float(input("Enter the item's " + 
                            "wholesale cost: "))
    #validate the wholesale cost                       
    while wholesale < 0:
        print("Error! Wholesale cost can't be negative.")
        wholesale = float(input("Enter the item's " + 
                            "wholesale cost: "))

    # Calculate the retail price.
    retail = wholesale * MARK_UP
    # Display the retail price.
    print('Retail price: $', format(retail, ',.2f'), sep='')
    # Do this again?
    another = input('Do you have another item? ' + 
                    '(Enter y for yes): ')                       