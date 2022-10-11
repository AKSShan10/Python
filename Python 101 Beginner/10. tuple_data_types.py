'''
tuple vs list:
tuple is immutable. list mutable.
tuple can not be changed
We can iterate a tuple is loops
'''

animals = ["cat", 'dog', 'zebra', 'Aardvaark']
print(animals)
animals.sort()
print(animals)

foods =  ('Pizza','Orange','Apple','Pasta')
print(foods) 
#foods.sort() AttributeError: 'tuple' object has no attribute 'sort'

foods = ('Pizza','Orange','Apple','Fish')

for food in foods:
    print("The food is ",food)