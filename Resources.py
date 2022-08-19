import Graphics

curOxygen = 60
totalOxygen = 60

food = 10
water = 5
ore = 0
plants = 0
bricks = 0

def printOxygen():
    print("Oxygen: " + str(curOxygen) + " minutes")
    Graphics.printBar(curOxygen, totalOxygen)
    print()
def printResources():
    printOxygen()
    print("Water: "+str(water))
    print("Food: "+str(food))
    print("Plants: "+str(plants))
    print("Ore: "+str(ore))
    print("Bricks: "+str(bricks))