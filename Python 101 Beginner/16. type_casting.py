# changing one data type to another data type

age = input( 'What is your age? ')
data_type = type(age)
print(data_type)

age = int(age)
data_type = type(age)
print(data_type)

dog_years = age*7
print(dog_years)



grocery_list = ['Apples', 'Orange', 'Bananas','Apples']
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))

grocery_list = ['Apples', 'Orange', 'Bananas','Apples']
grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))