l1 = input().split(" ")
n, m, k = int(l1[0]), int(l1[1]),int(l1[2])

a = list(map(int, input().split(" ")))

b = list(map(int, input().split(" ")))

c = [list() for x in range(m)]

for i in range(n):
    for j in range(m):
        print(i, j)
        c[i].append(a[i] * b[j])

# print(c[0][0])

for i in range(1):
    