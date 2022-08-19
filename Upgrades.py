curBaseLevel = 1
hasFilter = False
curOxygenLevel = 1
hasGarden = False

maxBaseLevel = 3
maxWaterLevel = 1
maxFoodLevel = 1
maxOxygenLevel = 100
numberReqOx = str(4*curOxygenLevel)

def upgradeOption():
    wantUpgrade = input("Would you like to make any upgrades")
    if(input=="yes"):
        printUpgradeOptions()


def printUpgradeOptions():
    oxygenTankCost()
    baseUpgradeCost()
    waterFilterCost()

def oxygenTankCost():
    print("1. Upgrade oxygen tank (extends max time by 30 min): ",end="")
    print(numberReqOx + " Ore and " + numberReqOx + " Plants)")

def baseUpgradeCost():
    print("2. Upgrade base costs:",end=" ")
    if(curBaseLevel==1):
        print("2 Plants and 2 Clay")
    elif(curBaseLevel==2):
        print("3 Plants, 3 Bricks, 1 Ore")
    elif(curBaseLevel==3):
        print("5 Plants, 5 Bricks, 2 Ore")

def waterFilterCost():
    if (hasGarden == False):
        print("3. Food costs: 1 Plant")
    if(hasFilter==False):
        print("4. Upgrade costs: Level 2 Base, 3 Ore, and 1 Plant")
    if (hasGarden == False and hasFilter):
        print("4. Upgrade costs: Water Filter, 3 Bricks, 5 Plants")


