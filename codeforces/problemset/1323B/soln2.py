l1 = input().split(" ")
n, m, k = int(l1[0]), int(l1[1]),int(l1[2])

a = list(map(int, input().split(" ")))

b = list(map(int, input().split(" ")))

c = [list() for x in range(n)]

for i in range(n):
    for j in range(m):
        # print(i, j)
        c[i].append(a[i] * b[j])

# print(c)
cl = []
for i in range(n):
    for j in range(m):
        cl.append(c[i][j])


def check_sub(i):
    global cl, k
    f =True
    start = i
    end = i + k
    for _i in range(start, end):
        if _i + k < len(cl):
            if cl[_i] != 1:
                f = False

    return f

count = 0
for i in range(len(cl)):
    if cl[i] == 1:
        if(check_sub(i)):
            count += 1

print(count - 1)