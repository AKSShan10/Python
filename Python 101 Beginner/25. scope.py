'''
when variable exist inside a function, we can not access it from outside. It is called scope.
'''

#Error
#def myfunc():
#    name = 'aks'
#    return name

#myfunc()
#print(name)

name = 'Aks'
def myfunc():
    return name
print(myfunc())


name = 'Aks'
def myfunc():
    name = 'New name'
    return name
print(myfunc())
print(name)
