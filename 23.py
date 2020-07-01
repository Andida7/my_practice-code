import coinn

#The main function
def main():
   #lets create 3 instances from Coin class
   coin1 = coinn.Coin()
   coin2 = coinn.Coin()
   coin3 = coinn.Coin()
   #Displaying the facing up...
   print('The facing up before tossing happened.')
   print('coin1: ', coin1.get_sideup())
   print('coin2: ', coin2.get_sideup())
   print('coin3: ', coin3.get_sideup())
   
   #Now lets toss them.
   print('I am tossing them...')
   coin1.toss()
   coin2.toss()
   coin3.toss()
   #Displaying the facing up...
   print('The facing up after tossing happened.')
   print('coin1: ', coin1.get_sideup())
   print('coin2: ', coin2.get_sideup())
   print('coin3: ', coin3.get_sideup())


main()
