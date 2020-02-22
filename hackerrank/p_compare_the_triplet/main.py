
# f = open("a.in")
# alice = f.readline().strip().split(" ")
# bob = f.readline().strip().split(" ")

# # print(alice, bob)
# alice_score = 0
# bob_score = 0

# for i in range(len(alice)):
#     if alice[i]> bob[i]:
#         alice_score += 1
#     else:
#         bob_score += 1
    

# print(alice_score, bob_score)

arrrr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    # Write your code here
    pdd = [[1,1],[2,2],[3,3]]
    sdd = [[3,1],[2,2],[1,3]]
    pd=0
    sd=0
    
    for i in pdd:
        pd += arr[i[0]-1][i[1]-1]
        
    for k in sdd:
        sd+= arr[k[0]-1][k[1]-1]
        
    return pd+sd


print(diagonalDifference(arrrr))
