lst = ['string', 9, 3.14, ['A new item'], 'Shan']

print(lst)

for item in lst:
    print("The item is: ",item)

names = ['Tom', 'Jimmy']
print(names)

names.append('Charles')  #Adding a name
print(names)

names.remove('Charles') #removing a name
print(names)

Jimmy = names.pop() #deleting the last valu by using pop
print(names)