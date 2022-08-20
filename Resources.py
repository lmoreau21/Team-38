import Graphics

curOxygen = 60
totalOxygen = 60

food = 5
water = 5
ore = 0
plants = 0
bricks = 0

def printOxygen():
    print("\nOxygen: " + str(curOxygen) + " minutes")
    Graphics.printBar(curOxygen, totalOxygen)
    print()
def printResources():
    printOxygen()
    print("Water: "+str(water)+"\tFood: "+str(food)+"\t\tPlants: "+str(plants)+"\tOre: "+str(ore)+"\tBricks: "+str(bricks))