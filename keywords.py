#Lab:02
#Task:01
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#Lab:02
#Task:02
print(keyword.iskeyword("if"))
print(keyword.iskeyword("False"))
print(keyword.iskeyword("async"))
print(keyword.iskeyword("name"))
print(keyword.iskeyword("student"))
print(keyword.iskeyword("def"))
print(keyword.iskeyword("or"))
#Lab:02
#Task:03
#Keywords as Variable names
for=5
True=10
#for=5
#   ^
#SyntaxError: invalid syntax
#True=10
#    ^
#SyntaxError: cannot assign to True
#Lab:02
#Task:Challenge
print(keyword.softkwlist)
print(len(keyword.softkwlist))
