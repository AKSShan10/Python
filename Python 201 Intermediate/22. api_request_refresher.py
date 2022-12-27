import requests

req = requests.get("https://swapi.dev/api/people/2/")

person = req.json()
print(f"Name is {person['name']}")
print(f"Birth year is {person['birth_year']}")

print("Film involve in: ")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print(f"Film is {film['title']}")
