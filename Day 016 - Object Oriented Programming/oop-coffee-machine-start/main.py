from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
register = MoneyMachine()

menu = Menu()


while True:
    coffeeType = input(f"What would you like? ({menu.get_items()}): ").strip().lower()
    if coffeeType == "off":
        print("Secret Key accepted. Turning off coffee machine...")
        exit()
    while coffeeType not in ['espresso', 'latte', 'cappuccino', 'report']:
        coffeeType = input(
            "Invalid Input. Please try again.\nWhat would you like? (espresso/latte/cappuccino): ").strip().lower()

    if coffeeType == "report":
        coffee_machine.report()
    else:
        coffee = menu.find_drink(order_name=coffeeType)
        can_create_coffee = coffee_machine.is_resource_sufficient(coffee)
        if can_create_coffee:
            is_valid_amount = register.make_payment(cost=coffee.cost)
            if is_valid_amount:
                 coffee_machine.make_coffee(coffee)

