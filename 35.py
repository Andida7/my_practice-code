"""
Write a program that predicts the approximate size of a population of organisms. The 
application should use text boxes to allow the user to enter the starting number of organisms, 
the average daily population increase (as a percentage), and the number of days the 
organisms will be left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:
    Day Approximate Population
    1  2 
    2  2.6
    3  3.38
    4  4.394
    5  5.7122
    6  7.42586
    7  9.653619
    8  12.5497
    9  16.31462
    10 21.209
"""
#get number of starting orgamisms
organism_num = int(input('Starting number of organisms: '))
#get avarage daily increase
increament = float(input('Avarage daily increase: ')) 
#get number of days to multiply
multiplication_day = int(input('Number of days to multiply: '))
#printing the columns of the data
print('Day Approximate', 'Population', sep=' ')
#lets loop     
for days in range(multiplication_day):
    organism_num += organism_num*increament
    print(days+1, format(organism_num, '16.4f'))