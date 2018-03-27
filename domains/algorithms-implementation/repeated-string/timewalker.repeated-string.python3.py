#!/bin/python3

import sys

def aCount(s):
    c = len(s)-len(s.replace('a', ''))
    return c

def rs(s, n):
    d = int(n / len(s))
    r = n % len(s)
    return (aCount(s) * d) + aCount(s[0:r])

s = input().strip()
n = int(input().strip())
print(rs(s, n))