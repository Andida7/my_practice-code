""" Enter the amount of sales: 10000.00
    Enter the commission rate: 0.10 
    The commission is $1,000.00
    Do you want to calculate another commission (Enter y for yes): y
    """
#first lets create a controler loop
keep_going = 'y'
#lets get series of inputs 
while keep_going == 'y':
    #lets get the sales
    sales = float(input('Enter the amount of sales: '))
    #lets get the commmison rate 
    commission_rate = float(input('Enter the commision rate: '))
    #lets calculate the commision
    commission = sales * commission_rate
    #lets display the commmision  
    print('The commision is $', format(commission , ',.2f') , sep='')
    #lets see if the user wants to continue 
    keep_going = input('Do you want to calculate another commision (Enter y for yes and n for no):')