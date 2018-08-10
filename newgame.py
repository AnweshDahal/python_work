# this is the third example of number guessing and scroing system
from random import randint

import sys

import time

def numGen(a,b):
    return randint(a,b)

def loopLogic(a):
    if a == 70:
        return 50
    elif a == 50:
        return 30
    elif a == 30:
        return 10
    else:
        return 5       

def mainGame(a):
    gotit = False
    fNum = numGen(-100,100)
    print (fNum + numGen(0,a) , " <--> " , fNum - numGen(0,a))
    myNumber = numGen(fNum,fNum+a)

    yy = loopLogic(a)-1
    for i in range(yy):
        yourAnswer = int(input(">.. "))

        if yourAnswer == myNumber:
            print ("Eureka!!")
            score = 1
            break
        
        if yourAnswer == 101001101011:
            print (myNumber)

        else:
            y = (loopLogic(a)-1) - i
            print("Wrong! you have " , y , " tries left.")
    
    if score == 1 and i != loopLogic(a):
        print ("Well Done!")

print ("Choose a difficulty:")

time.sleep(0.2)

print ("Easy")

time.sleep(0.2)

print("Medium")

time.sleep(0.2)

print("Hard")

time.sleep(0.9)

ex = "Extreme"

for i in ex:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.2)

print("\n")

ans = input("Your Answer(in lower case)>.. ")

if ans == "easy":
    mainGame(70)

elif ans == "medium":
    mainGame(50)

elif ans == "hard":
    mainGame(30)

else:
    mainGame(5)

def loop():
    pass

def logic(ans):
    pass