from random import randint
# this imports a module that generates a random number in the given range
from time import sleep
# this imports a module that a module that imports a time keeper
# but since python is an interpreter i still have no idea how to run this module simultaneously with the rest of the program
import sys
#import responses
"""def responses(type):
	def way_off_high():
		responses = ["Woah buddy calm down that's too high.","Even I don't go that high."]
		return resonses[random.randint(0,len(responses))]

	def too_high():
		responses = ["You might want to step it down.","Getting Close"]
"""

#lower_value = int(input("Enter the lower value>.. ")) This was a beta feature that let an user to select a manual range
#upper_value = int(input("Enter the upper value>.. ")) Same as above

#The line below is just for a s t h e t i c purpose
print("I am Thinking of a number. Can you guess it?")
sleep(0.5)
#the line above will delay the printing of the next line by 0.5 second
print ("Choose a difficulty")

sleep(0.5)

print("Easy")
"""for eesy in esy:
	sys.stdout.write(eesy)
	sys.stdout.flush()
	sleep(0.1)"""

sleep(0.5)
#print("\n")

print("Medium")

"""for mdmd in mdm:
	sys.stdout.write(mdmd)
	sys.stdout.flush()
	sleep(0.1)"""

sleep(0.5)
#print("\n")
print("Hard")
"""for hrdd in hrd:
	sys.stdout.write(hrdd)
	sys.stdout.flush()
	sleep(0.1)"""

sleep(0.5)
#print("\n")

# now we generate a random number and return a value
def numbergen(a,b):
	my_numb = randint(a,b)
	return my_numb
#the function above is generated
my_number = numbergen(0,2000)
#now we take your answer
yy = "Your Answer? (in lowercase) "
for char in yy:
	sys.stdout.write(char)
	sys.stdout.flush()
	sleep(0.05)
your_answer = input()
#i did this on purpose and the line below has no general but a specific purpose
achieve = False


#this is a fancy feature to choose a difficulty
if your_answer == "easy":
	print ("It's Between:")
	print (my_number - randint(0,100),"<-->",my_number + randint(0,100))
	#print (my_number + randint(0,100))

elif your_answer == "medium":
	print ("It's Between:")
	print (my_number - randint(0,500),"<-->",my_number + randint(0,500))
	#print (my_number + randint(0,500))

elif your_answer == "hard":
	print ("It's Between:")
	print (my_number - randint(0,2000),"<-->",my_number + randint(0,2000))
	#print (my_number + randint(0,2000))

else:
	print ("It's Between:")
	print (0)
	print (2000)

#print(my_number)
# as you can see the line below uses the achieve variable
while achieve == False:
	your_number = int(input("Enter Your number >.. "))

	if your_number == 101001101011:
		y = int(input("Which? "))
		if y == 99999:
			print (my_number - randint(0,10))

		elif y == 123123123:
			print (my_number)
		else:
			print ("NO!!")



	elif your_number < my_number:
		if my_number - your_number < 5:
			print ("Almost There")

		elif my_number - your_number < 20:
			print ("A Bit Low Try Again!")

		else:
			print ("Way Off Try Again!!")
			sleep(0.05)
			print("What I meant was raise the number!")

	elif your_number > my_number:
		if your_number - my_number < 5:
			print ("Almost There")

		elif your_number - my_number < 20:
			print ("A Bit High Try Again")

		else:
			print("Way Off Try Again!!")
			sleep(0.05)
			print("What I meant was lower the number!")

	else: #you did it
		print ("Eureka!!!")
		sleep(0.5)
		print("Thanks For Playing!!")
		achieve = True
