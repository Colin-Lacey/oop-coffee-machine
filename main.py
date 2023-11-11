from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

print("hello")

operating = True
while operating:
    options = my_menu.get_items()
    user_choice = input(f"What would you like? ({options})\n").lower()
    if user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif user_choice == "off":
        # input "off" -> stop the program
        operating = False
        break
    elif my_menu.find_drink(user_choice) is not None:
        drink = my_menu.find_drink(user_choice)
        sufficient_resources = my_coffee_maker.is_resource_sufficient(drink)
        if sufficient_resources:
            payment_accepted = my_money_machine.make_payment(
                next((x.cost for x in my_menu.menu if x.name == user_choice), None)
            )
            if payment_accepted:
                my_coffee_maker.make_coffee(drink)
