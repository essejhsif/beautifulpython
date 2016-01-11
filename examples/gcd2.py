# Given two inputs, print the greatest common denominator
# Note: this is not using recursion, but is 'beautiful' nonetheless
# Usage: python gcd2.py 1 2

import sys

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

if __name__ == "__main__":
  print gcd(int(sys.argv[1]), int(sys.argv[2]))  
