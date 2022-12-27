# class ThisIsAnAnimal:
#     pass
#
# animal = ThisIsAnAnimal()
class Animal:
    this_is_a_property_1 = {
        'key_1' : 'value 1'
    }

    this_list = ['Kane', 'kalob','Gully']
    _like_this = 'This is a private property' #Can not access it from outside of this class

the_animal = Animal()
print(the_animal.this_is_a_property_1)
print(the_animal.this_is_a_property_1['key_1'])
print(the_animal.this_list[2])
print(Animal.this_list)
