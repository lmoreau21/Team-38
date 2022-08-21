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
firstMountain = True
firstCity = True
firstPlain = True

#Checks day count and win conditions each day
def startDay():
    Lore.objective()
    while(main.day<=10):
        Base.atBase()
    if(Upgrades.curBaseLevel==3 and Upgrades.hasFilter and Upgrades.hasGarden):
        Lore.goodEnd()
    else:
        Graphics.printExplosion()
        Lore.deathDays()
    exit()

# gives information on the day and food/water consumption also runs function to choose location
def atBase():
    print("\nIt is day "+str(main.day)+". You have eaten one food and water!")
    Base.basePic()
    Base.isDay = True
    while(Base.isDay):
        Base.chooseLocation()

"""Takes away 1 food and 1 water at the end of day, adds a day to day count, and checks
   condition for a malnutrition death
"""
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

#checks oxygen level whenever called to determine if the player dies
def noOxygen():
    if Resources.curOxygen < 0:
        Lore.deathOxygen()
        exit()

#changes base picture based on level of base
def basePic():
    if (Upgrades.curBaseLevel == 1):
        Graphics.printBase1()
    elif (Upgrades.curBaseLevel == 2):
        Graphics.printBase2()
    else:
        Graphics.printBase3()

"""Gives the player options of what to do at their base and takes the players
input to determine where their go/ what they do 
"""
def chooseLocation():
    Resources.printResources()
    print("1. Plains ("+ str(Plains.getTravelTime()) +" minutes)")
    print("2. Mountain ("+ str(Mountains.getTravelTime()) +" minutes)")
    print("3. City (" + str(City.getTravelTime()) + " minutes)")
    print("4. Upgrade")
    print("5. End Day")
    userInput = int(input("Which location: "))
    while (userInput < 1 and userInput > 5 and userInput == 101):
        print("Please renenter the number")
        userInput = int(input("Which location: "))
    if userInput == 1:
        print("Welcome to the plains")
        if(firstPlain):
            Lore.plains()
            Base.firstPlain = False
        Graphics.printPlains()
        Base.choosePlain()
    elif userInput == 2:
        print("Welcome to the mountains")
        if(firstMountain):
            Lore.mountains()
            Base.firstMountain = False
        Graphics.printMountains()
        Base.chooseMountain()
    elif userInput == 3:
        print("Welcome to the city")
        if(firstCity):
            Lore.city()
            Base.firstCity = False
        Graphics.printBuildings()
        Base.chooseCity()
    elif userInput == 4:
        Upgrades.upgradeOption()
    elif userInput == 5:
        Base.isDay = False
        endDay()
    elif userInput == 101:
        Resources.curOxygen = 360
        Resources.ore = 100
        Resources.water = 100
        Resources.food = 100
        Resources.plants = 100
        Resources.bricks = 100

#gives the player options of resopurces to collect if they select to go to the plains
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
        print("5. Return Home ("+str(Plains.getTravelTime())+" minutes)")
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

#gives the player options of resopurces to collect if they select to go to the Mountians
def chooseMountain():
    Mountains.returnHome()
    Base.noOxygen()
    while (True):
        Base.noOxygen()
        print("\nEach Activity takes " + str(Mountains.resourceTime) + " minutes")
        print("1. Harvest Plants")
        print("2. Collect Water")
        print("3. Dig for Clay")
        print("4. Mine for Ore")
        print("5. Return Home ("+str(Mountains.getTravelTime())+" minutes)")
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

"""gives the player the option of what building to search for while in the city
and grants the item that is in that building
"""
def chooseCity():
    City.returnHome()
    Base.noOxygen()

    while (True):
        Graphics.printBar(Resources.curOxygen, Resources.totalOxygen)
        Base.noOxygen()
        print("\nEach Building takes " + str(City.searchTime) + " minutes to search")
        print("1. Building One")
        print("2. Building Two")
        print("3. Building Three")
        print("4. Building Four")
        print("5. Building Five")
        print("6. Return Home ("+str(City.getTravelTime())+" minutes)")
        userInput = int(input("Which Action: "))
        while userInput < 1 and userInput > 6:
            print("Please renenter the number")
            userInput = int(input("Which Action: "))
        if userInput <= 5:
            City.buildings[userInput-1]()
        elif userInput == 6:
            City.returnHome()
            Base.noOxygen()
            Base.chooseLocation()
            break
