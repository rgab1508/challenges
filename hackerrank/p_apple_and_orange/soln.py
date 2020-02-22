

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_in_house = 0
    oranges_in_house = 0
    for i in range(len(apples)):
        if ((apples[i] + a) >= s) and ((apples[i]+a) <= t):
            apples_in_house += 1
        
    for j in range(len(oranges)):
        if ((b + oranges[j]) >= s) and ((b + oranges[j]) <= t):
            oranges_in_house += 1

    print(apples_in_house)
    print(oranges_in_house)
    

if __name__ == '__main__':
    f = open("a.in")
    st = f.readline().split()

    s = int(st[0])

    t = int(st[1])

    ab = f.readline().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = f.readline().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, f.readline().rstrip().split()))

    oranges = list(map(int, f.readline().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
