
""" A simple program to find greatest common factor (gcf) """
import time

def gcd(num1, num2):
    """ Takes two integers and return the gcf """

    i = min(num1,num2)
    while i > 0:
        if not (num1 % i or num2 % i):
            return i
        else:
            i -= 1
