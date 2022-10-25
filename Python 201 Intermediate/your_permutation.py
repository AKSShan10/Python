trial = int(input())
 
while trial>0:
    n = int(input())
    c = 1
    lst = []
    while c<=n:
        lst.append(c)
        c+=1
 
    lst1 =[]
    #print("lst5 ",lst[5])
    if n%2 == 0:
        i = n//2
        m = i-1
        #print("m",m)
        l = n-1
        #print("l",l)
        c = 0
        #lst1 =[]
        while c<i:
            temp1 = lst[m]
            #print("temp1", temp1)
            temp2 = lst[l]
            #print("temp2",temp2)
            lst1.append(temp1)
            lst1.append(temp2)
            l=l-1
            m=m-1
            c=c+1
    else:
        i = n//2
        m = i
        #print("m",m)
        l = n-1
        #print("l",l)
        c = 0
        #lst1 =[]
        while c<i:
            temp1 = lst[m]
            #print("temp1", temp1)
            temp2 = lst[l]
            #print("temp2",temp2)
            lst1.append(temp1)
            lst1.append(temp2)
            l=l-1
            m=m-1
            c=c+1
        lst1.append(1)
        

    for i in lst1:
        print(i,end=" ")
    print()
    trial-=1