t = int(input())

for it in range(t):
    n = int(input())

    a = list(map(int, input().split(" ")))
    a = set(a)
    print(len(a))
