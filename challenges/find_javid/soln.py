##
#   @source discord(one lone coder)
##

TO_FIND = "javid"
TO_FIND_LEN = len(TO_FIND)

f = open("c.in")
l1 = f.readline().split(" ")
M, N = int(l1[0]), int(l1[1])
# M , N = 15, 15

grid = []

for i in range(M):
    l2 = f.readline().strip().split(" ")
    grid.append(l2)



def look_horizontal(i, j):
    found = False
    def look_right(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i][j+_i]
        
        if _ == TO_FIND:
            print(f"Found at {i},{j} - {i},{(j + TO_FIND_LEN)}(horizontal)")
            found = True

    def look_left(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i][j-_i]

        if _ == TO_FIND:
            print(f"Found at {i},{j} - {i},{(j - TO_FIND_LEN)}(horizontal)")
            found = True

    if not (j + TO_FIND_LEN > N):
        look_right(i, j)

    if not (j - TO_FIND_LEN < 0):
        look_left(i, j)

    return found

def look_vertical(i, j):
    found = False
    def look_down(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i + _i][j]
        
        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i + TO_FIND_LEN)},{j}(vertical)")
            found = True

    def look_top(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i-_i][j]

        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i - TO_FIND_LEN)},{j}(vertical)")
            found = True

    if not (i + TO_FIND_LEN > M):
        look_down(i, j)

    if not (i - TO_FIND_LEN < 0):
        look_top(i, j)

    return found



def look_diagonal(i, j):
    found = False
    def look_down_right(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i+_i][j+_i]
        
        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i + TO_FIND_LEN)},{(j + TO_FIND_LEN)}(diagonal)")
            found = True

    def look_down_left(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i+_i][j-_i]

        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i + TO_FIND_LEN)},{(j - TO_FIND_LEN)}(diagonal)")
            found = True

    def look_top_right(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i-_i][j+_i]

        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i - TO_FIND_LEN)},{(j + TO_FIND_LEN)}(diagonal)")
            found = True

    def look_top_left(i, j):
        global found
        _ = ""
        for _i in range(TO_FIND_LEN):
            _ += grid[i-_i][j-_i]

        if _ == TO_FIND:
            print(f"Found at {i},{j} - {(i - TO_FIND_LEN)},{(j - TO_FIND_LEN)}(diagonal)")
            found = True

    if not (i + TO_FIND_LEN > M) and not (j + TO_FIND_LEN > N):
        look_down_right(i, j)

    if not (i + TO_FIND_LEN > M) and not (j - TO_FIND_LEN < 0):
        look_down_left(i, j)

    if not (i - TO_FIND_LEN < 0) and not (j + TO_FIND_LEN > N):
        look_top_right(i, j)
    
    if not (i - TO_FIND_LEN < 0) and not (j -TO_FIND_LEN < 0):
        look_top_left(i, j)

    return found



for i in range(M):
    for j in range(N):
        if grid[i][j] == TO_FIND[0]:
            if look_horizontal(i, j):
                break
            elif look_vertical(i, j):
                break
            elif look_diagonal(i, j):
                break
            else:
                print(f"{TO_FIND} not found")
            
# for i in range(9, 14):
#     print(grid[i][7])