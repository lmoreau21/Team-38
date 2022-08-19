import Base
import City
import Resources
import Upgrades

travelTime = 6
ores = 1
waters = 2
plant = 4
clay = 4

resourceTime = 10

def getTravelTime():
    if(City.hasBike):
        return travelTime/2
    return travelTime

def returnHome():
    Resources.curOxygen -= getTravelTime()
def harvestPlants():
    Resources.plants+=plant
    Resources.curOxygen -= resourceTime
def collectWater():
    Resources.water+=waters
    Resources.curOxygen -= resourceTime
def digClay():
    Resources.bricks+=clay
    Resources.curOxygen -= resourceTime
def mineOre():
    Resources.ore+=ores
    Resources.curOxygen -= resourceTime