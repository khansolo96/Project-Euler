import numpy as np
import math as m

def prime(p):
    if p == 1:
        return False
    factors = 0
    for i in range(2, m.floor(np.sqrt(p))+1):
        if ((p % i) == 0):
            factors += 1
    if factors == 0:
        return True
    else:
        return False

def nth_prime(n):
    i = 1
    j = 0
    while i > 0:
        if (prime(i) == True):
            j += 1
        if (j ==n):
            break
        i += 1
    return i

x = int(input("Input which prime you need (1st, 2nd, 3rd....):"))
y = nth_prime(x)
print("The ", x, "th prime is: ", y)
