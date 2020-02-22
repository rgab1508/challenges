import math

n = 5
co = []
co_res_of_n = 0

def phi(n):
    p = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            # print(f"{i}/{n} : {n % i} : {math.gcd(n, i)}")
            
            p+=1
    return p
    

def co_res(n):
    C_num = n - phi(n)
    C_den = n - 1

    if C_den % C_num == 0:
        C_num = 1
        C_den = C_den / C_num

    return C_num, C_den

    

for i in range(2, n+1):
    
    _co_res = co_res(i)
    co.append((i,_co_res))


for j in range(len(co)):
    if co[j][1][0] == 1:
        co_res_of_n += co[j][0]


# print(co)
print(co_res_of_n)