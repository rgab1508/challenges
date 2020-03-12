n = int(input())

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

pairs = []


for i in range(n):
    for j in range(n):
        if i != j:
            if (a[i] + a[j]) > (b[i] + b[j]):
                if pairs.count([i, j]) == 0 and pairs.count([j, i]) == 0:
                    pairs.append([i,j])
        

        
# print(pairs)
print(len(pairs))