from re import L


lst = [0, 1, 2, 3, 4, 5]
print(lst[0])

lst = ['One', 'Two', 'Three'] ##offset = 2
 #       0       1       2
                    

print(lst[2])

b = True
#print(b[0]) #TypeError: 'bool' object is not subscriptable

lst = ['One', 'Two', 'Three', 'Four', 'Five']
print(lst[0:3])
print(lst[2::])
print(lst[-1])
print(lst[-2::])

course = 'Python 101'
print(course[5])