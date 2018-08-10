#This is an example of Class.
# The line below imports sleep() function form time which can be used to delay the suceeding outputs.
from time import sleep
# I imported the whole sys because we will be using a lot of its components
import sys
# Now we create a class named Dogs
class Dogs():
  # we make a container to prevent errors in future and make our code look more managed  
    def __init__(self, name, color, breed, height, weight, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.height = height
        self.weight = weight
        self.age = age
    # now a function
    def giveIntroduction(self):
     #fancy Stuff   
        print("Man: What's your name?")
        # Whats the purpose of the line below?
        sleep(0.5)

        print ("Woof!!")
        # it will delay the execution of the line below by
        sleep(0.2)
        # 0.2 seconds or 200 milliseconds
        print ("Woof!!")

        sleep(0.1)

        print ("Sorry! Initializing Translator.")

        dotdot = "............................................................"
        # The codes below from 35 38 prints the dots in dotdot individually
        for dot in dotdot:
            sys.stdout.write(dot) #stdout is linux for print
            sys.stdout.flush()
            sleep(0.2)

        print("\n")

        print ("My name is " + self.name + ".")
        
        sleep(0.5)

        print ("I am a " + self.color + " doggo.")

        sleep(0.5)

        print ("I am a " + self.breed + ".")

        sleep(0.5)

        print ("I am " + self.height + " centimeter tall.")

        sleep(0.5)

        print ("I weigh " + self.weight + " kilos.")

        sleep(0.5)

        print ("I am not that heavy.")

        sleep(0.5)

        print ("I am " + self.age + " years old.")
    #now we make an object
dog1 = Dogs("Bella", "Golden Brown", "Beagle","35", "9", "5")
dog2 = Dogs("Ace", "White", "Siberian Husky", "58", "26", "6" )
    # we made 2 objects
dog1.giveIntroduction()
dog2.giveIntroduction()
#now they are executed
        



