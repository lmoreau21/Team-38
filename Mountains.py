import City
import Resources
import Upgrades

travelTime = 16
ores = 4
waters = 2
plant = 1
clay = 2

resourceTime = 10

def getTravelTime():
    if(City.hasBike):
        return travelTime/2
    return travelTime

def returnHome():
    Resources.curOxygen -= getTravelTime()
def harvestPlants():
    Resources.plants+=plant
def collectWater():
    Resources.water+=waters
def digClay():
    Resources.bricks+=clay
def mineOre():
    Resources.ore+=ores