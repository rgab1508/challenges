t = int(input())

def is_divisible(n): 
    temp = n 

    while(n): 
        k = n % 10
  
        # check if K divides N 
        if(temp % k == 0): 
            return True
  
        n /= 10; 
  

    return False

for it in range(t):
    n = int(input())

    if n == 1:
        print(-1)
        continue
    
    l_num = "1"
    for i in range(n-1):
        l_num += "0"
    
    for i in range(int(l_num), int(l_num+ "0")):
        # print(i)
        if str(i).count("0") == 0 and str(i).count("1") == 0:
            # print(i)
            if not is_divisible(i):
                print(i)
                break