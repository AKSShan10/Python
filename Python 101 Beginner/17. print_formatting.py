name = input("Enter a name: ")

welcome_message = "Hello {} welcome to Python 101".format(name)

print(welcome_message)

#Another way called f string

welcome_message = f"Hello {name} welcome to Python 101"
#oldway
welcome_message = f"Hello %s welcome to Python 101"%name
print(welcome_message)