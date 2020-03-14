t = int(input())

for it in range(t):
    n = int(input())
    
    a = list(map(int, input().split(" ")))
    p = False
    for i in range(n):
        c = a[i]
        palindrome = False

        for j in range(i+2, n):
            if a[j] == c:
                p = True
                palindrome = True
                print("YES")
                break
        
        if palindrome:
            break
    if not p:
        print("NO")