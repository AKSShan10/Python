'''
lst = [varname1, varname2, varname3]
dictionary = {
    "Key": "value"
}
'''
#set does not maintain order
set = {'Item 1', 'Item 2', 'Item 3'}
print(set)

set = {'Item 1', 'Item 2', 'Item 2', 'Item 3'}
print(set) #set merge the same variable

set.add('Item 4')
print(set)

set.remove('Item 2')
print(set)

