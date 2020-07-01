"""A prime number is a number that is only evenly divisible by itself and 1. For example, the 
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, 
is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and 
returns true if the argument is a prime number, or false otherwise. Use the function in 
a program that prompts the user to enter a number then displays a message indicating 
whether the number is prime."""


def main():
    num = int(input('Enter the number: '))
    if is_prime(num) > 0:
        print(num, 'is not prime.')
    else:
        print(num, 'is prime.')    


def is_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count+=1
    return count

main()
