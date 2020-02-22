from Array2D.Array2D import Array2D

files = ["1_victoria_lake.txt", "b_himalayas.txt", "3_budapest.txt", "4_manhattan.txt", "5_oceania.txt"]
f = open(files[0])

#parsing inputs 

l1 = f.readline().split(" ")
N, M, C, R = int(l1[0]), int(l1[1]), int(l1[2]), int(l1[3])

customers = []
_map = Array2D(M, N)

for i in range(C):
    l2 = f.readline().split(" ")
    _obj = {
        "x": int(l2[0]),
        "y": int(l2[1]),
        "reward": int(l2[2])
    }
    customers.append(_obj)


for i in range(M):
    l3 = f.readline()
    for j in range(0, N):
      
        _map.arr[i][j] = l3[j]



for c in customers:
    _map.arr[c["x"]][c["y"]] = "C"

_map.pprint()