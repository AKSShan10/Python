class Animal:
    #fur_color = "orange"
    animal_type = 'Unknown'

    def __init__(self, fur_color ):
        # print(f"Fur color is{fur_color}")
        self.fur_color = fur_color
    def speak(self):
        raise NotImplementedError
        #print("Raawwwwwwr")

    def eat(self):
        print("I am eating yum yum yum")
    def chase(self, animal='Gazelle'):
        print("I am chasing a", animal)
class HouseCat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("fur color was saved to the class Object")
        self.animal_type = "House cat"
        print(self.animal_type)


    # def speak(self):
    #     print('Meeeowwwwww')
    #
    # def eat(self):
    #     #wrong way: Animal.eat()
    #     super().eat()
    #     print("I am eating Salmon")
    #
    # def chase(self, animal):
    #     super().chase(animal)
    #     print(animal, "was caught")

    def get_fur_color(self):
        print("Getting fur color ",self.fur_color)

cat = HouseCat("Grey")
#cat.get_fur_color()
#cat.speak()
#cat.eat()
#cat.c("Mouse")