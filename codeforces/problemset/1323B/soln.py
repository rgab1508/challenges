l1 = input().split(" ")
n, m, k = int(l1[0]), int(l1[1]),int(l1[2])

a = list(map(int, input().split(" ")))

b = list(map(int, input().split(" ")))

c = [list() for x in range(n)]

for i in range(n):
    for j in range(m):
        # print(i, j)
        c[i].append(a[i] * b[j])

print(c)

def check_sub(i, j):
    global m, k, c
    f = True
    if j + k > m :
        return False
    for _j in range(k):
        if not (_j +k > m):
            if c[i][j+_j] != 1:
                f = False

    return f

count = 0

for i in range(n):
    for j in range(m-1):
        if c[i][j] == 1:
            if(check_sub(i, j)):
                count += 1
            
print(count)