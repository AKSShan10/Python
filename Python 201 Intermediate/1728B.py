trial = int(input())
 
while trial>0:
    n = int(input())
    c = 1
    lst = []
    while c<=n:
        lst.append(c)
        c+=1
 
     
    c = n%2
    while c<n-2:
        temp = lst[c]
        lst[c] = lst[c+1]
        lst[c+1] = temp
        c+=2
 
    for i in lst:
        print(i,end=" ")
    print()
    trial-=1