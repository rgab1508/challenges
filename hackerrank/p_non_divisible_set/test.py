
ss = []
s = [124, 149, 278, 282, 338, 410, 436, 575, 576, 702, 718, 771]
k = 7
n = len(s)
s = list(set(s))
s = sorted(s)
blacklist = []
for i in range(n):
    for j in range(n):
        # print(f"{s[i]}+{s[j]}: {s[i]+s[j]} :{(s[i]+s[j]) % k}")
        if (s[i] + s[j]) % k != 0:

            if s[i] not in ss and s[i] not in blacklist:
                ss.append(s[i])
        else:
            print(f"{s[i]}+{s[j]}: {s[i]+s[j]} :{(s[i]+s[j]) % k}")
            blacklist.append(s[i])
            if s[i] in ss:
                ss.remove(s[i])

    
print(ss)
