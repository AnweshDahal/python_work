#This is the second example of class
import random

class descision():

    def __initi__(self, myNumber, yourNumber):
        self.myNumber  = int(myNumber)
        self.yourNumber = int(yourNumber)
        #self.difference = int(difference)
        #self.score = int(score)

    def diff(self):
        #differ = self.myNumber - self.yourNumber
        return self.myNumber - self.yourNumber

    def reasult(self,diffee):
        yess = False
        while yess == False:
            if diffee != 0:
                score = 0
                print ("NO!!")
        
            else:
                score = 1
                print ("Yes!!")
                yess = True

        return score


def numberGenerator():
    myNumber = random.randint(0,20)
    return myNumber

playAgain = False

while playAgain == False:
    your = int(input("Your Number>.. "))
    game = descision(numberGenerator(),your)

    y = game.reasult(game.diff())

    c = 0

    c = c + y

    print ("Would You Like To Play Again?")
    ans = input(">.. ")

    if ans == "no":
        playAgain = True
        print (y)
        




