""""

input an integer value

if it's divisible by 11, print a
if it's divisible by 9, print b
if it's divisible by 7, print c
if it's divisible by 2, print d 
everything else print e


example cases
input: 63
output: bc

input: 22
output: ad



put it on your github repository.

x = float(input("enter edge 1"))
y = float(input("enter edge 2"))
z = float(input("enter edge 3"))

if x + y > z and x + z > y:
    print(x + y + z)
else:
    print ("input invalid")


Score = int(input("enter score :"))

if(Score == 100):
    print("A+")
elif (99 > Score > 90):
    print("A")
elif (89 > Score > 80):
    print("B")

""""

