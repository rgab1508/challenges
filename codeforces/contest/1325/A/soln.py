import math
t = int(input())

def lcm(a, b):
    return (a*b)/math.gcd(a, b)

for it in range(t):
    n = int(input())

    found = False
    for i in range(1, 1000):
        for j in range(1, 100):
            if math.gcd(i, j) + lcm(i, j) == n:
                found = True
                print(i, j)
                break
        if found:
            break