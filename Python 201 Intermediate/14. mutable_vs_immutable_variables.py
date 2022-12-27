"""""
mutable vs immutable
changable vs unchangable
List are mytable & string immutable
"""

string = "The fox jumped over the cow"
print(string.upper())
print(string)

string = "Overwritten"
print(string.upper())
print(string)

name = ["A", "B", "C"]
name.append("D")
print(name)