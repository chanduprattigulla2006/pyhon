#Name:P.Chandu Srinvas
#Lab:05
#Task:01
#Program:Next year age claculator
name=input("Whats your name??")
age=int(input("Whats your age??"))
print(f"Hello {name},you will turn {age+1} next year")
#Lab:05
#Task:02
#Program:Type conversion and performing arithmetic operations
a,b=map(int,input("Enter two values").split())
print("sum=",a+b)
print("subtraction=",a-b)
print("product=",a*b)
print("division=",a//b)
#Lab:05
#Task:03
#Program:Output Formatting Methods
name="Ram Sai" 
age=18
#Comma separate
print("Name:",name,",Age:",age)
#str.format()
print("Name :{} ,Age : {}".format(name,age))
#f-string
print(f"Name:{name}, Age:{age}")
#Lab:05
#Task:04
#Program:Taking various inputs using single input function
n1,n2,n3=map(int,input("Enter three numbers:").split())
print("Sum of three numbers is:",n1+n2+n3)
#Lab:05
#Task:Challenge
#Program:Average of subject marks
tel,hin,eng=map(int,input("Enter telugu,hindi,english marks"))
avg=(tel+hin+eng)/3
print(f"Average of marks is avg:.2f")

