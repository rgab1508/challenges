t = int(input())

for it in range(t):
    n = int(input())
    if n > 1:
        a = list(map(int, input().split(" ")))
    else:
        a = [int(input())]

    sub_s = []
    even_s = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            sub_s.append(i + 1)
        
        if a[i] % 2 != 0:
            even_s.append(i+1)

    if len(even_s) >= 2:
        if len(even_s) % 2 == 0:
            sub_s.extend(even_s)
        else:
            for i in range(len(even_s)-1):
                sub_s.append(even_s[i])


    if not len(sub_s):
        print(-1)
    else:
        print(len(sub_s))
        print(" ".join(map(str, sub_s)))
