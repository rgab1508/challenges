n = int(input())

s = input()
s = list(s)

# print("".join(s))
step = 0

if n % 2 != 0:
    print(-1)
    exit()

for i in range(len(s)):
    if i % 2 == 0 and s[i] != "(":
        s[i] = "("
        step += 1
        continue
    elif i % 2 != 0 and s[i] != ")":
        s[i] = ")"
        step += 1
        continue


print(step)
print("".join(s))