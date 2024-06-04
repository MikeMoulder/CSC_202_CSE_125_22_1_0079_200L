#Treasure Hunt

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[🦜🏴‍☠️🏴‍☠️]
*******************************************************************************
''')

print("This is a Treasure Hunt")
direction = input('You are at a crossroad. Enter "right" or "left" to navigate-> ').upper()

if(direction == "RIGHT"):
    print("You made the wrong choice! Off into the pit you go!")
elif (direction == "LEFT"):
    direction = input("Great Choice! Now you arrived at a lake, would like to 'Wait' or 'Swim': ").upper()

    if(direction == "SWIM"):
        print("Smart!, you made it across the lake!")
        direction = input("Now there are 3 doors, a 'Blue', 'Red' and 'Green'! Choose to access the chest: ").lower()

        if(direction == "blue"):
            print("You came this far to fail! Sad!")
        elif (direction == "red"):
            print("You bravery has earned you what you deserve! Enjoy!")
        elif (direction == "green"):
            print("You just got devoured")
        else:
            print("What's wrong with you?")
    elif (direction == "WAIT"):
        print("You got shot by the evil pirate! 🏴‍☠️")
    else:
        print("You're not taking this seriously enough! Restart!")
else:
    print("You don't seem ready. Lol!")