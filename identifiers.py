#Program:Valid Identifiers
#lab:01
#task:01
name="chandu_srinvas"
PI=3.14
def hello():
    print("HELLO_WORLD")
class grade:
    pass
student_marks=64
print(name)
print(PI)
print(hello)
print(grade)
print(student_marks)
#Lab:01
#Task:02
#Program:invalid identifiers
2value=5
value_2=20
_hidden="no"
class=5
my-var
#Here 2value is an invalid variable because its sarting with digit
#value_2 is valid variable beacause its following identifier naming rules
#_hidden is valid variable
#class is an invalid variable because its a keyword
#may-var is invalid variable because it contains a hyphen
#MyClass is valid variable
# total$ is inavlid variable because it contains '$' symbol
#ouput
#SyntaxError: invalid syntax
#Lab:01
#Task:03
#Program:Case Sensitivity of Identifiers
Sum=45
sum=18
print(Sum)
print(sum)