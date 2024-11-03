class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

# Q1. Create subclass SmartCoffeeMachine to inheret from KitchenAppliance
class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']): # Q2. new attribute added of coffee_menu with default options
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
    
    def update_menu(self, new_coffee): #Q3. Two additional functions added 
        if new_coffee not in self.coffee_menu: #check if coffee already exists
            self.coffee_menu.append(new_coffee)
            print(f"{new_coffee} is added to the menu.")
        else:
            print(f"{new_coffee} is already on the menu.")

    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"{coffee_type} coming right up! ")
        else:
            print(f"Sorry, {coffee_type} does not exist.")
            print(f"Please choose an item from the menu: {self.coffee_menu}" )

#Testing the coffee machine functions. 
my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')