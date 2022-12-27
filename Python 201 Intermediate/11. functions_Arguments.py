#n = int(input())
#arr = map(int, input().split())
#print(arr)
lst = {1,4,2,3,4}
j = sorted(lst,reverse=True)
print(j)

#def thing(bame,*args)

def add_numbers(name, *args):
    print("args", args)
    print('type', type(args))
    print(type(name))
    total = 0
    for num in args:
        total= total+num
    return total

total = add_numbers('Shan',1,3,5,7,9)
print(total)