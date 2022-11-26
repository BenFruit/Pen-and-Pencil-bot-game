from math import ceil
import random as r

def choose(left):
    if left == 1:
        return 1
    if left <= 4:
        return left - 1
    if (left - 1) % 4 == 0:
        return r.randrange(1,3)
    else:
        step = 1
        while step < left:
            step += 4
        return 4 + left - step