# Name: Dayanara 
# Period 6 
# Dice Rolling Simulator

import random 

side1 = 0 
side2 = 0
side3 = 0
side4 = 0 
side5 = 0 
side6 = 0


print("Hello human being of this earth. Welcome tooooooo Dice Rolling Simulator!")
roll = int(input (" How many time would like to roll the dice?: "))
x = 1
while x<= roll:
 
  rolls = random.randint(1,6)
  if rolls == 1:
    side1 += 1
    print("result is 1")
  elif rolls == 2:
    side2 += 1
    print("result is 2")
  elif rolls == 3:
    side3 += 1
    print("result is 3")
  elif rolls == 4:
    side4 += 1
    print("result is 4")
  elif rolls == 5:
    side5 += 1
    print("result is 5")
  else:
    side6 += 1
    print("result is 6")
  x = x+1
print("The dice was rolled " + str(rolls) + "times!")


