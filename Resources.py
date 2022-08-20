import Graphics

curOxygen = 30
totalOxygen = 30

#resources you need to survive
food = 3
water = 3
ore = 0
plants = 0
bricks = 0

#display resources
def printOxygen():
    Graphics.printBar(curOxygen, totalOxygen)
    print()

def printResources():
    printOxygen()
    print("Water: "+str(water)+"\tFood: "+str(food)+"\t\tPlants: "+str(plants)+"\tOre: "+str(ore)+"\tBricks: "+str(bricks))