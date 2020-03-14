import math
t = int(input())

def lcm(a, b):
    return (a*b)/math.gcd(a, b)

for it in range(t):
    x = int(input())

    for a in range(1, x):
        for i in range(1, a):
            _ = i* (x-i)/a
            # print(_)
            if _.is_integer():
                if _ < x:
                    print(math.gcd(a, int(_)), lcm(a, int(_)), x)