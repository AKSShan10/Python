items = ['rice', 'Apple', 'oil', 'sugar','cocacola']

for item in items:
    if item =='oil':
        continue # continue used to skip something
    print(item)

print()
print('BREAK:')
for item in items:
    if item =='oil':
        break
    print(item)


num = 0
while num < 20:
    #num = num+1
    if num % 2 == 0:
        num = num+1
    print(num)
    num=num+1
    
