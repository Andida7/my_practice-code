"""Designing a Program with a while Loop
A project currently underway at Chemical Labs, Inc. 
requires that a substance be continually heated in a vat. 
A technician must check the substance’s temperature every 15 minutes. 
If the substance’s temperature does not exceed 102.5 degrees Celsius, then the technician 
does nothing. However, if the temperature is greater than 102.5 degrees Celsius, 
the technician must turn down the vat’s thermostat, wait 5 minutes, and check the temperature again. 
The technician repeats these steps until the temperature does not exceed 102.5 degrees 
Celsius. The director of engineering has asked you to write a program that guides the 
technician through this process."""
#The algorithm looks like this
#1. get the substance's temprature
#2. repeat the following steps as long as the temprature is greater than 102.5
    #a. tell the technicain to lower down the temprature and wait for 5 minutes.
    #b. check the temprature again 
#3. if the temp is less than 102.5 , tell him to check again in 15 minutes 

#create a named costant to present the maximum
LIMITING_TEMP = 102.5
#prompt the guy to enter the temprature
current_temp = float(input('Enter the temprature: '))
#loop as long as the condition is true
while current_temp > LIMITING_TEMP:
    print('Lower down the temp'\
        'and wait for 5 minutes')
    current_temp = float(input('Enter the temprature: '))
#Remind him to check every 15 minutes
print('Acceptable temprature. Check the temprature every 15 minutes')    

