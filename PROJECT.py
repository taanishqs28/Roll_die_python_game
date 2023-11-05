'''
PYTHON PROJECT(GAME)
Developed by	: TAANISHQ SETHI
'''
#introduction of the game
print('WELCOME TO ROLL THE DICE GAME!!!!')
#welcoming the user
import time
time.sleep(1)
name = input("What is your name? ")
print("Hello",name, "Time to play roll the dice!")
import time
time.sleep(1)
import random
min = 1
max = 6
roll_again = "yes"
SCORE=0
while roll_again == "yes" or roll_again == "y"or roll_again=="Y":
    import time
    time.sleep(0.5)
    a=random.randint(min, max)
    b=random.randint(min, max)
    value1=int(input('guess the first no(between 1 and 6)'))
    value2=int(input('guess the second no(between 1 and 6)'))
    import time
    time.sleep(1)
    print ("Rolling the dices...")
    import time
    time.sleep(1)
    print ("The values are....")
    import time
    time.sleep(1)
    print (random.randint(min, max))
    print (random.randint(min, max))
    if a==value1 or b==value2:
        print('YOU GOT 1 RIGHT!!')
        print('TRY AGAIN')
        SCORE+=5
    if a==value1 and b==value2 :
        print('YOU WON')
        SCORE+=10
    if a!=value1 and b!=value2:
        print('YOU LOST')
        SCORE-=5
    roll_again =input("Roll the dices again?")
    if roll_again=="no" or roll_again=="n":
        print('see you next time')
        break
if SCORE >0:
    print('YOU WON ','$',SCORE)
if SCORE <0:
    print('you have to pay','$',-(SCORE),'to owner of this game') 
if SCORE <0:
    print('TOTAL SCORE= 0')
    print('BETTER LUCK NEXT TIME')
