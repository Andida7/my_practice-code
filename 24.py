import bankaccount

def main():

    #lets get the starting balance
    starting_balance = float(input('What is your starting balance: '))

    #lets create an object from the Bankaccount class
    savings = bankaccount.BankAccount(starting_balance)

    #now lets deposite 
    payment = float(input('What is the ammunt of your payment: '))
    print('Adding to your balance...')
    savings.deposit(payment)

    #Display the balance
    #print('Your balance is: ', savings.get_balance())
    print(savings)
    #withdraw an amount from the balance
    withdraw = float(input('How much to withdraw: '))
    print('Withdrawing some amount... ')
    savings.withdraw(withdraw)
    
    #Display the balance
    
    #print('Your net balance is now: ', savings.get_balance())
    print(savings)
#Call the main function
main()


