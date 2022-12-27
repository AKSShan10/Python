animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
for animal in enumerate(animals):
    print(animal)

for animal in enumerate(animals):
    print(animal)

for index, animal in enumerate(animals):
    print(index, animal)

for index, animal in enumerate(animals):
    if index%2==0:
        continue
    print(index, animal)

for index, animal in enumerate(animals):
    print(index+1, animal)