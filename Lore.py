import Base
import Graphics


def start():
    Graphics.land()
    print("You landed on a mysterious golden planet and decide to name it Planet PFT 1269.")
    print("The base seems to be falling apart and it doesn't seem like it'll a third of a month.")
    print("This will be your home for an indefinite amount of time. Try your best to make it habitable in 10 days.")

    Base.startDay()

def objective():
    print("Since the landing was a little rough, you go to access the damages.")
    print("You find that your oxygen tank is intact but you probably need an upgrade soon since it lasts only 30 minutes a day.")
    print("You only have 3 days of food and water, but having a water filtration system at the base would be great.")
def gardenObjective():
    print("Congrats! You made a garden. You do not have to think about food anymore")



#Upgrades
def upgradeWater():
    print("You did it! Now you have an endless water supply!")
    print("You've made a water filtration that can sustain a garden!")
#
def upgradeOxygen():
    print("You upgraded your O2 tank! Your supply has gone up by 30 minutes!")

def upgradeBase():
    print("You upgrade your base! Now you can upgrade more things.")
#Entering each location
def city():
    print("You arrived to the entrance of the city. It's abandoned and small.")
    print("While looking around, you think about the type of people (or things) that once lived here.")
    print("Most of the city is in rubbles. It seems like you can only explore 5 buildings but you only have time for one right now.")
def plains():
    print("\nThe plains has a large sparkling river running through it with plants growing along side it.")
    print("Some of the plants look delicious.")
    print("You notice that the areas of the river with more plants are cleaner than the other areas lacking plants.")
    print("These plants seem to be filtering the water.")
def mountains():
    print("As you walk up to the mountains, you feel tiny compared to the tall structures.")
    print("There are ores all along the sides and a few plants.")





#endings
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
