"""Write another program that displays all of the prime numbers from 1 to 100. 
The program should have a loop that calls the is_prime function."""

def main():
    num1 = int(input('Enter the initial number: '))
    num2 = int(input('Enter the final number: '))
    print('This are the primes in the range (',num1,',',num2,').')
    is_prime(num1, num2)
    


def is_prime(num1, num2):
    count = 0
    prime_count = 0
    for nums in range(num1, num2+1):
        if nums == 1: continue
        for i in range(2, nums):
            
            if nums % i == 0:
                count+=1
        if count == 0:
            
            print(nums, end=' ')
            prime_count+=1

        else:
            count = 0  
    print('\n', end='')          
    print(prime_count, 'prime numbers found.')
    

main()