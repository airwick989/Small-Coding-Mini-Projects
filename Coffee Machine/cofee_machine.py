#COFFEE MACHINE

from os import system




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}




insufficient = []




def report():

    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")




def refill():

    global resources
    
    if resources["water"] + resources["milk"] + resources["coffee"] == 600:
        return "The coffe machine is already full of all its ingredients! \n"
    else:
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        return "The coffee machine has been refilled of all ingredients. \n"




def check_sufficient(coffee):

    #print(MENU[coffee]["ingredients"])  #THIS IS THE SYNTAX FOR REFERRING TO A DICTIONARY IN A DICTIONARY
    global insufficient
    sufficient = True

    for ingredient in MENU[coffee]["ingredients"]:
        
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            sufficient = False
            insufficient.append(ingredient)
    
    return sufficient




def apologize():
    
    global insufficient
    apology = "Sorry, there is not enough "
    apology_num = len(insufficient)

    for resource in range(0, apology_num):

        if len(insufficient) > 1:
            apology += f"{insufficient[0]}, "
            insufficient.remove(insufficient[0]) 
        elif apology_num > 1:
            apology += f"and {insufficient[0]}. \n"
            insufficient.remove(insufficient[0]) 
        else:
            apology += f"{insufficient[0]}. \n"
            insufficient.remove(insufficient[0]) 
        
    return apology




def brew(coffee):

    global resources

    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]




def process_coins(coffee):

    print(f"The price is ${MENU[coffee]['cost']}. Please insert coins.\n")
    
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    return  (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)




def transaction(coffee):

    global resources

    if check_sufficient(coffee) == False:
        print(apologize())
    else:
        payed = process_coins(coffee)
        
        if payed >= MENU[coffee]["cost"]:
            brew(coffee)
            print(f"Here is your {coffee}, enjoy!\n")
            resources["money"] += payed
        
        if payed > MENU[coffee]["cost"]:
            change = payed - MENU[coffee]["cost"]
            resources["money"] -= change
            print(f"Here is ${round(change, 2)} in change.\n")

        if payed < MENU[coffee]["cost"]:
            print("Sorry, that's not enough money. Money refunded.\n")        

        


on = True

system('cls')

while on == True:
    
    operation = (input("What would you like? (espresso/latte/cappuccino): ")).lower()

    while operation != "espresso" and operation != "latte" and operation != "cappuccino" and operation != "report" and operation != "off" and operation != "refill":
        operation = (input("That is not a valid option. Please enter a valid operation: ")).lower()

    if operation == "off":
        on = False
    elif operation == "report":
        report()
    elif operation == "refill":
        print(refill())
    else:
        transaction(operation)
    
    print("\n")

