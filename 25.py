"""Enter data for five phones.
Phone number 1:
Enter the manufacturer: Acme Electronics Enter
Enter the model number: M1000 Enter
Enter the retail price: 199.99 Enter
Phone number 2:
Enter the manufacturer: Atlantic Communications Enter
Enter the model number: S2 Enter
Enter the retail price: 149.99 Enter
"""

#creating class that can store cel phone info
class Cel_phone:
    #Initializing the class
    def __init__(self, manufacturer, model_number, retail_price):
        self.__manufacturer = manufacturer
        self.__model = model_number
        self.__retail_price = retail_price
    #Create a method that can uppdate the manufacturer
    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer
    #Create a method that can uppdate the model number
    def set_model(self, model_number):
        self.__model = model_number
    #Create a method that can uppdate the retail price  
    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
    #Display the manufacturer
    def get_manufacturer(self):
        return self.__manufacturer
    #Display the model
    def get_model(self):
        return self.__model
    #Display the retail price
    def get_retail_price(self):
        return self.__retail_price    

def Main():
    print('Enter data for five phones.')
    phoness = make_list()
    print('Here is the data that you entered:')
    Display_list(phoness)        

#Main function
def make_list():
    cel_phone_list = list()
    #lets get the three objects
    
    for i in range(1,4):
        #Displaying every phone to have data being stored
        print("Phone number ", str(i))
        #lets get the manufacturer
        manufacturer = input('Enter the manufacturer: ')
        #lets get the model number
        model = input('Enter the model number: ')
        #lets get the retail price
        retail_price = input('Enter the retail price: ')
        print()
        #Creating an object
        phones = Cel_phone(manufacturer, model, retail_price)
        cel_phone_list.append(phones)
    return cel_phone_list

def Display_list(cel_phone_list):
    #Display the data
    for phone in cel_phone_list:
        #Display the manufacturer
        print(phone.get_manufacturer())
        #Display the manufacturer
        print(phone.get_model())
        #Display the manufacturer
        print(phone.get_retail_price())
        print()

#calling the function

Main()