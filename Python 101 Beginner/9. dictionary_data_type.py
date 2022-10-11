person = {
    "key" : "value",  #key should be string, value can be any value. For example it can be int, float, list
    "name": "Shan",
    "twitter" : "@AKSShan2"
}

print(person['twitter'])

print(person)

person['fb'] = 'Aks Shan'
print(person)

del person['key'] #deleting a key
print(person)