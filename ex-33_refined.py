# While - Loops

i = 0
numbers = []
b = int(raw_input("Enter a no: "))
c = b + 1
g = int(raw_input("Enter the increment in numbers: "))
h = list()
while i < c:
    print "At the top i is %d" % i
    numbers.append(i)
	  
    i = i + g
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i 
	  
	  
print "The numbers: "

for num in numbers:
     h.append(num)
	 
print h

print "NEXT PROCESS>>>>>>>>>>>>>>>",raw_input()

numbe = list()
o = int(raw_input("Enter e Numbah :>>>>>>"))
q = o + 1 
u = list()
for s in range(0, q):
   print "Numbers now: "
   numbe.append(s)
   print numbe
   print "At the bottom o is: %d" % s
   
print "The numbers: "

for b in numbe:
    print b

	
	

