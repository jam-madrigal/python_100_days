MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0.0
}

# My solution
def list_resources(stock):
    for resource in stock:
        print(resource, stock[resource])

def compare_resources(drink, stock):
    ingredients = MENU[drink]['ingredients']
    for ingredient in ingredients:
        if stock[ingredient] < ingredients[ingredient]:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
    for ingredient in ingredients:
        stock[ingredient] -= ingredients[ingredient]
    return True
# TODO: 1. Prompt user by asking what they would like, espresso/latte/cappuccino
def make_drink():
    selection = input('What would you like to drink? Enter "espresso", "latte", or "cappuccino".\n').lower()
    if selection not in MENU:
        if selection == 'off':
            return
        elif selection == 'report':
            list_resources(resources)
            make_drink()
        else:
            print('Sorry, that was an invalid selection. Try again')
            make_drink()
    # TODO: 2. Check the users input to decide what to do next
    # After the user chooses a drink, check that there are enough resources to make it
    enough_ingredients = compare_resources(selection, resources)
    # if there are not enough, print 'sorry not enough {resource}' and should restart the prompt
    if not enough_ingredients:
        make_drink()
    # if there are enough resources, then prompt the user to enter coins, quarters, dimes, nickels, pennies
    quarters = int(input('Input the amount of quarters:\n')) * 0.25
    dimes = int(input('Input the amount of dimes:\n')) * 0.10
    nickels = int(input('Input the amount of nickels:\n')) * 0.05
    pennies = int(input('Input the amount of pennies:\n')) * 0.01
    # calculate the total value of the inserted coins
    total_payment = quarters + dimes + nickels + pennies
    # check that enough money for the drink was inserted, if not, 'sorry that's not enough money, money refunded'
    drink_price = MENU[selection]['cost']
    if total_payment < drink_price:
        print ('Sorry, that\'s not enough money. Money refunded.')
        make_drink()
    # if it was enough, add the cost of the drink to the resources as a money value, shows when report is triggered
    resources['money'] = round(resources['money'] + drink_price, 2)
    # if the user put in too much money, give them change (deduct drink cost from added money, return rest), rounded to 2 decimals 'here is {} in change
    change = round(total_payment - drink_price, 2)
    # deduct the made drink resources from the resources <- done in the function
    if change != 0:
        print(f'Here is your change of {change}.')
    # tell the user here is your drink, enjoy
    print(resources)
    make_drink()
    # TODO: 3. Every time the sequence is completed, it should prompt the user again
    # TODO: 4. 'off' as a secret word can be used to turn off the machine
    # TODO: 5. When the user enters 'report', a report should show the current resources and their values
make_drink()