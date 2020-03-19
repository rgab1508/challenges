t = int(input())

# for it in range(t):
    # s = input()

n = 55
res = ""
while n > 0:
    index = (n-1) % 26
    # print(index)
    res += chr(index + ord("A"))
    n = (n-1)//26

print(str(reversed(res)))