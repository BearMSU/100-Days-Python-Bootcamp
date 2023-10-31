print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'ve come to a crossroad, which direction would you like to take? Type "left" or "right". ').lower()

if choice1 == "left":
  #Continue in the game
  choice2 = input('You\'ve come to a lake, there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim. ').lower()
  if choice2 == "wait":
    #Continue in the game
    choice3 = input("You have arrived at the island unharmed. In front of you there is a hut with three doors. One door is green. One door is yellow. One door is red. Which do you choose? ").lower()
    if choice3 == "green":
      #Continue in the game
      print("You found the treasure!!! Congratulations!!! You've won the game!!!")
    elif choice3 == "yellow":
      print("A pirate has jumped out and you have been captured. Game Over.")
    elif choice3 == "red":
      print("A bear has has broken through the door and eaten you. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You were pulled under by a shark. Game Over.")
else:
  print("You fell into a pit of fire. Game Over.")
