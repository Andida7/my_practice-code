"""Repeat 10 times:
If a random number in the range of 1 through 2 equals 1 then:
Display ‘Heads’
Else:
Display ‘Tails"""

#import the random module
import random
#create a variable to control the loop
again = 'y'
#start the loop
while again == 'y' or again == 'Y':
    #ask the user how many times they want to toss the coin
    toss = int(input('How many times do you want to toss the coin? '))
    #toss the coin 
    for i in range(toss):
        #create a random number either 0 or 1
        random_num = random.randint(0,1)
        #check if the face up is tail or head
        if random_num == 1:
            print('Head')
        else:
            print('Tail')    
    #check if the user wants to toss again
    again = input('Do you want to toss again?(Enter "y" to continue) ')
        