files = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt"]

f = open(f"inputs/{files[0]}")

nodes = []
MAX_X, MAX_Y, MIN_X, MIN_Y = 0,0,0,0

START_X, START_Y, STOP_X, STOP_Y = map(int, f.readline().split())
N_OF_OBS = int(f.readline())

OBS = []

for i in range(N_OF_OBS):
    _ = list(map(int, f.readline().split()))
    OBS.append(_)


class Node():
    def __init__(self, i, j, x, y):
        self.i, self.j = i, j 
        self.x, self.y = x, y


# def getMinAndMax():
#     maxX,maxY,minX,minY = 0,0, 0, 0
#     for i in range(len(OBS)):
#         for j in range(1, len(OBS[i])+1, 2):
#             if j % 2 != 0:
#                 if OBS[i][j-1] > maxX:
#                     maxX = OBS[i][j-1]
#                 if OBS[i][j-1] < minX:
#                     minX = OBS[i][j-1]
#             if j % 2 == 0:
#                 if OBS[i][j-1] > maxY:
#                     maxY = OBS[i][j-1]
#                 if OBS[i][j-1] < minY:
#                     minY = OBS[i][j-1]

#     return maxX,maxY,minX,minY


# MAX_X, MAX_Y, MIN_Y, MIN_Y = getMinAndMax()

# WIDTH = abs(MIN_X) + abs(MAX_X)
# HEIGHT = abs(MIN_Y) + abs(MIN_Y)

# print(MAX_X,MAX_Y, MIN_X, MIN_Y)


# print(len(range(WIDTH)))
# print(len(range(MIN_X, MAX_X)))
# print(len(range(HEIGHT)))
# print(len(range(MIN_Y, MAX_Y)))

# for i, x in zip(range(WIDTH), range(MIN_X, MAX_X, 1)):
#     for j, y in zip(range(HEIGHT), range(MIN_Y, MAX_Y)):
#         print("IN")
#         n = Node(i, j, x, y)
#         nodes.append(n)

# print(len(nodes))



f.close()