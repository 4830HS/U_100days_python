from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 : Print report.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on :
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off" :
        is_on = False
    elif choice == "report" :      
        coffee_maker.report()
        money_machine.report()
    else : 
        drink = menu.find_drink(choice)
        # print(drink)

        # TODO 2 : Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink) :
            # TODO 3 : Process coins.
            # TODO 4 : Check transaction successful?
            if money_machine.make_payment(drink.cost) :
                # TODO 5 : Make Coffee.
                coffee_maker.make_coffee(drink)
            
            # or) if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) :