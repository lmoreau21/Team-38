# This is a sample Python script.
import City
import Graphics
import Mountains
import Plains
import Resources
import Upgrades
import main


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def atBase():
    print("It is day "+str(main.day))
    chooseLocation()

def chooseLocation():
    Resources.printResources()
    print("1. Plains ("+ str(Plains.getTravelTime()) +" minutes)")
    print("2. Mountain ("+ str(Mountains.getTravelTime()) +" minutes)")
    print("3. City (" + str(City.getTravelTime()) + " minutes)")
    print("4. Upgrade and End Day")
    userInput = int(input("Which location: "))
    while userInput < 1 and userInput > 3:
        print("Please renenter the number")
        userInput = int(input("Which location: "))
    if userInput == 1:
        main.choosePlain()
    elif userInput == 2:
        main.chooseMountain()
    elif userInput == 3:
        main.chooseCity()
    elif userInput == 4:
        Upgrades.upgradeOption()

def choosePlain():
    Plains.returnHome()
    Resources.printOxygen()
    print("Each Activity takes "+str(Plains.resourceTime)+" minutes")
    print("1. Harvest Plants")
    print("2. Collect Water")
    print("3. Dig for Clay")
    print("4. Mine for Ore")
    print("5. Return Home")
    userInput = int(input("Which Action: "))
    while userInput < 1 and userInput > 5:
        print("Please renenter the number")
        userInput = int(input("Which Action: "))
    if userInput == 1:
        Plains.harvestPlants()
    elif userInput == 2:
        Plains.collectWater()
    elif userInput == 3:
        Plains.digClay()
    elif userInput == 4:
        Plains.mineOre()
    elif userInput == 5:
        Plains.returnHome()
    Resources.printResources()
def chooseMountain():
    Mountains.returnHome()
    Resources.printOxygen()
    print("Each Activity takes " + str(Mountains.resourceTime) + " minutes")
    print("1. Harvest Plants")
    print("2. Collect Water")
    print("3. Dig for Clay")
    print("4. Mine for Ore")
    print("5. Return Home")
    userInput = int(input("Which Action: "))
    while userInput < 1 and userInput > 6:
        print("Please renenter the number")
        userInput = int(input("Which Action: "))
    if userInput == 1:
        Mountains.harvestPlants()
    elif userInput == 2:
        Mountains.collectWater()
    elif userInput == 3:
        Mountains.digClay()
    elif userInput == 4:
        Mountains.mineOre()
    elif userInput == 5:
        Mountains.returnHome()
    Resources.printResources()
def chooseCity():
    City.returnHome()
    Resources.printOxygen()
    print("Each Building takes " + str(City.resourceTime) + " minutes to search")
    print("1. Building One")
    print("2. Building Two")
    print("3. Building Three")
    print("4. Building Four")
    print("5. Building Five")
    print("6. Return Home")
    userInput = int(input("Which Action: "))
    while userInput < 1 and userInput > 6:
        print("Please renenter the number")
        userInput = int(input("Which Action: "))
    if userInput == 1:
        City.buildingOne()
    elif userInput == 2:
        City.buildingTwo()
    elif userInput == 3:
        City.buildingThree()
    elif userInput == 4:
        City.buildingFour()
    elif userInput == 5:
        City.buildingFive()
    elif userInput == 6:
        City.returnHome()
    Resources.printResources()
