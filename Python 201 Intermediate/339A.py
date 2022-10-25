n = input()
lst = []
l = int(len(n))
if len(n)>1:
    sym = n[1]
else:
    sym=""
 
for i in range(0,l):
    if i%2==0:
        lst.append(n[i])


for i in range(0,len(lst)):
    temp = int(lst[i])
    lst[i] = temp

lst = sorted(lst)
f = []
for i in lst:
    st = str(i)
    f.append(st)
    
if len(n)>1:
    mystring = ''
    for i in f:
        mystring +=i+sym

    fstring = mystring.rstrip(mystring[-1])
    print(fstring)
else:
    print(n)