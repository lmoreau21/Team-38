# This is a sample Python script.
import City
import Graphics
import Mountains
import Plains
import Resources
import main


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


                        # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.chooseLocation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def chooseLocation():
    print("1. Plains ("+ str(Plains.getTravelTime()) +" minutes)")
    print("2. Mountain ("+ str(Mountains.getTravelTime()) +" minutes)")
    print("3. City (" + str(City.getTravelTime()) + " minutes)")
    userInput = int(input("Which location: "))
    while userInput >= 1 and userInput <= 3:
        if userInput == 1:
            main.choosePlain()
        elif userInput == 2:
            main.chooseMountain()
        elif userInput == 3:
            main.chooseCity()
        else:
            print("Please renenter the number")
def choosePlain():
    Plains.returnHome()
    print("Each Activity takes "+str(Plains.resourceTime)+" minutes")
    print("1. Harvest Plants")
    print("2. Collect Water")
    print("3. Dig for Clay")
    print("4. Mine for Ore")
    print("5. Return Home")
    userInput = int(input("Which Action: "))
    while userInput >= 1 and userInput <= 5:
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
        else:
            print("Please renenter the number")
def chooseMountain():
    print("Each Activity takes " + str(Mountains.resourceTime) + " minutes")
    print("1. Harvest Plants")
    print("2. Collect Water")
    print("3. Dig for Clay")
    print("4. Mine for Ore")
    print("5. Return Home")
    userInput = int(input("Which Action: "))
    while userInput >= 1 and userInput <= 5:
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
        else:
            print("Please renenter the number")
def chooseCity():
    print("Each Building takes " + str(City.resourceTime) + " minutes to search")
    print("1. Building One")
    print("2. Building Two")
    print("3. Building Three")
    print("4. Building Four")
    print("5. Building Five")
    print("6. Return Home")
    userInput = int(input("Which Action: "))
    while userInput >= 1 and userInput <= 6:
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
        else:
            print("Please renenter the number")
