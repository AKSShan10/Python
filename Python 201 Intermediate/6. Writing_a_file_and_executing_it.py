from fileinput import filename


filename = input('Please enter your filename: ')
content = input('Please enter the content: ')

with open(filename,'w') as file:
    file.write(content)

open_file = input("Would you like to read this file? ")
if open_file in ['y', 'n']:
    if open_file == 'y':
        with open(filename, 'r') as file:
            print(file.read())