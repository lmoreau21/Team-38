import Resources
import Upgrades

curBaseLevel = 1
hasFilter = False
curOxygenLevel = 1
hasGarden = False

def upgradeOption():
    wantUpgrade = input("Would you like to make any upgrades: ")
    while(wantUpgrade=="yes"):
        Upgrades.printUpgradeOptions()
        Upgrades.chooseUpgrade()
        wantUpgrade = input("Would you like to make any upgrades: ")


def printUpgradeOptions():
    oxygenTankCost()
    baseUpgradeCost()
    waterFilterCost()

def chooseUpgrade():
    userInput = int(input("Which upgrade: "))
    while userInput < 1 and userInput > 5:
        print("Please renenter the number")
        userInput = int(input("Which upgrade: "))
    if userInput == 1:
        Upgrades.upgradeOxygen()
    elif userInput == 2:
        Upgrades.upgradeBase()
    elif userInput == 3:
        Upgrades.upgradeFood()
    elif userInput == 4:
        Upgrades.upgradeFilterGarden()
    Resources.printResources()

def oxygenTankCost():
    print("1. Upgrade oxygen tank (extends max time by 30 min): ",end="")
    print(str(2*curOxygenLevel) + " Ore and " + str(2*curOxygenLevel)+ " Plants)")

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
        print("4. Filter costs: Level 2 Base, 3 Ore, and 1 Plant")
    if (hasGarden == False and hasFilter):
        print("4. Garden costs: Water Filter, 3 Bricks, 5 Plants")


def upgradeOxygen():
    if(Resources.ore>=2*Upgrades.curOxygenLevel and Resources.plants>=2*Upgrades.curOxygenLevel):
        Resources.maxOxygen+=30
        Upgrades.curOxygenLevel+=1
    else:
        print("Not enough resources")
def upgradeBase():
    if(Upgrades.curBaseLevel==1 and Resources.plants >=2 and Resources.bricks >=2):
        Upgrades.curBaseLevel+=1
        Resources.plants -=2
        Resources.bricks -=2
    elif(Upgrades.curBaseLevel ==2 and Resources.plants >=3 and Resources.bricks >=3 and Resources.ore >=1):
        Upgrades.curBaseLevel +=2
        Resources.plants -=3
        Resources.bricks -=3
        Resources.ore -=1
    elif(Upgrades.curBaseLevel ==3 and Resources.plants >=5 and Resources.bricks >=5 and Resources.ore >=2):
        Upgrades.curBaseLevel +=3
        Resources.plants -=5
        Resources.bricks -=5
        Resources.ore -=2
    else:
        print("Not enough resources")
def upgradeFood():
    if(Resources.plants >= 1):
        Resources.food+=1
        Resources.plants-=1
    else:
        print("Not enough resources")
def upgradeFilterGarden():
    if (curBaseLevel == 2 and Resources.ore >=3 and Resources.plants >=1 ):
        Resources.ore -=3
        Resources.plants -=1
        Upgrades.hasFilter = True
    elif(hasFilter and Resources.bricks >=3 and Resources.plants >= 5):
        Resources.bricks -=3
        Resources.plants -=5
        Upgrades.hasGarden = True
    else:
        print("Not enough resources or base level requirement")




