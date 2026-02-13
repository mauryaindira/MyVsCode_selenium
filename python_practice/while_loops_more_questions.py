'''import random 
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 +  die2
print(f'The total is {total} of dice1: {die1},  dice2: {die2}')
# Keep rolling until total == 2 (snake eyes)
while total !=2:
  print("Nopes; Rerolling the dices")
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  print("Adding the total again")
  total = die1 +  die2
  print(total)
# we got snake eyes
print("Snake eyes!")'''

'''answer = input("Are we there yet?")

while answer != "Yes":
  answer = input("Are we there yet?")'''

for i in range(1,25):
    print(i , ':',      "* " * i)

