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
    print("You found a pickaxe!/nThis doubles ore resources when mining.")
    hasPickAxe = True

def buildingFour():
    print("You found a plow!/nThis doubles plant yield when harvesting.")
    hasPlow = True

def buildingFive():
    print("You found a shovel!/nThis doubles clay yield when digging")
    hasShovel = True