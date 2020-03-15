t = int(input())
t = 1

for it in range(t):
    a, b, x, y = map(int, input().split(" "))
    grid = [ [0]*a for ib in range(b)]
    # for ib in range(b):
    #     grid[ib] = list()

    for i in range(b):
        for j in range(a):
            if i == y or j == x:
                grid[i][j] = 1
            else:
                grid[i][j] = 0

    print(grid)