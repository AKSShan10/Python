from asyncore import read


with open('3. readme.txt','r') as file:
    print(file.read())

#
with open('3. readme.txt','r') as f:
    print(f.read())
    # we can not access 'f' outside of this indentation because python close trhis file

with open('3. readme.txt','r') as file:
    content = file.read()

print(f"The content is {content}")

