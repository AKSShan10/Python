class Animal:
    fur_color = "orange"

    def speak(self):
        print("Raawwwwwwr")

    def eat(self):
        pass
    def chase(self):
        pass



class Tiger(Animal): # Extending tiger class to Animal class
    def speak(self):
        print("They are Great! & \nnot inheriting")

class HouseCat(Animal):
    fur_color = "Black" # will not inherit color from Animal class
    def speak(self):
        print("Meow")


tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)
#print(type(tiger))
