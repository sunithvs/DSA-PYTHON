
""" A program to find the gcd of a number using euclid's algorithm """
import time


def gcd(m,n):
    """ recursive function to  return the gcd  """
    if m < n:
        m, n = n, m
    if not m % n:
        return n
    else:
        dif = m-n
        return gcd(max(n, dif), min(n, dif))

print(gcd(11, 5))

