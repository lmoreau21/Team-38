# This is a sample Python script.
import City
import Graphics
import Lore
import Mountains
import Plains
import Resources
import Upgrades
import main
import Base

isDay = True

def startDay():
    while(main.day<=30):
        Base.atBase()
    if(Upgrades.curBaseLevel==3 and Upgrades.hasFilter and Upgrades.hasGarden):
        Lore.goodEnd()
    else:
        Lore.deathDays()
    exit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def atBase():
    print("\nIt is day "+str(main.day))
    Base.isDay = True
    while(isDay):
        chooseLocation()

def endDay():
    main.day += 1
    Resources.curOxygen = Resources.totalOxygen
    if(Upgrades.hasGarden==False):
        Resources.food -= 1
    if Resources.food < 0:
        Lore.deathNutrients()
        exit()
    if (Upgrades.hasFilter == False):
        Resources.water -= 1
    if Resources.water < 0:
        Lore.deathNutrients()
        exit()



def noOxygen():
    if Resources.curOxygen < 0:
        Lore.deathOxygen()
        exit()

def basePic():
    if (Upgrades.curBaseLevel == 1):
        print(Graphics.printBase1())
    elif (Upgrades.curBaseLevel == 2):
        print(Graphics.printBase2())
    else:
        print(Graphics.printBase3())

def chooseLocation():
    print(basePic())
    Resources.printResources()
    print("1. Plains ("+ str(Plains.getTravelTime()) +" minutes)")
    print("2. Mountain ("+ str(Mountains.getTravelTime()) +" minutes)")
    print("3. City (" + str(City.getTravelTime()) + " minutes)")
    print("4. Upgrade")
    print("5. End Day")
    userInput = int(input("Which location: "))
    while userInput < 1 and userInput > 5:
        print("Please renenter the number")
        userInput = int(input("Which location: "))
    if userInput == 1:
        Lore.plains()
        Base.choosePlain()
    elif userInput == 2:
        Base.chooseMountain()
    elif userInput == 3:
        Lore.cityEntrance()
        Base.chooseCity()
    elif userInput == 4:
        Upgrades.upgradeOption()
    else:
        Base.isDay = False
        endDay()

def choosePlain():
    Plains.returnHome()
    Base.noOxygen()
    while (True):
        Base.noOxygen()
        Resources.printResources()
        print("\nEach Activity takes "+str(Plains.resourceTime)+" minutes")
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
            noOxygen()
            Base.chooseLocation()
            break

        ##Resources.printResources()
def chooseMountain():
    Mountains.returnHome()
    Base.noOxygen()
    while (True):
        Base.noOxygen()
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
            Base.noOxygen()
            Base.chooseLocation()
            break
        Resources.printResources()
def chooseCity():
    City.returnHome()
    Base.noOxygen()

    while (True):
        Base.noOxygen()
        print("Each Building takes " + str(City.searchTime) + " minutes to search")
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
            Base.noOxygen()
            Base.chooseLocation()
            break
