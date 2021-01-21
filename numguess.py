import random
usernumber = int(input("Please guess a number from 1 to 9 = "))
print (usernumber)
numguessed = int(random.randrange(1,9,1))
if  numguessed == usernumber:
        print('The number you guessed is PERFECT')
if  numguessed > usernumber:
        print('The number you guessed was LOW')
if  numguessed < usernumber:
        print('The number you guessed is HIGH')