t = int(input())


for it in range(t):
    tab = {}
    m, n = map(int, input().split(" "))

    f = list(map(int, input().split(" ")))
    p = list(map(int, input().split(" ")))
    for i in range(len(f)):
        tab[f[i]] = 0

    for i in range(len(p)):
        tab[f[i]] += p[i]

    print(tab)
