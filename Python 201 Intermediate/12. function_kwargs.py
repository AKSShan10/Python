#kwargs is like a dictionary type
def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print('You are ',kwargs.get('age'))

person(name = 'ABC', age=20, brain='huge')

def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")
    print(f"Shipping it to {address}")
    price = 18.00

    for key,value in toppings.items():
        price = price+2.00
    print(f"Total price is {price}")
    return price

total_price = order_pizza("X", "Uganda",jalapinos=True, extra_cheese=True, ham=True )