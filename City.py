import Graphics
import Mountains
import Plains
import Resources
import Base
import City

travelTime = 30
searchTime = 15
hasShovel = False
hasPlow = False
hasBike = False
hasPickAxe = False

def getTravelTime():
    if(hasBike):
        return travelTime/2
    return travelTime
def buildingOne():
    print("You found nothing!")
    Resources.curOxygen -= searchTime
def buildingTwo():
    print("You found a bike!\nThis cuts travel time in half.")
    City.hasBike = True
    Graphics.printBike()
    Resources.curOxygen -= searchTime

def buildingThree():
    print("You found a pickaxe!\nThis doubles ore resources when mining.")
    City.hasPickAxe = True
    Graphics.printAxe()
    Resources.curOxygen -= searchTime
    Plains.ores *= 2
    Mountains.ores *= 2

def buildingFour():
    print("You found a plow!\nThis doubles plant yield when harvesting.")
    City.hasPlow = True
    Resources.curOxygen -= searchTime
    Graphics.printPlow()
    Plains.plant *= 2
    Mountains.plant *= 2

def buildingFive():
    print("You found a shovel!\nThis doubles clay yield when digging")
    City.hasShovel = True
    Graphics.printShovel()
    Resources.curOxygen -= searchTime
    Plains.clay *= 2
    Mountains.clay *= 2

def returnHome():
    Resources.curOxygen -= getTravelTime()