t = int(input())

class Player:
    def __init__(self, _id, x, y):
        self._id = _id
        self.x = x
        self.y = y

for it in range(t):
    sboard = {}
    n, x, y = map(int, input().split(" "))
    p = Player('A', x, y)
    c_A = 65
    for i in range(n):
        _id = ord(c_A)

