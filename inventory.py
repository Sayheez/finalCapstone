class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 

    def get_cost(self):
        return self.cost 

    def get_quantity(self):
        return self.quantity

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_code(self):
        return self.code

    def get_name(self):
        return self.product

    def __str__(self):
        print(f'''
                Country = {self.country}
                Code = {self.code}
                Product = {self.product}
                Cost = {self.cost}
                Quantity = {self.quantity}
        ''')



#=============Shoe list===========
# Initialise an empty Shoe list
shoe_list = []

#==========Functions outside the class==============

# function to read shoe list from a file
def read_shoes_data():
    shoe_list = [] 
    file_inv = 'inventory.txt'
    f = open(file_inv, 'r') 

    # An empty string variable named contents to store file contents 
    contents = ""                  

    for line in f:
        contents += line

    line_list = contents.split("\n")   
    del(line_list[0])                    
    combine_lists = []

    for line in range(0, len(line_list)):
        combine_lists.append(line_list[line].split(","))

    try:
        for line in range(0, len(combine_lists)) : 
            object_data = Shoe(combine_lists[line][0], combine_lists[line][1], combine_lists[line][2], combine_lists[line][3], combine_lists[line][4])
            shoe_list.append(object_data)
    except ValueError :
        raise Exception("Invalid data format. Please input title as the first line of the file.")

    f.close()
    return shoe_list

# function to add a shoe to the file
def capture_shoes():

    country = input("Enter the country that the shoe is from: ")
    code = input("Enter code of the shoe: ")
    product = input("Enter the name of the product: ")
    cost = input("Enter the cost of shoe: ")
    quantity = int(input("Enter the quantity you want: "))

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print(f'''
            Task complete: new shoe added! 
            Country = {country}
            Code = {code}
            Product = {product}
            Cost = {cost}
            Quantity = {quantity}
    ''')

    file = open('inventory.txt', 'a')
    file.write(f'''\n{country},{code},{product},{cost},{quantity}''')
    file.close()

# function to view or display all shoes from a file
def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    shoe_list = read_shoes_data()
    for shoe in range(0, len(shoe_list)) :
        shoe_list[shoe].__str__()

# function to restock shoe 
def re_stock():

    qty_list = []  

    shoe_list = read_shoes_data()

    for index in range(0, len(shoe_list)):
        qty_list.append(int(shoe_list[index].get_quantity()))  #...using our get quantity method

    lowest_qty= min(qty_list)
    lowest_qty_index = int(qty_list.index(lowest_qty))  #now find the index of the lowest one

    print("The shoe with the lowest quantity is: ")
    shoe_list[lowest_qty_index].__str__()

    user_choice = input('Would you like to restock it? Y/N').lower()

    if user_choice == 'y' :
        new_qty = int(input("After restocking, please enter the quantity of this shoe you would like to record for the database: "))

        shoe_list[lowest_qty_index].change_quantity(new_qty)
        print(f"Task complete! The new quantity value is: {shoe_list[lowest_qty_index].get_quantity()}")

        

        f = open('inventory.txt', 'w') 

        new_contents = "Country,Code,Product,Cost,Quantity"           #this will create our new contents string and add our first line, which is always the same.

        for shoe in range(0, len(shoe_list)):
            new_contents += shoe_list[shoe].original_details()         #this will add all the shoe objects' details back, in the same format as before, but with our updated stock value of course

        f.write(new_contents)

        print(f'Task complete, please check inventory.txt for the updated details.')

        f.close()

    elif user_choice == 'n' :
        print("Thanks!")

# function to search available shoe from a file
def search_shoe():
    shoe_list = read_shoes_data()
    code_list = []

    for i in range(0, len(shoe_list)): 
        code_list.append(shoe_list[i].get_code())   #now we have a list of codes

    code_input = input("Please enter the code you would like to search for: ")

    if code_input in code_list :
        for index in range(0, len(code_list)) :   
            if code_list[index] == code_input : 
                searched_shoe = shoe_list[index]                   
    else : 
        raise Exception("The code you searched for does not exist. Try again!.")

    print(f'The shoe you searched for was: ')
    searched_shoe.__str__()
    print('Task Complete!')

# function to find the cost of a shoe from a file
def value_per_item():
    shoe_list = read_shoes_data()

    shoe_values = [] 
    shoe_names = []

    for shoe in range(0,len(shoe_list)): 
        shoe_values.append(int(shoe_list[shoe].get_quantity()) * int(shoe_list[shoe].get_cost()))
        shoe_names.append(shoe_list[shoe].get_name())

    values_dict = {}

    for index in range(len(shoe_names)):
        key = shoe_names[index]
        value = shoe_values[index]

        print(f'{key} : {str(value)} dollars')
        values_dict[key] = value


    user_choice = input('Do you want to get the price of an individual product, by name? Y/N: ').strip(" ").lower()

    if user_choice == 'y' :
        user_choice = input("Please enter the name of the shoe you wantt to view the price for: ").strip(" ")
        try: 
            print(f' The price of {user_choice} is: {values_dict[user_choice]}')
        except KeyError:
            print("Sorry, No such shoe found. Please try again.")
    elif user_choice == 'n': 
        print("Task complete. Thanks.")
  
# function to find the highest quantity shoe from a file
def highest_qty():

    qty_list = []
    shoe_list = read_shoes_data()

    for i in range(0, len(shoe_list)):
        qty_list.append(int(shoe_list[i].get_quantity()))

    maximum_index = qty_list.index(max(qty_list))


    print(f'''The shoe with the greatest quantity is {shoe_list[maximum_index].get_name()}:''')

    shoe_list[maximum_index].__str__()

    print(' This shoe is for sale! ')


#==========Main Menu=============

def main():
    while True:
        menu = input('''
            Please choose from the following options below:           
                                                                                                    
            1 - capture shoes (add a new product description to the database)                         
            2 - view all products in the database                                                      
            3 - re-stock the lowest-stocked shoe on the database                                       
            4 - search for details of a given shoe on record                                           
            5 - browse the value of the products in stock                                              
            6 - view the shoe with the highest quantity on record currently                            
            e - exit                                                                                   
                                                                                              
    ''').strip(" ").lower()

        if menu == '1' :
            capture_shoes()
        elif menu == '2' :
            view_all()
        elif menu == '3' :
            re_stock()
        elif menu == '4' :
            search_shoe()
        elif menu == '5' :
            value_per_item()
        elif menu == '6' :
            highest_qty()
        elif menu == 'e' :
            print("Goodbye!")
            break
        else: 
            print("Please kindly use the options display to enter a command!")


main()