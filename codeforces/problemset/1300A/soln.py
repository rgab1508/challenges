import random
t = int(input())


def mult(a:list):
    m = 1
    for i in range(len(a)):
        m *= a[i]

    return m

def fix_arr(a: list):
    pass



for it in range(t):
    n = int(input())

    a = list(map(int, input().split(" ")))
    c = 0

    for i in range(n):
        if a[i] == 0:
            a[i] += 1
            c += 1
    
    while sum(a) == 0 or mult(a) == 0:
        a[0] += 1
        c += 1


    print(c)