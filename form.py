# This is a sample form for research candidates
""" Name Age Sex Weight Allergies Preferences Dislikes (Estimated Physical Activeness) (Recent Health Issues) """

print ("College Research Board")
print ("Candidates are asked to fill out the following form")
print ("To be the part of the research")
print ("Please answer correctly")
print ("Research on 'Effect of Food on a Person's daily Life'")

print ("Form:")

nameOK = False
"""
while nameOK == Fasle:
    
    if name == name.title():
        nameOK = True
    else:
        print ("Please Enter the Initials in Upper Case.")"""
name = input("Enter Your Name:\n>.. ")
ageOk = False


age = int(input("Enter your age:\n>.. "))
if age >= 18:
    ageOK = True
else:
    print ("Sorry You have to be above 18 years to take participation in this research")
    exit()

sex = input("Enter your Gender:\n>.. ")

for i in sex:
    sx = i
    break

weight = int(input("Enter your weight:\n>.. "))

print("This is your Identification Card")

print ("Name:", name.title())
print ("Age:" , age)
print ("Gender:",sx.title())
print ("Weight:" , weight)


