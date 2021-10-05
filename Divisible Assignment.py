"""

x = float(input("enter edge 1"))
y = float(input("enter edge 2"))
z = float(input("enter edge 3"))

if x + y > z and x + z > y:
    print(x + y + z)
else:
    print ("input invalid")

"""
"""""
Score = int(input("enter score :"))

if(Score == 100):
    print("A+")
elif (99 > Score > 90):
    print("A")
elif (89 > Score > 80):
    print("B")

"""""

Number = int(input("Enter Number:"))

if(Number % 11 == 0):
    print("a")
else:
    print("b")