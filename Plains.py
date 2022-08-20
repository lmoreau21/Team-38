import Base
import City
import Resources
import Upgrades

travelTime = 5
ores = 1
waters = 2
plant = 2
clay = 1

resourceTime = 10

#checks if the player has bike and changes travel time if they do
def getTravelTime():
    if(City.hasBike):
        return travelTime/2
    return travelTime

#if selected takes away oxygen based on travel time
def returnHome():
    Resources.curOxygen -= getTravelTime()

#if selected adds plants and takes away oxygen
def harvestPlants():
    Resources.plants+=plant
    Resources.curOxygen -= resourceTime

#if selected adds water and takes away oxygen
def collectWater():
    Resources.water+=waters
    Resources.curOxygen -= resourceTime

#if selected adds bricks and takes away oxygen
def digClay():
    Resources.bricks+=clay
    Resources.curOxygen -= resourceTime

#if selected adds ore and takes away oxygen
def mineOre():
    Resources.ore+=ores
    Resources.curOxygen -= resourceTime