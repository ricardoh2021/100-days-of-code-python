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
    """Prints a report of the current resources and cash register money."""
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${cash_register_money}")


def get_coffee_resources(coffeeType):
    """
    Retrieves the necessary ingredients for the selected coffee type.

    Args:
        coffeeType (str): The type of coffee to be made.

    Returns:
        tuple: A tuple containing the required water, milk, and coffee amounts.
    """
    coffee = MENU.get(coffeeType)
    ingredient_list = coffee.get('ingredients')
    water = ingredient_list.get('water')
    milk = ingredient_list.get('milk', 0)
    coffee_amount = ingredient_list.get('coffee')

    return water, milk, coffee_amount


def check_resources(coffeeType):
    """
    Checks if there are sufficient resources to make the selected coffee type.

    Args:
        coffeeType (str): The type of coffee to be made.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
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
    """
    Processes coin input from the user and checks if the amount is sufficient to purchase the selected coffee.

    Args:
        coffeeType (str): The type of coffee to be purchased.

    Returns:
        bool: True if the amount is sufficient, False otherwise.
    """
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
        change = round(total - coffeePrice, 2)
        print(f"Here is ${change} in change.")
        cash_register_money += coffeePrice
        return True
    return False


def create_coffee(coffeeType):
    """
    Deducts the necessary resources to make the selected coffee and prints a message.

    Args:
        coffeeType (str): The type of coffee to be made.
    """
    water, milk, coffee_amount = get_coffee_resources(coffeeType)
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee_amount

    print(f"Here is your {coffeeType}. Enjoy!☕️")


def coffee_machine():
    """Main function to run the coffee machine, handling user input and operations."""
    while True:
        coffeeType = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if coffeeType == "off":
            print("Secret Key accepted. Turning off coffee machine...")
            exit()
        while coffeeType not in ['espresso', 'latte', 'cappuccino', 'report']:
            coffeeType = input(
                "Invalid Input. Please try again.\nWhat would you like? (espresso/latte/cappuccino): ").strip().lower()

        if coffeeType == "report":
            get_report()
        else:
            can_create_coffee = check_resources(coffeeType)
            if can_create_coffee:
                is_valid_amount = process_coins(coffeeType)
                if is_valid_amount:
                    create_coffee(coffeeType)


coffee_machine()