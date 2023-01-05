import json

# Inventory Database Management#
# Menu and stock inventory .json file is easily amenable via any text editor.
# The below code parses the json database for the first time.
with open('database.json') as json_file:
    menu_items = json.load(json_file)

is_quit = False
item = ''


# Order verification function verifies if the customer's entry if it is acceptable and continuous to loop till valid.
def order_verification(x):
    category_choices = menu_items[x]
    menu_key_list = list(category_choices)
    for key in menu_key_list:
        if category_choices[key]["Stock"] > 0:
            print(f'Please enter {key} for {category_choices[key]["Name"]} ({category_choices[key]["Price"]}aed)')

        else:
            continue

    # prompts the user for the item code.
    query = input("Enter the code number of the item you want to get: ")

    # Input verification and payment logic - customers are prompted till payment amount is sufficient, excess payment
    # will be dispensed as needed.
    if query.upper() in menu_key_list and category_choices[query.upper()]["Stock"] > 0:
        payment = int(input('\nKindly insert your payment amount: '))
        item_cost = category_choices[query.upper()]["Price"]
        print(f'Payment of {payment}aed received.')
        while payment < item_cost:
            payment_add = int(input(f'\nKindly insert {item_cost - payment}aed to complete your payment: '))
            payment += payment_add
        print(f'Change of {payment - item_cost}aed have been dispensed.')

        # Dispensing the order after successful item verification and payment.
        print(f'\nDispensing your {category_choices[query.upper()]["Name"]}...')
        print(f'Enjoy your {category_choices[query.upper()]["Name"]}!!!\n\n\n')

    # Function rerun on invalid entries.
    else:
        print("\nInvalid Entry!")
        order_verification(x)


# Function used in prompting the initial touch point of the customer which enables category selection.
# The function will loop and will only move forward once presented with valid entry.
def order_entry():
    order_type = str(input("\nEnter 1 for Cold Items, 2 for Hot Items, 3 for Sweet Snacks, 4 for Salty Snacks: "))

    if order_type == '1':
        return order_verification('Cold Items')

    elif order_type == '2':
        return order_verification('Hot Items')

    elif order_type == '3':
        return order_verification('Sweet Snacks')

    elif order_type == '4':
        return order_verification('Salty Snacks')
        
    else:
        print('Invalid entry!')
        order_entry()


# The program is continuously run, as it assumes the vending machine is on and will be constantly ready to
# accommodate customer orders.
while not is_quit:
    print("\n\nWelcome to Anne's Mini mart!")
    print("What type of item are you looking for today?")
    order_entry()