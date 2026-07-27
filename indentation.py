#Name:P.Chandu Srinvas
#Lab:06
#Task:01
#Program:Checking error by missing indent and fixing it
a=10;b=20
#if a>b:
#print("a is greater")
#else:
#print("b is greater")
#IndentationError: expected an indented block after 'if' statement on line 6
#correct program
if a>b:
    print("A is greater")
else:
    print("B is greater")
#Lab:06
#Task:02
#Program:nested for & if else
for i in range(1,11):
    if(i%2==0):
        print("even number")
    else:
        print("Odd number")
#Lab:06
#Task:03
#Program:writing correct code
x=10
if x>0:
    print("Positive")
else:
    print("Non-positive")
#Lab:06
#Task:Challenge
#Program:Three levels of indentation
n=int(input("enter the no of levels of triangle"))
if n>0:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

        