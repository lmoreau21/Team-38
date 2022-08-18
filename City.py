travelTime = 30
searchTime = 15
hasShovel = False
hasPlow = False
hasBike = False
hasPickAxe = False

def buildingOne():
    print("You found nothing!")
def buildingTwo():
    print("You found a bike!/nThis cuts travel time in half.")
    hasBike = True

def buildingThree():
    print("You found a pickaxe!/nThis cuts mining time in half.")
    hasPickAxe = True

def buildingFour():
    print("You found a plow!/nThis cuts harvesting time in half.")
    hasPlow = True

def buildingFive():
    print("You found a shovel!/nThis cuts digging time in half")
    hasShovel = True