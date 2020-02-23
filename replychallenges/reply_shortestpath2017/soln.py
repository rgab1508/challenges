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
    def __init__(self, i, j):
        self.i, self.j = i, j 
        

    def setG(self, value=None): 
        if value:
            self.g = value
        else:
            self.g = Node.distFrom(grid[int(START.x)][int(START.y)], self)

    def getG(self): return self.g

    def setH(self): 
        self.h = Node.distFrom(self, grid[max(0, int(END.x)-1)][max(0, int(END.y)-1)])

    def getH(self): return self.h

    def setF(self, value):
        self.f = value

    def getF(self): return self.f

    @staticmethod
    def distFrom(a, b):
        return math.sqrt((b.i - a.i)**2 + (b.j - a.j)**2)


