'''''
To write a function in python, we use:
def somename():
    pass
'''
def somename():
    print(f"Hello world!")

somename()


def somename(name):
    print(f"Hello {name}")
somename('aks')


def somename(name,food):
    print(f"Hello {name}. Let's eat {food}.")
somename('aks','pizza')


def somename(name,food='pizza'):
    print(f"Hello {name}. Let's eat {food}.")
somename('aks')


def somename(name,food='Pizza'):
    print(f"Hello {name}. Let's eat {food}.")
somename('aks','Burger')


def somename(name,food='Pizza'):
    print(f"Hello {name}. Let's eat {food}.")
somename('aks',food='Burger')

def somename(name=None, food="Pizza"):
    if name is None:
        name = "Zephyr"

    person_type = "human"
    if name == "Zephyr":
       person_type = "Cat"

    print(person_type)

    print(f"Hello {name}. Let's eat some {food}")

somename()


some_var = somename()
print("The variable is ", some_var)


def somefunction():
    return "a value"
thing = somefunction()
print(thing)


def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp(33, 6)
big_number2 = exp(12, 12)
print(big_number)
print(big_number2)