import Base


def start():
    print("You landed on a mysterious golden planet and decide to name it Planet PFT 1269.")
    print("The base seems to be falling apart and it doesn't seem like it'll last past a month.")
    print("This will be your home for an indefinite amount of time. Try your best to make it habitable in 30 days.")

    Base.startDay()

def objective():
    print("Since the landing was a little rough, you go to access the damages.")
    print("You find that your oxygen tank is intact but you probably need an upgrade soon.")
    print("You already have a small supply of food and water, but having a water filtration system at the base would be great.")

def gardenObjective():
    print("Gather plants and put them in the garden.")




def upgradeWater():
    print("You did it! Now you have an endless water supply!")
    print("You've made a water filtration that can sustain a garden!")

def upgradeOxygen2():
    print("You upgraded your O2 tank to Level 2! Your supply has gone up to 90 minutes!")
def upgradeOxygen3():
    print("You upgraded your O2 tank to Level 3! Your supply has gone up to 120 minutes!")
def upgradeOxygen4():
    print("You upgraded your O2 tank to Level 2! Your supply has gone up to 180 minutes!")
def upgradeBase():
    print("Your base is now secured! Your defense against the aliens have upgraded.")

def cityEntrance():
    print("You arrived to the entrance of the city. It's abandoned and small.")
    print("While looking around, you think about the type of people (or things) that once lived here.")
    print("Most of the city is in rubbles. It seems like you can only explore 5 buildings but you only have time for one right now.")


def plains():
    print("The plains has a large river running through it with plants growing along side it.")
    print("Some of the plants look delicious.")
    print("You notice that the areas of the river with more plants are cleaner than the other areas lacking plants.")
    print("These plants must be filtering the water.")

def goodEnd():
    print("Congratulations! You have successfully fulfilled all the objectives needed to live on Planet PFT 1269!")

def deathDays():
    print("Your base has collapsed! You lost everything. Now you're doomed to die.")
    print("Game Over")

def deathNutrients():
    print("Oh no, you forgot to eat! You died from malnutrition. Drink water and eat your vegetables.")
    print("Game Over")

def deathOxygen():
    print("You didn't have enough oxygen. You suffocated to death.")
    print("Game Over")
