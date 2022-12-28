class Animal:
    fur_color = "orange"

    def speak(self):
        raise NotImplementedError
        #print("Raawwwwwwr")

    def eat(self):
        print("I am eating yum yum yum")
    def chase(self, animal='Gazelle'):
        print("I am chasing a", animal)
class HouseCat(Animal):
    def speak(self):
        print('Meeeowwwwww')

    def eat(self):
        #wrong way: Animal.eat()
        super().eat()
        print("I am eating Salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
#cat.speak()
#cat.eat()
cat.chase("Mouse")