#importing random module 
import random

def main():
    #toss the coin
    tossing()
    #check if the user wants to toss again
    another()

#A function that simulates tossing    
def tossing():
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

def another():              
    #check if the user wants to toss again
    again = input('Do you want to toss again?(Enter "y" to continue) ')
    while again == 'y' or again == 'Y':
        tossing()
        again = input('Do you want to toss again?(Enter "y" to continue) ') 
#call the main function
main()