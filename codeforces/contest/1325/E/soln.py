import math
n = int(input())

a = list(map(int, input().split(" ")))

s = set(a)
if len(s) < len(a):
    print(2)
    exit()

def arr_prod(n):
    prod = 1
    for i in range(n):
        prod *= a[i]

    return prod

best_n = float("inf")
for i in range(1, n+1):
    prod = arr_prod(i)

    # print(prod, math.sqrt(prod))
    if math.sqrt(prod).is_integer():
        if i < best_n:
            best_n = i
    
if best_n == float("inf"):
    print(-1)
    exit()

print(best_n)