def is_divisible(n): 
    temp = n 

    while(n): 
        k = n % 10
  
        print(k)
        # check if K divides N 
        if(temp % k == 0): 
            return True
  
        n /= 10
  

    return False


print(is_divisible(226))