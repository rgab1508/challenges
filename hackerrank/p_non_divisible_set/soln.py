
import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    ss = []
    n = len(s)
    s = list(set(s))
    s = sorted(s)
    blacklist = []
    for i in range(n):
        for j in range(n):
            print(f"{s[i]}+{s[j]}: {s[i]+s[j]} :{(s[i]+s[j]) % k}")
            if (s[i] + s[j]) % k != 0:
                # print(f"{s[i]}+{s[j]}: {s[i]+s[j]} :{(s[i]+s[j]) % k}")

                if s[i] not in ss and s[i] not in blacklist:
                    ss.append(s[i])
            else:
                blacklist.append(s[i])
                if s[i] in ss:
                    ss.remove(s[i])
        

    return ss
    

if __name__ == '__main__':
    f = open('a.in')

    first_multiple_input = f.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, f.readline().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)

    f.close()
