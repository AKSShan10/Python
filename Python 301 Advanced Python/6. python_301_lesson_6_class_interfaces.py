class Animal:
    fur_color = "orange"

    def speak(self):
        raise NotImplementedError
        #print("Raawwwwwwr")

    def eat(self):
        raise NotImplementedError
    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print('Meeeowwwwww')

    def eat(self):
        print("Fish")

cat = HouseCat()
cat.speak()
cat.eat()



