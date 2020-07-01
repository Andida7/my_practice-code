"""Write a program that generates a random number in the range of 1 through 100, and asks 
the user to guess what the number is. If the user’s guess is higher than the random number, 
the program should display “Too high, try again.” If the user’s guess is lower than the
random number, the program should display “Too low, try again.” If the user guesses the 
number, the application should congratulate the user and generate a new random number 
so the game can start over.
Optional Enhancement: Enhance the game so it keeps count of the number of guesses that 
the user makes. When the user correctly guesses the random number, the program should 
display the number of guesses."""

"""
STEPS
- should generate a random number between 1 and 100
- ask the user 
- if guess is high say high
- if guess is low say low
- count the guesses made 
FUNCTIONS
-main
-random_num
-dispaly 
"""
import random
#create a main function 
def main():
    print('We created a random number between 1 and 20, try guessing it.')
    num = random_num()
    guess(num)

def guess(num):
    stop = 'y'
    count = 0
    while stop == 'y' or stop == 'Y':

        guess = int(input("Enter your guess: "))
    
        if guess > num:
            print('Too high, try again.')
            count+=1   
            continue
            
        elif guess < num:
            print('Too low, try again.')  
            count+=1   
            continue
                
        elif guess == num:
            if count == 0:
                print('Congrats! You get it immidietly.')
            else:    
                print('Congrats! You get it after',count+1, 'guesses.')
            stop = input("Enter 'y' if you want to play again: ")
            if stop == 'y' or stop == 'Y':
                count = 0
                num = random_num()
                print('We again created a random number between 1 and 20, try guessing it.')
                continue
            else: break
          

#create a random number
def random_num():
    num = random.randint(1,20)
    return num


main()