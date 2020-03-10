n = int(input())

s = input()
s = list(s)

start = True
step = 0
for i in range(len(s)):
    if start and s[i] != "(":
        s[i] = "("
        start = False
        step += 1
        continue
    elif not start and s[i] != ")":
        s[i] = ")"
        start = True
        step += 1
        continue

print(s)
print(step)