n = int(input())
c1 = 0

while c1<n:
    arr = []
    ai = int(input())
    c2 = 0

    while c2<ai:
        aj = int(input())
        arr.append(aj)
        c2+=1

    step = 0
    while len(arr)>1:
        aii = int(input())
        ajj = int(input())
        if arr[aii]>=arr[ajj]:
            step+=1
            
    print(step)
    c1+=1

