#this is an example of class
from time import sleep
import sys

class Dogs():

    def __init__(self, name, color, breed, height, weight, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.height = height
        self.weight = weight
        self.age = age

    def giveIntroduction(self):
        print ("Woof")
        sleep(0.5)
        print ("Woof")
        sleep(0.1)
        print ("Sorry! initiating Translator")
        dotdot = "..........................................................."
        for dot in dotdot:
            sys.stdout.write(dot)
            sys.stdout.flush()
            sleep(0.15)
        print("\n")
        print ("My name is " + self.name + ".")
        sleep(0.5)
        print ("I am a " + self.color + "doggo.")
        sleep(0.5)
        print ("I am a " + self.breed)
        sleep(0.5)
        print ("I am " + self.height + " centimeter tall.")
        sleep(0.5)
        print ("I weigh " + self.weight + " kilos.")
        sleep(0.5)
        print ("I am not that heavy.")
        sleep(0.5)
        print ("I am " + self.age + " years old.")


dg = Dogs("Lola", "White", "Siberian Husky","54","42","6")
dg.giveIntroduction()
