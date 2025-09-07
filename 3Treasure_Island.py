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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
a=input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").strip().lower()
if a=="right":
    print("You fell into a hole. Game Over.")
elif a== "left":
    b=input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across: ").strip().lower()
    if b=="swim":
        print("Attacked by trout. Game Over.")
    elif b=="wait":
        c=input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue.\nWhich colour do you choose? ").strip().lower()
        if c=="red":
            print("Burned by fire. Game Over.")
        elif c=="blue":
            print("Eaten by beasts. Game Over.")
        elif c=="yellow":
            print("You Win!")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid direction. Game Over.")
