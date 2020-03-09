import random
t = int(input())

def check_good(arr, N):
    f = False
    for m in range(N):
        for n in range(N):
            if m < n:
                if ((n - arr[n]) != (m - arr[m])):
                    print(n - arr[n], (m - arr[m]))
                    f = True

    return f


for i in range(t):
    N = int(input())

    a = list(map(int, input().split(" ")))

    while(not check_good(a, N)):
        # print(a)
        random.shuffle(a)

    print(a)