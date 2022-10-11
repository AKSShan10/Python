can_code = True

if can_code == True:
    print("You can code!")
else:
    print("You do not know how to code yet.")


teacher = 'Mr. X'

if teacher == 'Mr. X':
    print('Show the teacher portal')
else:
    print('You are a student')
    

name = input("What is your name? ")

if name == 'Bob':
    print('Welcome Bob')
    bring_Food = 'Pizza'
elif name == 'Jhon':
    print('Welcome Jhon')
    bring_Food = 'Burger'
else:
    print('You are not Bob. Get out from here')
    bring_Food = 'Salmon'

print(f"You are eating {bring_Food}")