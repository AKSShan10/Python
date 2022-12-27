# class ThisIsAnAnimal:
#     pass
#
# animal = ThisIsAnAnimal()
class Animal:
    this_is_a_property_1 = {
        'key_1' : 'value 1'
    }

    this_list = ['Kane', 'kalob','Gully']

    def add_name(self,name):
        self.this_list.append(name)
        return self.this_list
    def this_is_a_method(self):  # self hasaccess everything on a particular class
        print(self.this_list)

    @property
    def get_gully(self):
        return self.this_list[2]



the_animal = Animal()
the_animal.this_is_a_method() # We are calling thhe method
gully = the_animal.get_gully
print("The cutestgate of all time is", gully)
the_animal.add_name("Rhubarb")
print(the_animal.this_list)