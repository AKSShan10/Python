distance = int(input())

step = 0

output = distance//5

if distance %5==0:
    step = output
else:
    step = output+1

print(step)