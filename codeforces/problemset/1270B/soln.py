t = int(input())


for it in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    # print(n, a)

    max_a = max(a)
    min_a = min(a)

    # print(max_a, min_a)

    k = len(a)
    while k > 1:
        if max_a - min_a >= k:
            print("YES")
            break
        elif max_a - min_a < k:
            pass
            # print("NO")
            