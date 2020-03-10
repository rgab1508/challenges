n = int(input())

s = input()
s = list(s)

# print("".join(s))
step = 0

if n % 2 != 0:
    print(-1)
    exit()

i = 0
while(i < len(s)):
    ch = False
    if s[i] == "(" and s[i+1] == ")":
        step+=0
    if s[i] == ")":
        s[i] = "("
        ch = True
    if s[i+1] == "(":
        s[i+1] = ")"
        ch = True
    if ch:
        step+=2
    i += 2

print(step)
# print("".join(s))