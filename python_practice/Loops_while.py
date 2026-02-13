
'''#loops:  while
print("Bank of Codedex")
pin = int(input("Enter the Pin: "))

while pin !=1234:
  pin =  int(input("Incorrect Pin: enter correct pin:" ))

if pin== 1234:
  print("Pin Accepted")'''


#################

#guess the the number
'''
guess = 0
tries = 0

while guess !=6 and tries<3:
    guess = int(input("Guess the number: "))
    tries+=1


if tries==3 and guess !=6:
    print("No attempt remianing")
elif tries==3 and guess==6:
    print("You got it")
else:
    print("you got it")'''


#print the number square
'''
for i in range(10):
    print('the square of' , str(i) , 'is ' , str(i**2))'''


#99 bottles
'''
for i in range(5, 0, -1):
  if i>1:
    print(f' {i}  bottles of beer on the wall')
    print(f' {i}  bottles of beer ')
    print('  Takes one down, pass it around')
    print(f' {i-1} {"bottle" if i-1==1 else "bottles"}  of the beer on the wall')
    print("###")
  else:
    #when there is only 1 bottle left
    print(f' {i}  bottle of beer on the wall')
    print(f' {i}  bottle of beer ')
    print(f'Takes one down, pass it around')

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
'''
'''
#Fizz Buzz

for i in range(1,16):
    if i%3==0 and i%5==0:
        print(f'{i} Fizzbuzz')
    elif i%5==0:
        print(f'{i} buzz')
    elif i%3==0:
        print(f'{i} Fizz')
    else:
        print(i)
 '''
'''
i = 0

while i < 6:
  print(f' i : {i}')
  j = 0
  print(f' j : {j}')
  while j < 6:
    print(f'multiply of i and j is {i * j}')
    j = j + 1
    print(f' j counter: {j}')
  i = i + 1
  '''
import random

lucky_number = random.randint(1, 9)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      break
    else:
      print(i)

print(f"Yay I got my lucky number {lucky_number}! 🍀")
