n = int(input())

a = list(map(int, input().split(" ")))

summ = 0
s = []

for i in range(n):
    for j in range(i+1, n):
            # print(a[i], a[j], a[i]^a[j])
            s.append(a[i] + a[j])

summ = s[0]

for i in range(1, len(s)):
    summ ^=  s[i]     

print(summ)