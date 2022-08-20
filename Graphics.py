#creates a axe graphic
def printAxe():
    print(r""" _,-,
T_  |
||`-'
||
||
~~""")

#creates a pickaxe graphic
def printPickAxe():
    print(r""" ,--,_,--,
<|  _T_  |>
 '-`| |`-'
    | |
    | |
    ~~~""")

#creates a Plow graphic
def printPlow():
    print(r"""                                        
  ~~:..                                  :~JPB#G. 
 .B&&@@&&#G5?!^:.                   .~5#&&#P?~:   
     .:^!?5GB&&@@&&#BPY?~^..     .7#@@B?:         
                .:~7JPG#&&@@&#BPB@@#!             
                           .?&@@@#^               
                         .?#@@@@J                 
                      :?#@@@@@@7                  
                  .!P&@@@@@@@@J                   
             .7YB&@@@@@@@@@@@B                    
             :&@@@@@@@@@@@#5!.                    
               ~B@@@@&BJ^.                        
                 ..:.                """)

# creates a Shovel graphic
def printShovel():
    print(r"""
                    ██████            
                  ██░░░░▒▒██          
                ██░░░░▒▒░░▓▓          
              ██░░░░▒▒░░░░▓▓          
                ▓▓▒▒░░░░▓▓░░          
              ▓▓▒▒██░░▓▓              
            ▓▓▓▓██  ██                
          ▓▓▒▒██                      
        ▓▓▓▓██                                                                            
    ██▓▓▒▒██                              
    ▓▓▒▒██                                
      ▓▓██                                
                    """)

#creates a Land graphic
def land():
    print(r"""                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \:.    / `.
                   / .-'':._.'`-. \
                   |/    /||\    \|
               _..--\"\"\"````\"\"\""'--.._
           _.-'``                    ``'-._
         -'                                '-""")

#creates a Bike graphic
def printBike():
    print(r"""  ,
.-/c-.,:: 
(_)'==(_)    
    """)

#creates a Base1 graphic
def printBase1():
    print(r"""      ___I_
     /\-_--\
    /  \_-__\
    |[]| [] |""")

#creates a Base2 graphic
def printBase2():
        print(r"""       []___
      /    /\____
(~)  /_/\_//____/\
 |   | || |||__|||""")

#creates a Base3 graphic
def printBase3():
            print(r"""     ____||____
    ///////////\
   ///////////  \
   |    _    |  |
   |[] | | []|[]|  
   |   | |   |  |""")

# creates a Mountains graphic
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

# creates a Plains graphic
def printPlains():
    print(r"""             ░░      ░░  ░░    ▒▒░░            ░░      
                ░░    ░░░░▒▒░░        ▒▒        
        ▒▒      ░░    ▒▒  ▒▒░░      ░░          
          ░░    ░░▒▒  ▒▒  ▒▒      ░░▒▒          
          ▒▒    ░░  ▒▒    ▒▒  ░░  ▒▒        ░░  
          ░░░░  ▒▒  ▒▒  ░░▒▒  ░░  ▒▒      ▒▒    
          ▒▒▓▓  ▒▒  ▓▓▒▒▒▒▒▒  ▒▒▒▒▓▓    ▒▒           
        ░░▒▒░░▒▒▒▒  ▒▒▓▓▒▒▓▓  ▒▒▓▓░░░░▓▓░░      
          ░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓░░▓▓░░  ▒▒      
          ▓▓░░▓▓████▓▓██▓▓░░▒▒▓▓██▓▓▒▒▓▓▒▒▓▓    
          ▓▓▓▓████████████▓▓▓▓██▓▓████████▓▓    """)

#creates a Buildings graphic
def printBuildings():
            print(r"""            |   _   _
      . | . x .|.|-|.|
   |\ ./.\-/.\-|.|.|.|
   |.|_|.|_|.|.|.|_|.|""")

#creates a Explosion graphic
def printExplosion():
            print(r"""          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
  ___________/_ __ \___________""")

#creates a CharacterDead graphic
def printCharacterDead():
                print(r"""
 .--.
(()())
 |HH| You are dead.
 `--'
                       ~~""")

def printBar(cur, max):
    print("Oxygen: "+str(cur)+" minutes")
    for x in range (60):
        if(x <= cur/max*60):
            print("█",end="")
        else:
            print("▒",end="")
