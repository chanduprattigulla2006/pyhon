#Name:P.Chandu Srinvas
#Lab:07
#Task:01
#Program:Taking command line argument
import sys
print("Hello",sys.argv[0])
#Lab:07
#Task:02
#Program:Taking numbers using command line and finding the sum
n1=int(sys.argv[1])
n2=int(sys.argv[2])
if len(sys.argv==3):
    print("Sum=",(n1+n2))
else:
    print("invalid no of argumnets")
#Lab:07
#Task:03
#Program:Printing program name and length
print("Program name:",sys.argv[0])
print("No of arguments are",len(sys.argv))

