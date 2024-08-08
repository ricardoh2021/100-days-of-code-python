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
}

cash_register_money = 0.0


def get_report():
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${cash_register_money}")

def get_coffee_resources(coffeeType):
    coffee = MENU.get(coffeeType)
    ingredient_list = coffee.get('ingredients')
    water = ingredient_list.get('water')
    milk = ingredient_list.get('milk', 0)
    coffee_amount = ingredient_list.get('coffee')

    return water, milk, coffee_amount
def check_resources(coffeeType):
    water, milk, coffee_amount = get_coffee_resources(coffeeType)

    if water > resources.get('water'):
        print("Sorry there is not enough water.")
    elif coffee_amount > resources.get('coffee'):
        print("Sorry there is not enough coffee.")
    elif milk > resources.get('milk'):
        print("Sorry there is not enough milk.")
    else:
        return True
    return False

def process_coins(coffeeType):
    global cash_register_money
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            if quarters < 0:
                raise ValueError
            quarters *= 0.25
            break
        except ValueError:
            print("Please enter a valid non-negative integer for quarters.")

    while True:
        try:
            dimes = int(input("How many dimes?: "))
            if dimes < 0:
                raise ValueError
            dimes *= 0.10
            break
        except ValueError:
            print("Please enter a valid non-negative integer for dimes.")

    while True:
        try:
            nickels = int(input("How many nickels?: "))
            if nickels < 0:
                raise ValueError
            nickels *= 0.05
            break
        except ValueError:
            print("Please enter a valid non-negative integer for nickels.")

    while True:
        try:
            pennies = int(input("How many pennies?: "))
            if pennies < 0:
                raise ValueError
            pennies *= 0.01
            break
        except ValueError:
            print("Please enter a valid non-negative integer for pennies.")

    total = quarters + dimes + nickels + pennies

    coffeePrice = MENU.get(coffeeType).get("cost")

    if total < coffeePrice:
        print("Sorry that's not enough money. Money Refunded.")
    elif total > coffeePrice:
        #give change.
        change = round(total - coffeePrice, 2)
        print(f"Here is ${change} in change.")
        cash_register_money += coffeePrice
        return True
    return False

def create_coffee(coffeeType):
    water, milk, coffee_amount = get_coffee_resources(coffeeType)
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee_amount

    print(f"Here is your {coffeeType}. Enjoy!☕️")

def coffee_machine():
    while True:
        ##Ask the user what they want to drink
        coffeeType = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if coffeeType == "off":
            # Turn off machine.
            print("Secret Key accepted. Turning off coffee machine...")
            exit()
        while coffeeType not in ['espresso', 'latte', 'cappuccino', 'report']:
            coffeeType = input(
                "Invalid Input. Please try again.\nWhat would you like? (expresso/latte/cappuccino): ").strip().lower()

        if coffeeType == "report":
            get_report()
        else:
            can_create_coffee = check_resources(coffeeType)
            if can_create_coffee:
                ##Ask for coins
                is_valid_amount = process_coins(coffeeType)
                if is_valid_amount:
                    # Deplete the resources.
                    create_coffee(coffeeType)

coffee_machine()