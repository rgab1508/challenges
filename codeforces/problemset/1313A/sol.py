from math import factorial as fact


def calc_den(a: list):
    m = 1
    for i in range(len(a)):
        m *= fact(a[i])
    
    return m

t = int(input())

for it in range(t):
    a = list(map(int, input().split(" ")))
    s = 0
    den = calc_den(a)
    for i in range(len(a)):
        num = fact(a[i])
        s += num // den


    print(s)