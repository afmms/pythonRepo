# At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
nWater = 400
nMilk = 540
nCoffee = 120
nCups = 9
nMoney = 550


def printCurrentState():
    print()
    print("The coffee machine has:")
    print(nWater,"ml water")
    print(nMilk, "ml of milk")
    print(nCoffee,"g coffee beans")
    print(nCups, " disposable cups")
    print(str(nMoney) + "$")
    

def getAction():
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if(action == "buy"):
        return 1
    elif(action == "fill"):
        return 2
    elif(action == "take"):
        return 3
    elif(action == "remaining"):
        return 4   
    else:
        return 5
        

def checkResources(water, milk, coffee):
    print()
    global nWater
    global nMilk
    global nCoffee

    if(nWater - water < 0):
        return [False, "Sorry, not enough water!"]
    elif(nMilk - milk < 0):
        return [False, "Sorry, not enough milk!"]
    elif(nCoffee - coffee < 0):
        return [False, "Sorry, not enough coffee beans!"]
    else:
        return [True, "I have enough resources, making you a coffee!"]


def doEspresso():
    # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
    global nWater
    global nCoffee
    global nMoney
    global nCups
    output = checkResources(250, 0, 16)
    print(output[1])
    if(output[0]):    
        nCups-=1
        nWater = nWater - 250
        nCoffee -= 16
        nMoney += 4


def doLatte():
    # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    global nWater
    global nMilk
    global nCoffee
    global nMoney
    global nCups
    output = checkResources(250, 0, 16)
    print(output[1])
    if(output[0]):    
        nCups-=1
        nWater -= 350
        nMilk -= 75
        nCoffee -= 20
        nMoney += 7


def doCappuccino():
    # For a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6. 
    global nWater
    global nMilk
    global nCoffee
    global nMoney
    global nCups
    output = checkResources(250, 0, 16)
    print(output[1])
    if(output[0]):    
        nCups-=1
        nWater -= 200
        nMilk -= 100
        nCoffee -= 12
        nMoney += 6


def displayCoffees():
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input()
    if(choice == str(1)):
        doEspresso()
    elif(choice == str(2)):
        doLatte()
    elif(choice == str(3)):
        doCappuccino()   
    else:
        pass     
    

def displayFill():
    print()
    global nWater
    global nMilk
    global nCoffee
    global nMoney
    global nCups
    

    print("Write how many ml of water do you want to add:")
    nWater += int(input())
    print("Write how many ml of milk do you want to add:")
    nMilk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    nCoffee += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    nCups += int(input())
    

def displayTake():
    print()
    global nMoney
    print("I gave you $", nMoney)
    nMoney = 0
    

def run():
    while(True):
        actionID = getAction()  
        if(actionID == 1):
            displayCoffees()
        elif(actionID == 2):
            displayFill()
        elif(actionID == 3):
            displayTake()
        elif(actionID == 4):
            printCurrentState()        
        else:
            break

run()