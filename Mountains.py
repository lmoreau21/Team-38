import Base
import City
import Resources
import Upgrades

travelTime = 15
ores = 2
waters = 1
plant = 1
clay = 2

resourceTime = 10

#checks to see if the player has unlocked the bike and changes the travel time based on that
def getTravelTime():
    if(City.hasBike):
        return travelTime/2
    return travelTime

#if selected takes away oxygen based on the cost of travel
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

#if selected adds ore and takes away oxugen
def mineOre():
    Resources.ore+=ores
    Resources.curOxygen -= resourceTime