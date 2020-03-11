import random
t = int(input())

def avg(arr, n):
    return sum(arr)/n

def pick_rand_marks(n, m, _avg):
    a = []
    for i in range(n):
        num = random.randint(0, m)
        a.append(num)
    
    if avg(a, n) != _avg:
        return pick_rand_marks(n, m, _avg)
    
    return a

for it in range(t):
    n, m = map(int, input().split(" "))

    a = list(map(int, input().split(" ")))

    if n == 1:
        print(a[0])
        continue

    _avg = avg(a, n)
    best_a = 0
    best_arr = []
    for i in range(100):
        r = pick_rand_marks(n, m, _avg)
        
        if best_a < r[0]:
            best_a = r[0]
            best_arr = r.copy()
            if r[0] == m:
                break

    print(best_a)

