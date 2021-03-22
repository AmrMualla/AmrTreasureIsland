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
print("Welcome to Amr's Deadly Treasure Island.")
print("Your mission is to find the treasure. Good luck m8") 

Choiceone = input(print("You've reached a crossroad. What direction would you like to head in? Type 'right' or 'left'"))

if(Choiceone == "Left" or Choiceone == "left"):
  Choicetwo = input(print("You've reached a lake, would you like to swim across or wait for a boat to arrive? Type 'swim' or 'wait'"))
  if(Choicetwo == "Wait" or Choicetwo == "wait"):
    Choicethree = input(print("You made it safely across, and have a choice of three caves to continue. Each cave has a colored mark outside. What color do you choose? Type 'red', 'blue' or 'orange'"))
    if(Choicethree == "Orange" or Choicethree == "orange"):
      print("CONGRATULATIONS! You've found Amr's Hidden Treasure, I bet you were thinking you were gonna get some gold, no no, this is worth more, this is a collection of all my novels. Knowledge is power. ")
    else:
      print("[GAMEOVER] Khabib was in the cave and challenged you. He remains undefeated.")
  else:
    print("[GAMEOVER] You got slapped by a Kraken, the hit was fatal.")
else:
  print("[GAMEOVER] Tough luck, a herd of buffalo trampled you.")


