t = int(input())


for it in range(t):
    n, d = map(int, input().split(" "))

    a = list(map(int, input().split(" ")))

    for i in range(d):
        for i in range(1, len(a)):
            if a[i] > 0:
                a[i] -= 1
                a[i-1]+=1
                break
        
    print(a[0])