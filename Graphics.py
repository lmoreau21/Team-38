def printAxe():
    print(r"""
 _,-,
T_  |
||`-'
||
||
~~""")

def printBar(cur, max):
    for x in range (max):
        if(x <= cur):
            print("|",end="")
        else:
            print("-",end="")