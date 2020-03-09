n = int(input())

a = list(map(int, input().split(" ")))

def check_d(arr):
    f = False
    for i in range(len(arr) - 1):
        if a[i] == a[i + 1]:
            f = True
    
    return f

def shrink_arr(arr):
    global n
    if check_d(arr):
        i = 0
        while(i < n-1):
                if a[i] == a[i + 1]:
                    a[i] = a[i] + 1
                    del a[i+1]
                    n = len(a)
                
                i += 1
    
    if not check_d(arr):
        return arr

    return shrink_arr(arr)


shrink_arr(arr=a)

print(len(a))