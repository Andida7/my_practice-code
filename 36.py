
"""While the user wants to roll the dice:
        Display a random number in the range of 1 through 6
        Display another random number in the range of 1 through 6
        Ask the user if he or she wants to roll the dice again  """

#Importing the random module
import random
#Create a variable that controls the loop
another = 'y'
#Ask the user if they want to roll the dice
another = input('Do you want to roll the dice?(Enter "y" to continue): ')
#Start the loop
while another == 'y' or another == 'Y':
    
    #roll the dice twice
    for s in range(2):
        print('Rolling the dice...')
        #generating random faces
        print('The number facing up: ',  random.randint(1, 6))
    #asking the user if they want to continue    
    another = input('Do you want to roll the dice again?(Enter "y" to continue): ')    

