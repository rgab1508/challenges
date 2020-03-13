t= int(input())
# t = 1

for it in range(t):
    N = 0
    s = input()
    # s = "1111000"
    s = list(s)

    zero =False
    prevI = -1
    for i in range(len(s)):
        if s[i] == "1":
            prevI = i
            break

    for i in range(prevI+1, len(s)):
        if s[i] == "1":
            if i - prevI > 1:
                N += i - prevI - 1
                prevI = i
            elif i - prevI == 1:
                prevI = i

    print(N)
