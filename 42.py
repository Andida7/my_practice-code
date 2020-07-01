""" Write a program that generates 100 random numbers 
and keeps a count of how many of those random numbers are even, and how many of 
them  are odd. """
"""
STEPS
- create a random 100 number
        - import random module 
        - use randint function 
- every time the number is created check if its odd or even
- count it every time after its checked
- display it
FUNCTONS
- main
- count
- display
"""
import random

def main():
    #lets initialize even and odd variables

    even = 0
    odd = 0
    #create a random num
    for i in range(0,100):
        num = random.randint(0,100)
        if count(num) == True:
            even+=1
        else:
            odd+=1    

    #display 
    display(even, odd)            

#co(unt the even and the odd ones
def count(num):
    if num % 2 == 0:
        return True
    else:
        return False

#create display function
def display(e,o):
    print('There are ', str(o), 'odd numbers.')     
    print('There are ', str(e), 'even numbers.')

main()       