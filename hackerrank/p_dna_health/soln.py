#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, genes, health, first_last_d):
    pass


if __name__ == '__main__':
    f = open("a.in")
    n = int(f.readline())

    genes = f.readline().rstrip().split()

    health = list(map(int, f.readline().rstrip().split()))

    s = int(f.readline())

    first_last_d = []

    for s_itr in range(s):
        firstLastd = f.readline().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        first_last_d.append([first, last, d])

    solve(n, genes, health, first_last_d)

    f.close()