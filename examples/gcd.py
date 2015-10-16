# Given two inputs, print the greatest common denominator
# Usage: python gcd.py 1 2

import sys

def gcd (a, b):
  if b == 0:
    return a
  else:
    return gcd (b, a % b)

if __name__ == "__main__":
  print gcd(int(sys.argv[1]), int(sys.argv[2]))  
