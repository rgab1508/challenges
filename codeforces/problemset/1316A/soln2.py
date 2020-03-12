from random import randint
t = int(input())

def avg(arr, n):
    # print(f"arr: {sum(arr)/n}")
    return sum(arr)/n
    
def pick_rand_arr(n, m, _avg):
    a = []
    for i in range(n):
        a.append(randint(0, m))

    if sum(a) != (n * _avg):
        return pick_rand_arr(n,m,_avg)
    else:
        return a

for it in range(t):
    n, m = map(int, input().split(" "))


    a = list(map(int, input().split(" ")))

    if n == 1:
        print(int(avg(a, n)))
        break

    _avg = avg(a, n)

    best_a = 0
    best_arr = []
    for i in range(100):
        r = pick_rand_arr(n, m, _avg)

        if best_a < r[0]:
            best_a = r[0]
            best_arr = r.copy()

            if best_a == m:
                break

    print(best_a)