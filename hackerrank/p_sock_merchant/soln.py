import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    pairs = dict()
    for i in range(n):
        if ar[i] in pairs:
            pairs[ar[i]] += 1
        else:
            pairs[ar[i]] = 1

    no_of_pairs = 0
    for key in pairs:
        no_of_pairs += pairs[key]//2

    return no_of_pairs

if __name__ == '__main__':
    f = open("a.in") 

    n = int(f.readline())

    ar = list(map(int, f.readline().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    f.close()
