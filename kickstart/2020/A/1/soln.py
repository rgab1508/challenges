# t = int(input())

# for it in range(t):
#     n, b = map(int, input().split(" "))
#     bought = 0
#     a = list(map(int, input().split(" ")))
#     a.sort()
#     # print(a)
#     while(True):
#         if len(a) > 0:
#             if(b >= a[0]):
#                 b -= a[0]
#                 # print(a[0])
#                 a.pop(0)
#                 bought += 1
#             else:
#                 break
#         else:
#             break
    
#     print(f"case #{it+1}: {bought}")
import sys
t = int(input())


for it in range(t):
    n, b = map(int, input().split(" "))
    bought = 0
    a = list(map(int, input().split(" ")))
    a.sort()
    # print(a)
    i = 0
    while(i < n):
        if b >= a[i]:
            b -= a[i]
            # print(a[0])
            # a.pop(i)
            i += 1
            bought += 1
        else:
            break
    
    sys.stdout.flush()
    print(f"Case #{it+1}: {bought}")