import Graphics
def printAxe():
    print(r"""
 _,-,
T_  |
||`-'
||
||
~~""")

def printPickAxe():
    print(r"""
 _,-,
T_  |
||`-'
||
||
~~""")


def printBike():
    print(r"""  ,
.-/c-.,:: 
(_)'==(_)    
    """)

def printBase1():
    print(r"""      ___I_
     /\-_--\
    /  \_-__\
    |[]| [] |""")

def printBase2():
        print(r"""       []___
      /    /\____
(~)  /_/\_//____/\
 |   | || |||__|||""")

def printBase3():
            print(r"""     ____||____
    ///////////\
   ///////////  \
   |    _    |  |
   |[] | | []|[]|  
   |   | |   |  |""")
def printMountains():
            print(r"""             o\
   _________/__\__________
  |                  - (  |
 ,'-.                 . `-|
(____".       ,-.    '   ||
  |          /\,-\   ,-.  |
  |      ,-./     \ /'.-\ |
  |     /-.,\      /     \|
  |    /     \    ,-.     \
  |___/_______\__/___\_____\ """)

def printBuildings():
            print(r"""            |   _   _
      . | . x .|.|-|.|
   |\ ./.\-/.\-|.|.|.|
   |.|_|.|_|.|.|.|_|.|""")

def printExplosion():
            print(r"""          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
  ___________/_ __ \___________""")

def printCharacterDead():
                print(r"""
 .--.
(()())
 |HH| You are dead.
 `--'
                       ~~""")


def printBar(cur, max):
    for x in range (60):
        if(x <= cur/max*60):
            print("█",end="")
        else:
            print("▒",end="")
