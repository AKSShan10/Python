fav_foods = ['Pizza', 'Tacos', 'Salmon']

for food in fav_foods:
    print(f'My favourite food is {food}')

for food in fav_foods:
    if food == "Pizza":
        size = input("What size pizza would you like?")
        print(f"You ordered a {size} pizza")

fav_foods = set(fav_foods)
for food in fav_foods:
    print(food)



food = "Pizza!"
for letter in food:
    print(letter)

person = {
    "name": "Kalob",
    "twitter": "@KalobTaulien",
    "instagram": "@coding.for.everybody"
}
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")