import Graphics
import Mountains
import Plains
import Resources
import Base
import City

travelTime = 30
searchTime = 15
hasBike = False

def getTravelTime():
    if(hasBike):
        return travelTime/2
    return travelTime

#Building One has nothing
def buildingOne():
    print("You found nothing!")
    Resources.curOxygen -= searchTime

#Building Two has a bike that doubles speed
def buildingTwo():
    print("You found a bike!\nThis cuts travel time in half.")
    City.hasBike = True
    Graphics.printBike()
    Resources.curOxygen -= searchTime

#Building Three gives pickaxe to double ore
def buildingThree():
    print("You found a pickaxe!\nThis doubles ore resources when mining.")
    Graphics.printAxe()
    Resources.curOxygen -= searchTime
    Plains.ores *= 2
    Mountains.ores *= 2

#Building Four has plow to double plants
def buildingFour():
    print("You found a plow!\nThis doubles plant yield when harvesting.")
    Resources.curOxygen -= searchTime
    Graphics.printPlow()
    Plains.plant *= 2
    Mountains.plant *= 2

#Building Five has a shovel to double clay
def buildingFive():
    print("You found a shovel!\nThis doubles clay yield when digging")
    Graphics.printShovel()
    Resources.curOxygen -= searchTime
    Plains.clay *= 2
    Mountains.clay *= 2

def returnHome():
    Resources.curOxygen -= getTravelTime()