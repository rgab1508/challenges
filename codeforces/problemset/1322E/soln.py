n = int(input())

a = list(map(int, input().split(" ")))

b = a.copy()

def median(arr):
    return sorted(arr)[1]

c = 0
while(True):
    for i in range(1, len(a)-1):
        a[i] = median([b[i-1],b[i], b[i+1]])
    
    if(a == b):
        if c == 0:
            print(c)
            print(" ".join(map(str, a)))
        break


    c += 1
    # print(b)
    # print(c)
    # print(" ".join(map(str, a)))
    b = a.copy()

print(c)
print(" ".join(map(str, a)))