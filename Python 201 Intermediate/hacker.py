import numpy as np

n,m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)],int)

print(np.min(arr, axis=1))
y = sorted(output, reverse=True)