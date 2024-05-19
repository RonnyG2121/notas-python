#!/usr/bin/env python
import pdb
pdb.set_trace()
def sum(list):
    sum = 0
    for item in list:
        sum += item
    return sum

if __name__ == '__main__':
    digits = []
    for i in range(10):
        digits.append(i)
    sum(digits)